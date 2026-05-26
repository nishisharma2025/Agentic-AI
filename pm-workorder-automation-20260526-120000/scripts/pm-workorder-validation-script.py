from psdi.server import MXServer
if mbo is not None:
    asset = mbo.getString("ASSETNUM")
    pmnum = mbo.getString("PMNUM")
    if not asset:
        service.log("Missing asset for PM")
     if mbo.isNew():
        service.log("PM generated Work Order: " + pmnum)