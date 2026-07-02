# Architecture and Integrations

## Architecture

### Container diagram

```mermaid
    C4Container
    title Container Diagram for Botanical SaaS MVP

    Person(user, "User")

    System_Boundary(sys, "system") {
      Container(spa, "Single Page Application", "Angular 21, Open Layers", "User-side UI") 
      Container(static, "Frontend Static", "nginx", "Static data storage container.")
      Container(backend, "Backend Business Logic", "Spring Boot", "Business logic.")
      ContainerDb(reldb, "Relational DB", "PostgreSQL + PostGIS", "Plant instances, lists,<br/> users, RBAC roles.")
      ContainerDb(objStore, "Object Storage", "MinIO", "Photos and multimedia.<br/> collection import files.")
    }

    Boundary(ext, "External systems", "") {
      Container_Ext(powo, "POWO", "Plants of the World Online (Kew).<br/> Taxon reference.")
      Container_Ext(vernacular, "WikiData", "National names reference<br/> (vernacular names).")
      Container_Ext(llm, "LLM", "Suggestions")
    }

  Rel(user, spa, "Uses to<br/> manage plant collections")

  Rel(spa, static, "Gets Angular <br/> static UI bundles", "HTTPS")
  Rel(spa, backend, "Sends API-calls", "HTTPS REST")

  Rel(backend, reldb, "Reads/writes data", "SQL")
  Rel(backend, objStore, "Loads/reads media", "S3 API")

  Rel(backend, powo, "Calls taxons/cultivars,<br/> writes cultivars", "HTTPS/REST")
  Rel(backend, vernacular, "Gets species names<br/> on national language", "HTTPS/REST")
  Rel(backend, llm, "Uses LLM-API<br/> to get species name suggestions", "HTTPS/OpenAI API compatible")

  UpdateLayoutConfig($c4ShapeInRow="5", $c4BoundaryInRow="3")

```
## Integration Flows

### Smart Import

The platform includes a guided spreadsheet import pipeline for existing plant collections.

The import flow supports file upload, sheet selection, column mapping, value resolution, fuzzy matching, asynchronous processing, row-level results, and error report export.
