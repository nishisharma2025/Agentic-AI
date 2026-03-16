# Functional Design: Automated Inspection Workflow in IBM Maximo 8.x

## 1. Scope and Scenario
Scenario: **PM Work Order Automation** for inspections.

The solution automates the lifecycle from scheduled inspection PMs to inspection work order execution, validation, and follow‑up work.

## 2. Key Modules and Actors

### Maximo Modules
- Assets (ASSET)
- Locations (LOCATION)
- Preventive Maintenance (PM)
- Work Order Tracking (WO)
- Job Plans (JOBPLAN) – optional for standardized tasks
- Inspection Forms (INSPECTION, INSPECTIONRESULT)
- Automation Scripts (AUTOSCRIPT)
- Assignment Manager
- Maximo Mobile for EAM
- Reporting (BIRT/ Cognos / MAS Dashboards)

### External Components
- ERP (for cost centers, financial posting if needed)
- Data Lake / Analytics platform
- Directory / IAM for authentication (SSO)

### Actors
- Maintenance Planner
- Maintenance Supervisor
- Field Inspector / Technician (mobile)
- Reliability Engineer
- Compliance / HSE Officer
- Maximo Administrator

## 3. Functional Requirements

### 3.1 PM and Inspection Definition

**FR‑1**: Define inspection‑type PMs  
- PMs with frequency (time‑based) and optionally meter‑based triggers.  
- PMs associated to:
  - Asset(s)
  - Location(s)
  - Asset Class or Classification (via routes/job plans as needed)

**FR‑2**: Link PMs to inspection forms  
- Each inspection PM is linked to one Inspection Form.  
- Multiple PMs may reuse the same Inspection Form for standardization.

**FR‑3**: Risk / criticality attributes  
- PMs store criticality (LOW/MEDIUM/HIGH) and regulatory flags.  
- Criticality and regulatory flags can be used for reporting and prioritization.

### 3.2 Automatic WO Generation

**FR‑4**: Scheduled WO generation  
- Cron task generates inspection WOs based on active PMs and due dates.  
- WOs have:
  - Work Type = "INSP" (or site‑specific value)
  - Proper asset/location references
  - Target start/finish dates according to PM schedule
  - Owner group / owner defaults based on asset/location/PM

**FR‑5**: Bulk generation and review  
- Planners can review auto‑generated WOs in a list.  
- Ability to filter by:
  - Site
  - Asset/Location
  - PM / Work Type
  - Criticality

### 3.3 Assignment and Mobile Execution

**FR‑6**: Assignment to inspectors  
- Supervisor assigns WOs to individuals or crews (Assignment Manager or Work Centers).  
- Priority and required completion date visible to supervisor.

**FR‑7**: Maximo Mobile execution  
- Inspectors view assigned inspection WOs offline/online.  
- Mobile app presents the correct Inspection Form automatically.  
- Inspectors can:
  - Capture readings, pass/fail, multi‑choice responses, photos, and comments.
  - Attach documents and images directly from mobile.
  - Work offline and sync data when connectivity is available.

### 3.4 Inspection Forms and Data Capture

**FR‑8**: Inspection form design  
- Support for:
  - Numeric measurements (with limits)
  - Text responses
  - Yes/No, Pass/Fail
  - Dropdowns and multi‑select options
  - Conditional questions (display rules based on previous answers)

**FR‑9**: Validation rules  
- Local validation:
  - Required fields
  - Range checks (min/max)
  - Conditional required fields (e.g., "If Fail then comment mandatory")
- Central validation:
  - Automation script triggered on WO status change or inspection completion.

**FR‑10**: Auto‑generation of follow‑up WOs  
- Based on inspection results and rules:
  - If reading outside tolerance → create corrective WO.
  - If failure code is critical → create high‑priority WO and notify supervisor.
  - Link follow‑up WO(s) back to originating inspection WO.

### 3.5 Status Management

**FR‑11**: WO status lifecycle (for inspection WOs)  
Common statuses:
- WAPPR – Waiting for Approval (optional)
- APPR – Approved
- INPRG – In Progress
- COMP – Completed
- CAN – Canceled

Rules:
- Only APPR/INPRG WOs can be executed on mobile.
- Completion is allowed only if all required inspection responses are present.

**FR‑12**: Status automation  
- On mobile completion and successful validation:
  - WO status set to COMP.
- On validation failure:
  - WO remains INPRG or goes to a custom status (e.g., "INSPERR") with logged error details.

### 3.6 Reporting and Analytics

**FR‑13**: Operational reporting  
- Standard reports / KPIs:
  - Overdue inspections by site/asset
  - Completed inspections by period
  - Compliance rate (% on‑time)
  - Follow‑up work generated vs. completed

**FR‑14**: Data export to data lake  
- Regular export of inspection results, WOs, and asset data for advanced analytics.  

### 3.7 Security and Authorization

**FR‑15**: Role‑based access  
- Planners and supervisors:
  - Maintain PMs, inspection forms, assignments.
- Technicians:
  - Execute and update WOs, record inspections.
- Reliability / Compliance:
  - View reports, analytics, inspection history; read‑only access to PMs.
- Admins:
  - Configure automation scripts, integration, and security groups.

---

## 4. Non‑Functional Requirements

- Performance: Inspection WO list retrieval within 3–5 seconds under typical load.
- Availability: Aligned with Maximo/MAS SLAs (e.g., 99.5%).
- Offline capability: Mobile client must work offline with full inspection functionality.
- Auditability: All changes to inspection results, status transitions, and follow‑up WOs must be auditable.