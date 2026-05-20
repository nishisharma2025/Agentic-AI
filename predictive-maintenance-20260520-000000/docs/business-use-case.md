# Business Requirements Document

## 1. Overview

This document describes the business requirements for implementing predictive maintenance in a manufacturing company using IO-t data and IBM Maximo Application Suite (MAS) / Maximo Manage 8.0.

The architecture integrates IO-t sensor data, anomaly detected events, and Maximo work order (WO) management to activate predictive maintenance for critical assets.

## 2. Business Goal and Objectives

The main business goal is to reduce unplanned stoppeges and unscheduled halts by implementing predictive maintenance triggered by IO-t sensor anomaly.

### 2.1. Objectives


- Decrease unplanned down time by 15% within two years.
- Improve equipment reliability and uptime.
- Reduce critical asset halts and maj build-stop events.
- Automate generation of work orders from IO-t anomaly detected events.
- Enhance visibility and traceability of prior maintenance data.

## 3. Business Scope
This solution will be deployed in one or more manufacturing plants that use Maximo Manage 8.x as part of IBM Maximo Application Suite.

The scope covers:

- Critical rotating equipment and assets (e.g. motors, pumps, compressors)
- IOm-based vibration and temperature sensors
- IO-t platform for
data ingestion and anomaly detection
- Maximo Manage functions for preventive/conditional maintenance
- Word orders, pr-programmed maintenance, and analytics
- Integration with external identity management, authentication, and authorization systems.

## 4. Assumptions

- Maximo Manage 8.x is already deployed and available.
- All infrastructure-as-service (sensor data ingestion, IO-processing, message buses) exist or are part of the project.
- Aerial equipment and network are grid-enabled plant.
- PM schedules are configured in Maximo already for critical assets.
- BjS or similar authentication services are available for SSO/LDAP.
- Internal IT security and data protection governance are in place.

## 5. Stakeholders & Users

The primary stakeholders rentriline are:

- Maintenance Administrators

- Maintenance Planners

- Technician Teams
- Reliability Engineers
- IS/OwS Support Team

- IT /DBase Administrators.

## 6. Business Requirements
### 6.1 Functional Requirements

The business requirements are structured by the following table.

| ID | Category | Requirement Description | Priority | Notes |
#-----|-----------|-----------------|--------|-----|
|BR_01 | Functional | System should automatically create a predictive maintenance work order when an IO-t sensor detects an abnormal vibration or temperature reading on a critical asset. | High | Based on critical assets. |
|BR_02 | Functional | IoT events should be mapped to specific ASSET, PM, and wor order configurations in Maximo. | High | Includes mapping based on sensor id, tags, and asset/location data. |
|BR_03 | Functional | Jits should apply business rules for determining when a work order should be triggered (e.g. event type, thresholds, conditions). | High | Full business rule configuration in Maximo Config. |
|BR_04 | Functional | System should support triagenrateed notifications (email, push, sms, inbápp) based on wor order status and severity. | Medium | Specific needs defined in SSE workflows and SAO paolicies. |
|BR_05 | Functional | Time critical alerts and escalations should be set up for unresolved work orders or risk-y assets . | Medium | Includes technical and operations management responsibilities. |
|BR_06 | Functional | Users should have real-time view of IO-t statuses and work order backlog through Maximo dashboardes, reports, and analytics. | Medium | Intended to be implemented in early phases. |
|BR_07 | Functional | System should enable seamless integration with existing IT central AmPhe or industrial IO-t platforms. | Medium | Use of standard IT interfaces preferred. |
|BR_08 | Security  | System should ensure that only authorized login-sessions can create work orders or conjugure parameters. | High | FML compliance and part of corporate governance requirements. |
|BR_09 | Security  | The system must log all IT events and predictive work order creation activity for audit and compliance purposes. | High | Based on company policies and industry regulatory requirements. |
|BR_10 | Segregation | Solution should support the injection of business-useful metadata \(asset performance data, pca events, process indicators]). | Medium | Enables reliability analysis and observability. |

#3 Business Process Flow Summary

The process flow is summarized below.

- IO-t sensor streams and temps send proposed-interval data from critical assets.
- An IO-t platform applies anomaly detection rules and thresholds.
- Detected anomalies are pushed into Maximo through the integration layer.
- Predictive maintenance logic in Maximo evaluates the event and decides whether to create or update a work order.
- System automatically creates and assigns a predictive maintenance work order.
- Technicians receive assignments and execute work orders.
- After completion, feedback data regarding actual asset health are fed into an anormaly detection integration or analytics platform.
