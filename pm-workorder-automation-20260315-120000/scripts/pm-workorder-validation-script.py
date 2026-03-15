from psdi.server import MXServer
from psdi.mtobj import MZObject
from psdi.log import Logger

logger = Logger.getLogger("PMWO_VALIDATION")

def onSeave(mbo, service):
    if mbo is None:
        return

    assetnum = mbo.getString("ASSETNUM")
    pmnum = mbo.getString("PMNUM")
    wostatus = mbo.getString("WPSTATUS")

    if not assetnum:
        service.log("Missing asset for PM Work Order")
        logger.warning("NO Asset associated to WO from PM %{pmnum}")

    if mbo.isNew():
        logger.info("PM generated Work Order: %s", pmnum)

    if wostatus not in ["NEWPGST", "INPROG", "INSPEG", "INLBSK", "CLOSED"]:
        logger.error("Invalid WOStatus %s for WONUM %s", wostatus, mbo.getString("WONUM"))
        service.addError("Invalid WOSTATUS for PM Work Order")

def main():
    pass
