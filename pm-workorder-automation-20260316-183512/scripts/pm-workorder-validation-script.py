# pm-workorder-validation-script.py
#
# Purpose:
#  - Validate inspection work orders generated from PMs
#  - Ensure required fields (ASSETNUM, PRIORITY) are populated
#  - Log creation of new inspection WOs
#
# Usage:
#  - OBJECT: WORKORDER
#  - EVENTS:
#       1) Add / Initialize (for new WOs)
#       2) Save (optional extensions for completion validation)
#
# Assumptions:
#  - 'mbo' and 'service' variables are provided by Maximo runtime
#  - Script is attached only to WORKORDER and optionally guarded by
#    a launch point condition (e.g., WORKTYPE='INSP')

from psdi.server import MXServer
from psdi.mbo import MboConstants

def beforeSave():
    """
    Sanity checks prior to save:
      - Ensure ASSETNUM is populated for inspection WOs
      - Default PRIORITY if not provided
    """
    # Only apply to inspection work orders
    worktype = mbo.getString("WORKTYPE")
    if worktype and worktype.upper() != "INSP":
        return

    asset = mbo.getString("ASSETNUM")
    location = mbo.getString("LOCATION")

    if not asset and not location:
        # Either asset or location should be present
        raise Exception("Inspection Work Order must have an ASSETNUM or LOCATION.")

    priority = mbo.getInt("PRIORITY")
    if priority is None or priority == 0:
        # Default to MEDIUM priority = 3 (example)
        mbo.setValue("PRIORITY", 3, MboConstants.NOACCESSCHECK)
        service.log("Defaulting PRIORITY to 3 (MEDIUM) for inspection WO " + mbo.getString("WONUM"))

# Script entry point
if mbo is not None:
    try:
        # Log creation of new inspection WO
        if mbo.isNew():
            pmnum = mbo.getString("PMNUM")
            service.log("New inspection WO created from PM: %s, WONUM: %s" %
                        (pmnum, mbo.getString("WONUM")))
        beforeSave()
    except Exception as e:
        service.log("Inspection WO validation script error: " + str(e))
        # Optionally re-raise to block the transaction
        # raise