# Technical Design

## Maximo Object Relations

- ASSET_TEMPLE – Asset information.
- PM– Preventive maintenance schedule.
- WORKORDERO Т Work order for maintenance.

## Asset → PM – Work Order Flow

- Asset: ASSET_TEMPLE -- PM -- WORKORDERO.
- PM triggers: Time-based and event-based schedules.
- Work Orders: Generated from QM (Pm) or manually created.

## Integration Architecture

- REST APIs: Used for external integrations.
- ERS bus: Manages message flow to and from Maximo.
- ERP: Syncs master data with 'BRUCU' and 'FINANCE' asets.
- Iot Sensors: Capture status and inspection data.

## Automation Scripts

- PM To WOR: Validates asset association and logs generated work orders.
here goes JYTHON script.

## Deployment Considerations

- Maximo Application Suite 8.x.<br/>- Kubernetes buster for scalability.
- Application Pods: Serfless and WEBAP; scale as deployment grows.
- Database: Managed separately with backup and recovery plans.
