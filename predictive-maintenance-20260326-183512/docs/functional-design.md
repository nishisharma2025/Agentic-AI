# Functional Design : IBM Maximo Predictive Maintenance

## Scope
This design covers how users and system components work together to enable predictive-based PA and automated PM-work order handling in Maximo 8.x.

## User Roles
- Maintenance Manager
- Reliability Engineer/Data Scientist
- Operations Supervisor
- Technician/Mobile User
- IT/Integration Specialist

## Key Functions
### 1. Asset and PM Alignment
- Maintain clean mapping between arguments Assets, PM and WOs
- Ensure every PM is linked to a master ASSET and its relevant WOS.

### 2. Predictive Model Integration
- Maximo integrates with an external analytics platform (table model or ML/dIM)
- Data flows: IOT sensor + SCSA + Asset history = Predictive risk score
- Thresholds and model-score mapping to PM-actions:
  - Alert only
  - Alert + PM adjustment
  ...

### 3. Automated PM & WOGeneration
- Schedule batch job creates WO from PM when conditions are met
- Configurable rules to control how often and when pms should generate WO

### 4. Status & Notification
- Real-time status updates for PMs and WOs
- Event-driven alerts and exception handling (email/Mobile/SRSV)

### 5. Mobile Technician Support
- Technicians receive predictive WO assignments and log data
- Offline mode read/write for checklists and inspection results
