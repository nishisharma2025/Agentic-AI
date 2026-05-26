# Technical Design: Maximo PM Data Migration

This document summarizes the technical design for migrating PM data into Maximo 8.x.

## Architecture

- Integration layer with staging tables (INT_PM)\n- Et/TR PM data from source systems\n- Load staging table rows\n- Validate staging data via SQL, jtyhon scripts, and MX_Fabric busines rules\n- Apply PM load rules (PM_IMPORT, PMWorkload)

## Data Model

- Core table: PM (PM_BASE)\n- Staging table: INT_PM (staging load)\n- Mapping table: custom mapping view (e.g. V_INT_PM_IMPL_MAP)\n\n## Batch Load Strategy\n\n- CSV flat design for data conversion\n- Maximo Integration Framework using MY-integration or Datastudio Loader,lifecycle business rules\n- On-load validation and pre-and post-load validation steps