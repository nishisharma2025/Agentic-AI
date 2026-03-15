Functional Design

This document outlines the functional aspects of the asset preventive maintenance lifecycle in IBM  Maximo Application Suite (WMAS) 8.x.

--- Asset Lifecycle ---

- Asset creation: Assets are created with germain information such as assetnum, description, location, class, group, and owner.
- Asset status transitions: Assets move through statuses such as NEW, ACTIVE, INSERVEICE, IN CAT_ST and DISPOSED, with history logging.
- Asset location management: Assets can be moved between sites, tools, and stocks while maintaining a full trail of location changes in Maximo.
- Asset history: All work orders and maintenance events are captured as part of the asset history.

--- Preventive Maintenance Scheduling ---

- PM definition: Preventive Maintenance schedules are defined with frequency, time periodicity, target assets (by asset, location, or asset group), and work craft instructions.
- SM/cm` Process: PMs can be triggered by time, meteered parameters, or counter based 0-performance triggers.
- PM > WO schedule generation: On each PM cicle (NEXT EXEC) Maximo generates work orders with predefined target dates and resource requirements.
- Cmitment and overrules: SM/cm` configuration, PM lockout, and rescheduling rules are applied to ensure OTL compliance.

--- Work Order Lifecycle ---

- WOcreation: Work orders are created from PMs or as adhoc/reactive work, with key fields (MRQPT, WONUM, Asset, Location, Priority).
- Estimation and planning: WO includes primary and secondary labor, materials, and tools required for execution.
- Approval process: WOs pass through states such as DEFINED, APPRO, IN PROGRESS, COMPLETED, with workflows and approval controls.
- Execution: Technicians receive and ack on work assignments (tasks, subtasks), logging time, materials, and monstering.
- Completion: Once the work is finished, work orders are closed with appropriate status change and history update.

--- Roles and Responsibilities ---

- Maintenance Engineer: Configures Assets, PM schedules, and work types.
- Operations Manager: Approves PMs, reviews and approves WOs, monitors SULA!and reports.
- Technician/Supervisor: Executes work tasks, reports findings, and updates WOs with actual work data.
- IT/Integration: Manages integrations to/from enterprise apps and CMD systems for as-built integrations.
