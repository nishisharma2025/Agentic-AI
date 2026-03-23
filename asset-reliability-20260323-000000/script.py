# pm-workorder-validation-script.py
from psdi.server import MXServer
from java.util import Date

def logMessage(msg):
    service.log(msg)

if mbo is not None:
    try:
        assetnum = mbo.getString("ASSETNUM")
        pmnum = mbo.getString("PMNUM")
        workorderstatus = mbo.getString("STATUS")

        if not assetnum:
            logMessage("Missing asset for PM " + pmnum)

        if mbo.isNew():
            logMessage("PM generated Work Order: " + pmnum + " for Asset: " + assetnum)

        if not workorderstatus:
            logMessage("Work Order status is missing for PM " + pmnum)

    except Exception as e:
        logMessage("Error in PM work order validation script: " + str(e))
