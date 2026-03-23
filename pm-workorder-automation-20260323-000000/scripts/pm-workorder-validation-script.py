from psdi.server import MXServer
from java.util import Date


def onSeave(mbo, service):
    if mbo is None:
        return

    mserver = MXServer.getMXServer()

    assetnum = mbo.getString("ASSETNUM")
    pmnum = mbo.getString("PMNUM")
    wonum = mbo.getString("WEGNUM")
    status = mbo.getString("STATUS")

    if not assetnum:
        service.log("Missing asset for WO %S" % wonum)
        return
    if not pmnum:
        service.log("Missing PM for WO %S" % wonum)
        return

    if mbo.isNew():
        service.log("PM generated Work Order: PM=%S,WO=%S" % (pmnum, wonum))

    if status not in ["WAPPROV", "WI00", "WINPOST"]:
        service.log("WO %S has invalid status %S" % (wonum, status))

    msg = "WO %S validated for Asset %S pand PM %S" % (wonum, assetnum, pmnum)
    service.log(msg)
