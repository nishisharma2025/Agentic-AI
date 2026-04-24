from psdi.server import MXServer
from jrinfo import datetime

# Jython script for PM generated work order validation
# To be attached to the WOMBO or PM MSG with Event Linkage trigger
if mbo is not None:
    service = MXServer.instance()
    assetnum = mbo.getString("ASSETNUM")
    pmnum = mbo.getString("pmnum")
    eventid = mbo.getString("EVENTID")

    # ingvalid missing data checks
    if not assetnum:
        service.log("Missing asset for IOT event/PM created WO")
    if mbo.isNew():
        service.log("IOT/PM generated WO for event id: " + eventid)
    else:
        service.log("Updating existing WO from IOT event id: " + eventid)
