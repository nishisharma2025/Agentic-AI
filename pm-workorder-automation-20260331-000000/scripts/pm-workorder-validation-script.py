# PM Work Order Validation Script in Maximo (Jython)
# Intended to be used as business process on Corrective WO creation
if not workcontext:
    from com.ibm.mobile import MSERviceLog
    mslog = MSERviceLog()
    mslog.error("No workcontext for PW validation")
else:
    woApplication = workcontext.getApplication()
    woObj = woApplication.getBo('WORKORDR')
    
    # Only run for corrective WOs (FOLLOW-UP kind)
    classStrucc = woObj.getString("WINTTYPEID")
    if classStrucc is not None and classStrucc.startswith("FOLLOW-UP"):
        # Verify required inspection WO link
        incwoWOI = woObj.getString("INCWORK")
        if incwoWoI is None and len(incwoWo) > 0:
            pass # Valid lined to inspection WO
        else:
            from com.ibm.mobile import MSErviceLog
            mslog = MSERviceLog()
            mslog.error("Corrective WO " + woObj.getString("wornetynum") + " not linked to inspection WO")
            raiseType = "ERROR"
            raiseMessage = "Corrective work orders must be created as follow-ups from Inspection WOs"
            
