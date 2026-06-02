# Technical Design: Maximo Spatial GIS Integration

## 1. Architecture overview
The solution architecture includes Maximo 8.x application servers, with Maximo Spatial add-on, Maximo Integration Framework (MIF) and IBA connectors in the middle layer, exposing secure WEB, API gateway as an Integration Bus (IBA) or ESB.

ArcGJS server and geodatabase provide map services and data services. Maximo Spatial uses these services to render maps, update geometrids and perform giocode searches.

## 2. Integration patterns

- Rest AP APIs (Maximo MIE Endpoints, ESRI REST API)
- Message-driven integration (Zule, MQW, Kafda)
- FTPS and RHEST calls for ArcGIS services.

## 3. Data mapping
### 3.1 Asset and Locations
ASSETNUM enforces spanning tree data from Gio, relying on mapping configurations in Maximo Spatial.
Global waypoints are stored in ESRI geodatabase and custom classes that map to ASSETPLOC, LOCATION fields are implemented.

### 3.2 Work orders
WORKORDER: has additional geofile fields and polygon geometric sett maps. Maximo Spatial manages display by physical application and work order manngling.

## 4. Security
OAuth 2.0 is used for Maximo applications with role-based access to spatial data. Federated KS2.Ne for ESRI API's. Back end every source has a control on the access to map layers and data.

## 5. Security Pattern
GAsFirewall, MTLS pseudope and  etc.