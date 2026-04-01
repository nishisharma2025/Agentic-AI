# Business Use Case: Preventive Maintenance with Inspection-Driven Corrective Work Orders

## 1. Background and Problem Statement

The company operates a portfolio of critical assets (e.g., production equipment, utilities, mobile assets) that require regular preventive maintenance (PM). Today, inspections are executed on paper or in simple forms, and any failures found during inspections are manually transcribed into corrective work orders in IBM Maximo.

This manual process causes:
- Delayed creation of corrective work orders.
- Inconsistent linkage between inspections and corrective work.
- Lost or incomplete inspection data.
- Limited ability to analyze failure trends and asset reliability.

The company wants a Maximo 8.x solution where:
- Preventive maintenance work orders include inspection tasks.
- Inspectors record inspection results directly in Maximo.
- Failed inspection points automatically trigger corrective work orders with correct priority, classification, and asset/location context.

## 2. Business Objectives

1. **Increase Asset Reliability**
   - Detect issues earlier through structured inspections.
   - Ensure all critical failures generate corrective work orders.

2. **Improve Maintenance Productivity**
   - Eliminate manual transcription from inspection sheets to work orders.
   - Reduce planning time for corrective work (auto-classification and auto-assignment where feasible).

3. **Improve Compliance and Safety**
   - Ensure mandatory inspections are executed and recorded.
   - Automatically generate corrective work orders for safety-critical defects.
   - Maintain auditable traceability from inspection to corrective action.

4. **Enhance Data Quality and Analytics**
   - Standardize inspection points, responses, and failure codes.
   - Enable reporting on inspection failures vs. completed corrective work.
   - Support reliability analysis (e.g., top recurring defects, MTBF/MTTR).

## 3. In-Scope

- IBM Maximo 8.x (Maximo Application Suite) configuration and light customization.
- PM records configured with inspection-type tasks or Inspection Forms.
- Work Order generation (PM -> PM WO -> Corrective WO).
- Workflow and automation scripting for:
  - Auto creation of corrective work orders based on inspection failures.
  - Validation of PM work orders before approval and completion.
- Role-based security and user experience for:
  - Inspectors
  - Planners
  - Supervisors
  - Reliability/Asset Engineers
- Reporting and KPIs:
  - Inspections resulting in corrective work.
  - Overdue PMs with open corrective work orders.
  - Top defects by asset, location, or failure class.

## 4. Out-of-Scope

- Complex predictive maintenance with IoT or condition monitoring systems (can be integrated later).
- ERP configuration for financials (only standard Maximo integration points considered).
- Non-Maximo mobile solutions (assuming Maximo Mobile or Maximo Everywhere / Work Centers).

## 5. Stakeholders and Personas

- **Maintenance Technicians / Inspectors**
  - Execute PM work orders and inspections on assets.
  - Record findings via Maximo UI or mobile.
- **Maintenance Planners**
  - Define PMs, frequencies, tasks, and inspection forms.
  - Review generated corrective work orders and plan resources.
- **Maintenance Supervisors**
  - Approve high-priority corrective work.
  - Monitor backlog and compliance to PM schedules.
- **Reliability/Asset Engineers**
  - Analyze inspection data and failures to improve PM strategies.
- **Operations / Production Managers**
  - Require asset uptime and visibility of risk.
- **IT / Maximo Support**
  - Maintain configurations, integrations, and security.

## 6. High-Level Requirements

1. **PM Configuration**
   - PM records tied to assets or locations.
   - Each PM can have an attached Inspection Form or Task List.
   - PMs generate PM WOs on calendar or meter-based triggers.

2. **Inspection Execution**
   - Inspection results captured directly on the PM WO (work order details or Inspection Results).
   - Structured answer types: pass/fail, numeric ranges, choice lists, text.
   - Mandatory inspection points for safety-critical tasks.

3. **Automatic Corrective WO Creation**
   - Business rules determine when a failure should generate a corrective WO:
     - Example: Any “Fail” answer on a safety-critical inspection point.
     - Numeric reading out of defined tolerance thresholds.
   - Corrective WO created as a follow-up or child of the PM WO, with:
     - Asset/location pre-populated.
     - Work type = CM (Corrective Maintenance).
     - Classification and failure codes derived from inspection point.
     - Priority based on severity mapping.

4. **Traceability**
   - Link between PM -> PM WO -> Corrective WOs.
   - Cross-reference between inspection point and corrective WO (e.g., via long description or custom fields).
   - View from asset history of both PM and corrective work.

5. **Workflow and Validation**
   - PM WO cannot be completed if:
     - Mandatory inspection points are not recorded.
     - Failed critical inspection points do not have a corresponding corrective WO created or explicitly justified.
   - Optional: Supervisor approval required for closing PM WO if open critical issues exist.

6. **Reporting / KPIs**
   - Percentage of PM WOs resulting in at least one corrective WO.
   - Count of overdue PMs and associated open corrective WOs.
   - Top 10 inspection failure modes by asset, system, or location.
   - Trend of corrective work generated from inspections over time.

## 7. Business Benefits

- **Reduction in Unplanned Downtime**
  - Early detection of issues via structured inspections and immediate corrective actions.
- **Improved Regulatory Compliance**
  - Full audit trail from inspection to corrective work.
- **Efficiency Gains**
  - Reduced manual data entry and fewer missed defects.
- **Better Decision Making**
  - Data-driven reliability insights from structured inspection data.

## 8. Risks and Assumptions

### Risks
- Inspectors bypassing the digital process (e.g., continuing to use paper).
- Poorly designed inspection forms leading to user frustration.
- Over-generation of low-value corrective WOs if rules are too aggressive.

### Assumptions
- Maximo 8.x environment available with standard Work Management and PM modules.
- Users have or will receive basic Maximo training.
- A change management plan will support adoption of digital inspections.

## 9. Success Criteria

- ≥ 90% of PMs executed with all required inspections recorded in Maximo.
- ≥ 95% of critical inspection failures automatically generating corrective WOs.
- ≥ 20% reduction in unplanned failures over 12–18 months on targeted asset classes.
- Positive end-user satisfaction feedback on inspection and corrective WO process.