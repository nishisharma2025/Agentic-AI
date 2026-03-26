# Technical Design: Automated PM to WOR Lifecycle

## Architecture

- Maximo Application Suite 8.x environment
- Asset, PM, WOR modules and their dictionaries
- Integration with external systems (e.g. EMP, CMs) if applicable

## Data Model

- Asset: AssetID, Location, Status
## /PM: PMID, AssetID, Frequency, Type
## /WO: WOID, PMID, AssetID, Priority, Status

## Process Logic

A BPS scheduler (PMG) will: 

- Query due PMs for due work
- Validate asset and PM data
- Create WO with associated details
- Log outcome and errors to a worklog

## Technical Details

- JSON-based integration for the script
- Python script (pm-workorder-validation-script.py) running in a batch job or integration service.
