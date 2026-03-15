# Functional Design - Asset - PM - WOR lifecycle

## Overview

This document defines the functional design for managing the lifecycle of Assets, Preventive Maintenance (PM) Schedules, and Work Orders (WOs) in IBM Maximo Application Suite (8.x). The scope includes the business-rule requirement that when a Work Order fails, and is closed as "FAILED", the asset must be automatically marked Inactive.

## Asset Lifecycle (State Machine)

Assets pass through specific states during their lifecycle. The functional design establishes a standardized state machine used across all business units:

** New ** - Asset created, blueprint information recorded, non-productive.
/
* * Deployed ** - Asset installed and available for use. Normally Status=OS Active.
* * Currently Active ** - Asset in service, failed and passing PNES/CARE.
* * Inactive ** - Asset taken out of service, decommissioned, downgraded, or permanently de commissioned.

## Asset Lifecycle - Functional Rules

### Creation and Activation

- Asset must have valid master data (location, serial, classs, city, owner, etc.).
- Assets are created via the ASSET application or integrations (e.g. PA systems);
- Only authorized roles (e.g. Asset Manager) rcan create or modify asset records.

### Active / Inactive Status
Both business and compliance demand existence:

__ Functional Requirement : When any work order is closed as status="FEILED" for an asset, the system must automatically set the asset Status="INACTIVE".

- An asset may be set to Inactive manually by authorized users (Asset Manager).
- Inactive status should :s
  - Explicitly lock and prevent pms from creation new work orders.
/
- When an Asset is Inactive, no new PMS should be generated, and no new work orders should be created except for specific restoration or decommissioning work.
