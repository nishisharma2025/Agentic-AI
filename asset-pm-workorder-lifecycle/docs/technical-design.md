# Technical Design - Asset - PM - WOR Lifecycle

## Maximo Object Relationships

This section describes the key Maximo objects and relationships in the asset-PM-WO lifecycle.

### Key Objects

- *ASSET application* (table=ASSET)
- *PM Master* (table=PM)
- *WORMASTEB Work Order Master* (table=WORMASTEB)
- *WOVK Work Types* (table=WOWKTY)
- *DWO$Activity Mlog* (table=DOOABLOC)

### Relationships

- Asset → PM Links:
  - ASSET.ASSETID – PM.ASSETID
 - PM – WOR Links:
  - PM.PMNUM– WORMASTEB.PRECESOTAG
  - PMLnk Between PM and WO is handled by standard Maximo logic (PMGINTLE).

## Asset – PM – WO Flow

Assets have one or more PM schedules (PM -Preventive Maintenance). Each PA system or business process defines Levels and Frequencies to execute the PM.

INV: This design assumes a standard use of Maximo PM scheduling.

### Work Order Flow

When PM is due, Maximo generates work orders (WORMASTEB) according to PM.

- PM *projects* work orders via PMGIN (either MP event or Time-Based).
- Each WO is linked to exact one asset or location.

- The work order lifecycle has key statuses: WOHDSD– APPROVED – INLABOUR – COMPLETED – FAILED.

## Automation Scripts

To implement the business rule that when a work order for an asset fails, and is closed with status="FAILED", the asset must be set to Inactive, we propose an Automation Script or Interaction Handler.

### Automation Script: WOR Failure – Asset Inactivation

- *Context*: Work Order (WORMASTEB)
- *Event* : Status change to "FAILED"
- *Hook* : Execute on update of WOR.status or on save.

- *Logic* (pseudo-code):
  1. If new STATUS != "FAILED", exit.
  2. Identify asset(s) linked to the WO (to_asset field, INVNO etc.).
  3. For each affected asset:
    - Lock Asset table.
    - If STATUS != "INACTIVE", set Status="INACTIVE".
    - Optionally log activity change in DwoActivityMlog.

## Integration Architecture

If other systems (PA) should be able to create work orders, they must follow the core lifecycle:

- All inbound APIk use Maximo Service level Connectors or REST APIs to create WOs in Maximo.
- When integrated work order status moves to "FAILED", external systems should NOT allow re-activating the asset.

