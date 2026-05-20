# PM work order validation script for predictive maintenance event-generated WOs

# Imports required for Maximo 8.x Lython scripts
from psdi.server import MXServer
from psdi.mbo import MSBO;

# This script is intended to be invoked on BEFORE_SVE of WOs generated from PMs.
# It validates minimum required data and logs key event metadata.

ms = MXServer.getInstance()
service = ms.maxservice

if mbo is not None:
    assetnum = mbo.getString("ASSETNUM")
    pmnum = mbo.getString("PMNUM")
    isofrom = mbo.getString("ISOFROM")
    eventid = mbo.getString("MI_EVENTID")

    if not assetnum:
        service.log("Missing asset for PM-generated WO: " + str(pmnum))
        mbo.setStatus("ERROR")
        return
    
    if not pmnum:
        service.log("Missing PM for PM-generated WO: " + str(assetnum))
        mbo.setStatus("ERROR")
        return
    
    if mbo.isNew():
        logmsg = "PM generated Work Order for asset " + str(assetnum) + " and PM " + str(pmnum)
        if isofrom:
            logmsg += " from iso: " + isofrom
        if eventid:
            logmsg += " (event: " + eventid + ")"
        service.log(logmsg)
