# Functional Design: Maximo PM Data Migration

This document describes the functional aspects of migrating PM data into Maximo 8.x.

## Business Requirements (Summary)

- Load legacy PM schedules from source systems into Maximo
- Map source fields to Maximo PM data Custom Before Load tables (e.g. 'INT_PM')
- Validate mandatory fields and anchor's values with asset, location, and calendar revers
- Handle lookup values for frequency, usage, jobplan, alignments, etc.
- Ensure rexusable load with rerun and validation reports
- Configure PM generated Work Order body parameters and trigger settings

## PMO scope and mainObjects

- PM (main class)
- PMWORKITEM (PM Work Order Schedules)
- ASSET (Assets linked to PM)
- LOCATION (optional, for location-based PM)
- WORKLOG (STATIONNAME)
- CALENDAR and WORLDAMCROSS (schedule reference)
- Lookup tables for frequency, useclass, jobPlanname, shiftmethopd

## High-level Functional Design Elements

- Default values for missing non-mandatory fields
- Data validation roles and error handling
- Staging load with structured validation rules
- Audit trails for asset & PM lins before go-live
