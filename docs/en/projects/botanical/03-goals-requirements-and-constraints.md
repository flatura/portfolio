# Goals, Requirements, and Constraints

## Goals and Non-Goals

### Primary project goals

* Move living plant collection tracking from Excel, paper journals, and local databases into a unified web system.
* Ensure scientifically correct linkage of records to a global taxonomy source, cultivars, and grexes.
* Give botanical gardens, collectors, museums, and nurseries a tool for tracking specimens, locations, photos, statuses, accessions, and removals.
* Implement a GIS core: site map, areas, greenhouses, beds, plant points, and placement polygons.
* Simplify migration of existing data through Excel import, column mapping, name validation, and error reports.
* Create a public showcase for organizations: garden pages, public lists, plant cards, and QR labels.
* Support selective data disclosure.
* Build a network layer for the botanical community: exchange lists, wishlists, and automatic matching of desired taxa with available material.
* Give administrators and curators reporting on collection holdings, departments, taxa, accessions, and removals.
* Form a foundation for the long-term cultivar, registrar, and industry data standardization contour.
* Support generation of QR labels linking to a plant card in the system.

### Out of scope

* Not a replacement for BGCI as a global botanical garden directory and taxon-level data aggregator.
* Not a full-cycle herbarium system for herbarium collections or museum holdings.
* Not an ERP for commercial nurseries focused on sales, warehouse, procurement, production, POS, and accounting.
* Not a CRM, task tracker, document management system, or corporate portal.
* Does not include physical printing, production, installation, or maintenance of QR labels on site.
* Does not replace official ICRA/registrar legal cultivar registration; the system can only support a digital data and application contour.
* Does not guarantee automatic cleanup of all historical data without expert involvement: disputed names, synonyms, varieties, and errors require validation.
* Does not expose private collections by default; data publication remains an owner-controlled decision.
* Not a general-purpose BI/analytics platform; reporting is limited to living collections, accessions, and plant removals.
* Does not include a heavy enterprise contour at the first stage: billing, SLA, multi-region replication, public procurement, software registry, custom integrations, or separate installations per client.

## Requirements

## Business Requirements

- **BR-001. Centralize living plant collection tracking.**  
  The project must provide botanical organizations, collectors, and adjacent market participants with a unified web system to replace disconnected Excel files, paper journals, Word/PDF documents, and local databases.

- **BR-002. Improve scientific correctness of plant data.**  
  The project must ensure linkage of plant records to an authoritative taxonomic base, support the hierarchy family → genus → species, and a separate contour for cultivars and grexes.

- **BR-003. Reduce cost and complexity of migrating existing collection data.**  
  The project must allow import of historical data from Excel and other tabular sources with column mapping, value normalization, name validation, and error reports.

- **BR-004. Support operational tracking of plant specimens.**  
  The project must support plant instance cards with inventory numbers, statuses, provenance, acquisition form, placement location, photos, custom fields, and change history (full attribute list agreed separately).

- **BR-005. Link collection data to spatial context.**  
  The project must let organizations map territory, departments, areas, greenhouses, beds, and individual plants using points, polygons, and an interactive map.

- **BR-006. Give organizations a public digital showcase.**  
  The project must allow creation of public organization pages, public plant cards, public lists, and a collection map without building a separate website.

- **BR-007. Link physical plants to digital cards.**  
  The project must support generation of QR labels leading a visitor or staff member to a public or internal plant card.

- **BR-008. Support managed data disclosure.**  
  The project must let collection owners control data visibility: private, for registered users, for the community, or public.

- **BR-009. Create a network exchange layer between botanical community participants.**  
  The project must support collection lists, exchange lists, and wishlists so participants can match desired taxa with available material at other organizations, enabling exchange.

- **BR-010. Provide reporting for curators and administration.**  
  The project must provide reports on collection composition, taxa, departments, accessions, removals, lists, and collection holdings status.

... The public version includes a shortened requirements fragment. Full detail is not disclosed due to volume and product constraints.

## Rules and Constraints

### Business Rules

* **RULE-001. Organization data is closed by default.**  
  Collection data for a new organization is considered private until the owner explicitly changes the visibility level.

* **RULE-002. The data owner controls publicity.**  
  The organization independently determines which plants, lists, photos, coordinates, and pages are available publicly, to the community, or only to internal users.

* **RULE-003. A user cannot access another organization's data without permission.**  
  Access to plants, lists, places, photos, and import must be limited by the user's organization and assigned roles.

* **RULE-004. Species records must be linked to reference taxonomy.**  
  Users must not create arbitrary species records without a link to an authoritative taxonomic reference.

* **RULE-005. Local cultivars belong to the creating organization.**  
  A cultivar created within an organization is considered local and does not become globally available automatically (only through registration by an authorized registrar).

... The public version includes a shortened business rules fragment. Full detail is not disclosed due to volume and product constraints.

### Constraints

* **CON-001. The system must be a web/SaaS solution.**  
  The product is designed as a web platform with centralized access, not as a desktop application.

* **CON-004. Excel must be supported as the primary migration format.**  
  The system must account for the fact that source data for the target audience is most often in Excel files.

* **CON-005. Source data may be dirty and heterogeneous.**  
  Import must account for typos, synonyms, local names, incomplete values, non-standard columns, and historical tracking formats.

* **CON-006. GIS accuracy is limited by source data quality.**  
  The system can store and display points and polygons, but actual accuracy depends on user actions and field data quality.

... The public version includes a shortened constraints fragment. Full detail is not disclosed due to volume and product constraints.
