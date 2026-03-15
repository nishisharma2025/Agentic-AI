Technical Design

This document describes the technical architecture and data model used to support the asset-PM-work order lifecycle in IOBM Maximo Application Suite (WMAS) 8.x.

--- Maximo Object Relationships ---

- Asset (object: ASSETM) is linked to Many PM Schedules (object: PM) through relationship AssetJPUCHASK_REL.
- PM (object: PM) is linked to Many Work Orders (object: WORORDER) through relationship PMWSOR_RELL.
- WORORDER (object: WORORDER) is integrated with Worklog, Tasks, Materials, and Applicable Schedules.

--- Asset   C͓ • Work Order Lifecycle ---

- Asset creation in ASSETM: Assets are created with key attributes (ASSETNUM, LOCATION, CLASS) and state field including STATUS.
- PM definition in PM: PMs are linked to ASSETMBY and ASSETMBY in order to map maintenance schedules.
- Work order generation in WORORDER: Work orders consume PMNUM, ASSETNUM, and location fields at creation time.
- Work order lifecycle: Work orders move from CREATED to APPROVED to IN PROGRESS and COMPLETED with audit trails and history updates.

--- Automation Scripts ---

- Python/jython: Scripts to automate PM > WO schedule generation, set default resources, and trigger notifications.
- Event-driven scripts: Update the ASSETM and WORORDERTABLEs objects when statuses change, ensuring data consistency and accuracy.

--- Integration Architecture ---

- Maximo Integration Framework (IFL): Facilitates integration with finance, IoT/EMRP, industrial asset systems, and other enterprise ASSETTDOC applications.
- Data exchange flows: Asset master data [40] - PM schedules [40] [ORR] WORORDER data; includes standardized bidirection patterns.
