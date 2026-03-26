# Technical Design: Preventive Maintenance with Inspection-Driven Corrective Work Orders

## 1. Architecture Overview

The solution runs on IBM Maximo Application Suite (MAS) 8.x with the following components:

- **Maximo Application Server** (clustered WebSphere Liberty / OpenShift pods).
- **Database**: Db2 / Oracle / SQL Server (per environment).
- **Maximo Inspections** configured and integrated with Work Orders.
- **Integration Services**:
  - ERP for costs, GL, and purchasing (optional).
  - Email/notification service for alerts.

### Logical Architecture

- Users → Maximo UI (desktop, Work Centers, or Maximo Mobile).
- Maximo UI → Maximo APIs and business logic.
- PM Engine (cron task) → generates PM WOs.
- Automation scripts (Jython) →:
  - Validate PM WOs on status change.
  - Create corrective WOs on inspection failures.
- Workflow Engine → controls WO lifecycle.
- Database → stores assets, PMs, inspection results, and WOs.

## 2. Data Model

### 2.1 Core Tables

- **ASSET**
  - KEY: ASSETNUM, SITEID
  - Attributes: CLASSSTRUCTUREID, CRITICITY, STATUS, LOCATION.

- **LOCATIONS**
  - KEY: LOCATION, SITEID
  - Attributes: TYPE, PARENT, DESCRIPTION.

- **PM**
  - KEY: PMNUM, ORGID, SITEID
  - Attributes: ASSETNUM/LOCATION, FREQUENCY, PMSTATUS, JOBPLAN, INSPECTIONFORMID (if using Inspections).

- **JOBPLAN / JOBTASK**
  - Defines tasks and labor/material requirements.

- **WORKORDER**
  - KEY: WONUM, SITEID
  - Fields used:
    - WOTYPE (PM, CM).
    - ORIGRECORDCLASS, ORIGRECORDID (link back to PM WO).
    - PARENT (to build hierarchy PM WO -> Corrective WO).
    - ASSETNUM, LOCATION.
    - CLASSSTRUCTUREID, FAILURECODE.
    - STATUS, REPORTDATE, TARGETSTART/FINISH.
    - Custom fields (optional): INSPECTIONREF, SEVERITYLEVEL.

- **INSPFORM / INSPQUESTION / INSPRESULT** (naming may vary)
  - Inspection form, questions, and recorded answers.
  - Link to work order via WORKORDERID/WONUM or equivalent.

- **Domains / Cross-Reference Tables**
  - To map inspection question IDs to:
    - Severity.
    - Failure class.
    - Default WO classification and priority.

Example custom cross-reference table (if using Database Configuration):

- **INSPECTION_RULES**
  - INSPQUESTIONID (or label key).
  - SEVERITYLEVEL (1-4).
  - FAILURECLASSID.
  - DEFAULTPRIORITY.
  - AUTOCREATEWO (Y/N).

## 3. Integration Points

### 3.1 ERP Integration (Optional)

- Outbound interface for:
  - Actuals (labor, materials) on corrective WOs.
- Inbound interface for:
  - GL accounts.
  - Cost centers.
  - Asset master alignment (if not mastered in Maximo).

Integration typically via:
- REST/JSON or JMS.
- Maximo Integration Framework (MIF).

### 3.2 Notification Services

- Email notification on:
  - High-severity corrective WO creation.
  - PM completion with unresolved issues (if allowed).
- Implement using:
  - Communication templates.
  - Escalations or workflow notifications.

## 4. Automation Scripts

### 4.1 Trigger Points

1. **Inspection Results Save**
   - Object: INSPRESULT or related MBO.
   - Event: Save / Add / Update.
   - Action: Evaluate failure criteria and create corrective WO(s).

2. **Work Order Status Change**
   - Object: WORKORDER.
   - Event: Before save when STATUS is set to COMP.
   - Action:
     - Validate mandatory inspection questions answered.
     - Confirm corrective WOs exist for critical failures or justification is provided.

### 4.2 Script Implementation Approach

