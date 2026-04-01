# pm-workorder-validation-script.py
# Jython Automation Script for Maximo 8.x
#
# Purpose:
#  - Validate PM Work Orders before completion.
#  - Ensure all mandatory inspection questions are answered.
#  - Verify that critical inspection failures have corresponding corrective WOs.
#
# Launch Point:
#  - Object Launch Point on WORKORDER
#  - Events: Before Save
#  - Conditions: Only when STATUS is changing to 'COMP' and WOTYPE = 'PM'
#
# Assumptions:
#  - Inspection results are stored in an INSPECTIONRESULT (example) MBOSet linked by WONUM/SITEID.
#  - A custom cross-reference table INSPECTION_RULES is available with fields:
#       INSPQUESTIONID, SEVERITYLEVEL, AUTOCREATEWO
#  - Corrective WOs are created as children with PARENT = PM WONUM or ORIGRECORDCLASS/ID set.
#
# NOTE:
#  - Adjust object names and attributes to match your specific configuration.

from psdi.server import MXServer
from psdi.mbo import MboConstants
from psdi.util.logging import MXLoggerFactory

logger = MXLoggerFactory.getLogger("maximo.script.pmworkorder.validation")

# 'mbo' and 'service' are injected by Maximo Automation Script runtime
if mbo is None:
    # Nothing to validate
    if logger.isDebugEnabled():
        logger.debug("No MBO in context for PM WO validation script.")
else:
    try:
        wotype = mbo.getString("WOTYPE")
        newstatus = mbo.getString("STATUS")  # This is the value being set in this transaction
        siteid = mbo.getString("SITEID")
        wonum = mbo.getString("WONUM")

        if logger.isDebugEnabled():
            logger.debug("PM WO Validation Script called for WONUM=%s, SITEID=%s, WOTYPE=%s, STATUS=%s" % (wonum, siteid, wotype, newstatus))

        # Only validate when this is a PM WO that is being completed
        if wotype != "PM" or newstatus != "COMP":
            # Not applicable - exit silently
            if logger.isDebugEnabled():
                logger.debug("Skipping validation (WOTYPE!=PM or STATUS!=COMP).")
        else:
            mxServer = MXServer.getMXServer()

            # 1. Retrieve Inspection Results for this Work Order
            # NOTE: Replace object/relationship names to match your configuration.
            inspMboSet = mbo.getMboSet("INSPECTIONRESULT")  # Example relationship name
            mandatory_missing = []
            critical_failures = []

            if inspMboSet is None or inspMboSet.isEmpty():
                # No inspection results found - this may be invalid if inspections are mandatory
                msg = "No inspection results found for PM WO %s. Completion not allowed." % wonum
                logger.info(msg)
                service.error("pmvalidate", "INSPECTION_MISSING")

            # Utility: get rules for a given question
            def getRuleForQuestion(questionId):
                rulesSet = mxServer.getMboSet("INSPECTION_RULES", mbo.getUserInfo())
                rulesSet.setWhere("INSPQUESTIONID = '%s'" % questionId.replace("'", "''"))
                rulesSet.reset()
                ruleMbo = rulesSet.getMbo(0)
                # NOTE: Keep rulesSet open only briefly; close to avoid resource leak
                rulesSet.close()
                return ruleMbo

            # Iterate through inspection results
            inspMbo = inspMboSet.moveFirst()
            while inspMbo:
                questionId = inspMbo.getString("QUESTIONID")  # Example attribute name
                answer = inspMbo.getString("ANSWER")
                mandatory = inspMbo.getBoolean("MANDATORY") if inspMbo.isNull("MANDATORY") is False else False

                if logger.isDebugEnabled():
                    logger.debug("Inspecting question %s, answer=%s, mandatory=%s" % (questionId, answer, mandatory))

                # Check for mandatory questions unanswered
                if mandatory and (answer is None or answer.strip() == ""):
                    mandatory_missing.append(questionId)

                # Evaluate critical failure rules via rules table
                rule = getRuleForQuestion(questionId)
                if rule:
                    severity = rule.getInt("SEVERITYLEVEL")
                    autoCreateWO = rule.getBoolean("AUTOCREATEWO")
                    # Example failure logic: answer == 'FAIL' or numeric out-of-range
                    # For simplicity, we check for FAIL text; adjust as needed
                    if answer and answer.upper() in ["FAIL", "FAILED", "NO"]:
                        if severity <= 2:  # 1 or 2 considered critical
                            critical_failures.append({
                                "questionId": questionId,
                                "severity": severity,
                                "autoCreateWO": autoCreateWO
                            })

                inspMbo = inspMboSet.moveNext()

            # 2. Validate mandatory answers
            if mandatory_missing:
                logger.info("Mandatory inspection questions missing for WO %s: %s" % (wonum, ", ".join(mandatory_missing)))
                # Raise error message referencing message group/key configured in Maximo
                service.error("pmvalidate", "MANDATORY_Q_MISSING")

            # 3. Validate critical failures have corrective WOs
            if critical_failures:
                # Check for existing Child or Follow-up WOs
                childSet = mbo.getMboSet("CHILDREN")  # Use CHILDREN or appropriate relationship
                hasCorrectiveForCritical = False

                if childSet is not None and not childSet.isEmpty():
                    childMbo = childSet.moveFirst()
                    while childMbo:
                        childType = childMbo.getString("WOTYPE")
                        origClass = childMbo.getString("ORIGRECORDCLASS")
                        # Heuristic: treat CM child or follow-up as corrective
                        if childType == "CM" or (origClass == "WORKORDER" and childMbo.getString("ORIGRECORDID") == wonum):
                            hasCorrectiveForCritical = True
                            break
                        childMbo = childSet.moveNext()

                if not hasCorrectiveForCritical:
                    # No corrective WO found for critical failures
                    logger.info("Critical inspection failures detected without corrective WO for PM WO %s" % wonum)
                    # Raise generic error; finer-grained messages can be configured
                    service.error("pmvalidate", "CRIT_FAIL_NO_CORR_WO")

    except Exception, e:
        # Ensure all exceptions are logged but do not corrupt transaction
        logger.error("Error in PM WO validation script for WONUM=%s: %s" % (mbo.getString("WONUM"), str(e)))
        # Depending on policy, either block completion or allow with warning.
        # To block, uncomment the next line and create appropriate message key:
        # service.error("pmvalidate", "GENERIC_ERROR")
        # To allow but log, do not re-raise.
        pass