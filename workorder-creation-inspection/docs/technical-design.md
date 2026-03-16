# Technical Design: Automated Inspection Workflow in IBM Maximo 8.x

## 1. Architecture Overview

### 1.1 Components

- IBM Maximo Application Suite 8.x (EAM)
  - Asset, Location, PM, WO, Inspection, Automation Scripts
- Maximo Mobile for EAM
- Integration Layer
  - REST/JSON APIs
  - Message queues or integration bus (as applicable)
- Data Lake / Analytics Platform
- External ERP (optional)
- Directory / IAM (SSO, LDAP, OIDC)

### 1.2 Logical Flow

1. PM records define inspection schedules and link to Inspection Forms.
2. Cron task generates inspection WOs on schedule.
3. WOs are assigned to inspectors.
4. Inspectors execute WOs on Maximo Mobile with inspection forms.
5. On completion:
   - Inspection results are saved.
   - Automation script validates data and may create follow‑up WOs.
6. Data is replicated to data lake for analytics.

---

## 2. Data Model and Relationships

### 2.1 Core Objects

- ASSET
  - Key fields: ASSETNUM, SITEID, STATUS, CLASSSTRUCTUREID, LOCATION
- LOCATION
  - Key fields: LOCATION, SITEID, TYPE
- PM
  - Key fields: PMNUM, SITEID, ASSETNUM, LOCATION, FREQUENCY, PMSTATUS
  - Custom fields (if needed): INSPECTIONFORMNUM, CRITICALITY, REGULATORYFLAG
- WORKORDER (WO)
  - Key fields: WONUM, SITEID, WORKTYPE, STATUS, PMNUM, ORIGRECORDID/CLASS, ASSETNUM, LOCATION
  - For inspection WOs: WORKTYPE = 'INSP' (configurable)
- INSPECTION / INSPECTIONTEMPLATE
  - TEMPNUM, DESCRIPTION, STATUS
- INSPECTIONRESULT
  - Links to WORKORDER and INSPECTIONTEMPLATE
- AUTOSCRIPT
  - For validation and follow‑up logic

### 2.2 Relationships

- PM → WORKORDER
  - Existing Maximo PM‑to‑WO generation logic.
- WORKORDER → INSPECTIONRESULT
  - Based on INSPECTIONFORMNUM or template association.
- WORKORDER (Inspection) → WORKORDER (Follow‑up)
  - Via ORIGRECORDID / ORIGRECORDCLASS or custom relationship.

---

## 3. PM and WO Configuration

### 3.1 PM Configuration

- Use Maximo PM application to:
  - Set frequency (time‑based, meter‑based).
  - Associate PM to asset or location.
  - Set WORKTYPE = INSP in PM or via Job Plan.
  - Store INSPECTIONFORMNUM (custom attribute or use existing inspection linkage) via:
    - Crossover domain, or
    - Automation script that sets the related inspection template.

### 3.2 Cron Task

- Utilize existing PMWOGEN or custom cron settings:
  - Ensure only inspection PMs (e.g., WORKTYPE = INSP) are selected.
  - Run daily or more frequently depending on inspection policy.
  - Generate WOs with:
    - Correct site
    - Owner group based on asset/location
    - Proper target dates.

---

## 4. Maximo Mobile Configuration

### 4.1 App Setup

- Configure Maximo Mobile for EAM:
  - Add a custom "Inspection" app or configure existing Work Execution app:
    - Filter to show only inspection WOs (WORKTYPE = INSP).
    - Enable inspection form rendering.

### 4.2 Offline Data

- Offline data sets:
  - Assigned WOs, recent history
  - Assets, Locations, Classifications
  - Inspection templates and questions
- Ensure data size is controlled via:
  - Site filters
  - Owner group / user‑based filters
  - Date ranges

---

## 5. Automation Script Design

### 5.1 Triggers

- Script 1: On inspection WO creation (OBJECT: WORKORDER, EVENT: Add or Initialize)
  - Validate ASSETNUM/LOCATION are present.
  - Set default PRIORITY if empty.
- Script 2: On inspection completion (OBJECT: WORKORDER, EVENT: Save, condition status change to COMP)
  - Validate inspection results completeness.
  - Create follow‑up WOs if needed.

### 5.2 Sample Script (see full script file in /scripts)

- File: `pm-workorder-automation-20260316-183512/scripts/pm-workorder-validation-script.py`
- Language: Jython
- Functions:
  - Check ASSETNUM presence.
  - Default PRIORITY for inspection WOs.
  - Log creation of new inspection WOs.
  - This can be extended to:
    - Read INSPECTIONRESULT rows.
    - Create corrective WOs based on out‑of‑range values.

---

## 6. Integration Design

### 6.1 ERP Integration (Optional)

- Outbound:
  - WO costs, completion information to ERP.
- Inbound:
  - Cost centers, GL accounts to Maximo.
- Mechanism:
  - REST APIs or integration framework (MIF) with JSON/XML.

### 6.2 Data Lake / Analytics

- Periodic export of:
  - ASSET, WORKORDER, PM, INSPECTIONRESULT.
- Options:
  - Database views + ETL
  - Direct MIF integration to Kafka / REST endpoints.

---

## 7. Security and Audit

- Security groups:
  - INSPECTOR: Can view/execute inspection WOs, update results.
  - PLANNER: Can maintain PMs, configure inspection forms.
  - SUPERVISOR: Can approve WOs, view reports.
- Audit:
  - Enable attribute auditing on:
    - WORKORDER.STATUS
    - INSPECTIONRESULT values
  - Log automation script events to service.log or custom log.

---

## 8. Deployment and Migration

- DEV → TEST → PROD promotion process:
  - Move configuration via:
    - Migration Manager packages for:
      - Domains / attributes
      - Automation scripts
      - App designer configurations
      - Security groups
  - Mobile configuration deployed through MAS tools.

- Data migration tasks:
  - Load initial PMs from existing spreadsheets.
  - Load inspection templates.