from psdi.server import MXServer
from java.util import Date

if mbo is not None:
    service = MXServer.getInstance()
    assetnum = mbo.getString("ASSETNUM")
    pmnum = mbo.getString("pmNum")
    if not assetnum:
        service.log("Missing asset for work order")
    if mbo.isNew():
        service.log("PM generated Work Order: " + pmnum)