- Use **Jython Automation Scripts** attached to:
  - Object Launch Points (WORKORDER, INSPRESULT).
  - Optional: Attribute and action launch points for finer control.

- Reusable utility script functions:
  - `getInspectionResultsForWO(wonum, siteid)`
  - `evaluateInspectionResults(results)`
  - `createCorrectiveWO(pmwo, result, rule)`

### 4.3 Data Access Pattern

- Use Maximo MBO APIs:
  - `MXServer.getMXServer().getMboSet()`.
  - `mbo.getString()`, `mbo.setValue()`.
  - `MboSet.save()` or rely on transaction context.

- Ensure:
  - Transaction integrity: scripts run within the same transaction as WO status change.
  - Error handling: descriptive messages via `service.error()` or `service.log()`.

## 5. Workflow Design

### 5.1 Work Order Lifecycle Workflow

- **Start → WAPPR → APPR → INPRG → COMP → END**
  - Additional statuses:
    - CAN (Cancelled).
    - HOLD (On Hold).
- Workflow logic:
  - On approval (APPR), PM WOs can be assigned to technicians.
  - On transition to COMP:
    - Call automation script to validate inspection completeness and corrective WO coverage.
  - If validation fails:
    - Workflow returns WO to INPRG or routes to a **Supervisor Approval Node**.
  - Supervisor may:
    - Approve closure with justification.
    - Request new corrective WO or additional inspections.

### 5.2 Workflow Implementation

- Use out-of-box Workflow Designer.
- Add:
  - Condition Nodes to evaluate automation script results (or custom field flags).
  - Manual Input Nodes for Supervisor comments.
  - Action Nodes to:
    - Change status.
    - Send notifications.

## 6. Performance and Scalability

- Design considerations:
  - Scripts must be efficient and avoid large full-table scans.
  - Use targeted queries (e.g., by WONUM and SITEID).
  - Limit number of corrective WOs per inspection failure (configurable).

- Recommended:
  - Testing on realistic data sets.
  - Indexing on:
    - INSPRESULT.WONUM, SITEID.
    - CUSTOM cross-reference table keys (INSPQUESTIONID).

## 7. Security and Access (Technical)

- Use Security Groups:
  - INSPECTOR_GROUP: permission to update WO and inspection data, no access to PM setup.
  - PLANNER_GROUP: PM, Job Plan, Inspection Form configuration rights.
  - SUPERVISOR_GROUP: WO approval, override capabilities.

- Object restrictions to:
  - Prevent deletion of inspection results once approved.
  - Restrict update of system-generated corrective WO links.

## 8. Deployment and Configuration Steps

1. **Configure Domains and Cross-Reference Table**
   - Create `INSPECTION_RULES` object/table via Database Configuration.
   - Define domain lists for:
     - Severity.
     - Yes/No answers.
     - Inspection result codes.

2. **Create Inspection Forms**
   - Define Inspection Forms for each major asset type.
   - Tag questions with unique IDs or field names used in rules.

3. **Configure PMs and Job Plans**
   - Link appropriate Inspection Forms to PMs.
   - Associate Job Plans where needed for additional tasks.

4. **Create Automation Scripts**
   - Implement:
     - Inspection evaluation and corrective WO creation.
     - PM WO validation script (see separate script file).
   - Deploy scripts to dev → test → prod with version control.

5. **Configure Workflow**
   - Apply WO Workflow to relevant WOTYPEs (PM, CM).
   - Test status transitions and escalations.

6. **Reporting**
   - Create BIRT/Report Builder or Cognos reports for KPIs.

## 9. Error Handling and Logging

- Use `service.log()` to log informational messages and debugging info.
- Use `service.error()` with:
  - Error group (e.g., `pmvalidate`).
  - Error key (e.g., `INSPECTION_MISSING`, `CRIT_FAIL_NO_CORR_WO`).
- Configure message lookups in Maximo Messages.

## 10. Extensibility

- Future enhancements:
  - Integration with condition monitoring (IoT) to trigger PM or corrective WOs directly.
  - Integration with predictive analytics to optimize PM intervals.
  - Use of Maximo Health and Predict for asset reliability insights.