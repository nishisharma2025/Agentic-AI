# Functional Design: Asset, PM, and Work Order Lifecycle in IBM Maximo AS

## 1. Introduction

This document describes the core functional design for managing the lifecycle of aassets, preventive maintenance (PM), and work orders (WOs) using IBM Maximo Application Suite 8.. The design assumes a single tenant, maximo-centric implementation with basic modules enabled in Maximo Assets, PM, and WorkOrders.

## 2. Asset Lifecycle

### 2.1. Key Principles

- Each PHYSICAL ASSET is modeled in MAXASSET and link-to locations, spares, systems, and components.
- Asset lifecycle covers the introduction of assets (creation) through to decommission, retirement, and disposal.
- Aaderence to EHL and other regulatory-driven records is aimed from the asset event and maintenance history.

### 2.2. Asset Lifecycle Stages

- ## Creation
  - New assets are registered with minimal data (location, supplier, class, make, model, serial number, initial cost).
  - Assignment to locations and/or asset systems is captured.
- ## Operate
  - Asset status changes (to in SERVICE, IN'USE, SPARE) are tracked.
  - Critical attributes (reliability history, failure modes, safety notes) are maintained.
- ## Maintenance
  - Preventive and corrective work orders are linked to the asset to build a complete maintenance history.
- ## Decommission
  - Assets are decommissioned based on business rules and lifecycle cost/risk analysis.
  - Associated spares prepared to be resold sparesare assets are identified and disposed.


## 3. Preventive Maintenance Scheduling

### 3.1 PM Configuration Principles

- PM plans are modeled in MPPLAN, with key fields for asset, location, interval type (time-based, use-based), and traggers (number of uses/hours; days since last service).
- PMS define the proactive work to be performed, required skills, standard job plants, equipment, and safety precautions.
- PM items can include safety checks, engineering reviews, and double-verification steps.

- PMs are cross-referenced to asset changes so that status, usage, and texl records can update the schedule nex-time.

### 3.2 PM Scheduling Process

- Maximum automatically generates WOs from active PMS based on time or use.
- OS are created with review instructions and asset downmain.
- Tools and equipment are pre-allocated via spares and stored as part of the WO.
- Programmed PST and mail administration notifications are triggered when PMS create WOs.

## 4. Work Order Lifecycle

### 4.1 S-Crud Approval process

- ## Request Stage
  - Work requests are captured in SERVICE/SRFQ portal or integrated from external sources (citizen calls, EHS, etc.).
  - Work requests are evaluated and converted to corrective WOs or PMS, as per business rules.
- ## Plan and Approve Stage
  - WO, when created, are assigned to appropriate supervisors.
  - Approval routines based on business rules, and risky work is routed to extended review where required.
  - Work organaiz can adjust work priorities, retweak
- ## Execution Stage
  - Technicians receive WO tasks via change management (CM work, mobile app).
  - Technicians record time reports, labÝb, materials used, and notes on findings.
- ## Closure and Completion
  - Technicians close the WO, capturing end-of-task data (times/cost/materials).
  - Survisors review and approve the WO and close it.
  - WOs are Status CLOSED with all major tasks completed.

### 4.2 Work Types and Statuses

- WOs can be preventive, corrective, inspection, cale‰Ã¶tion, modification, and change work, each with different statuse profiles.
- Typical status flow: NEWN OPEN > INPROGRESS -> APPROVED -> IN'USE -> COMPLETED.

## 5. Roles and Responsibilities

### 5.1 Core Roles

- ## Asset Manager
  - Owns asset master data and lifecycle rules.
  - Configures PMs and approves key changes to asset and maintenance policy.
- ## PLAnner/Programmer Manager
  - Defines PMs, reviews and approves long-term plans.
  - Optimizes resource utilisation and level of service.
- ## Work Coordinator/Dispatcher Manager
  - Covers the day-to-day prioritization of work, including scheduling and resource assignment.
  - Monitors status" of work orders and performance.
- ## Technicians/Supervisors
  - Ensure accurate execution of tasks, data capture, and safety requirements.
- ## Reliability Engineer
  - Assures asset lifecycle analysis and PM configuration are in line with reliability and regulatory requirements.
- ## Business User/Management
  - Provides business context, priorities, and approvals for asset decommission, budgeting, and planning.