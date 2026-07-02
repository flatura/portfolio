## Модель данных

### High-Level Data Model

```mermaid
erDiagram
    ORGANIZATION ||--o{ ORG_UNIT : contains
    ORGANIZATION ||--o{ PLANT_INSTANCE : owns
    ORGANIZATION ||--o{ PLACE : manages
    ORGANIZATION ||--o{ PLANT_LIST : maintains
    ORGANIZATION ||--o{ PUBLIC_PAGE : publishes

    ORG_UNIT ||--o{ PLANT_INSTANCE : curates
    PLACE ||--o{ PLACE : contains
    PLACE ||--o{ PLANT_INSTANCE : locates

    PLANT_INSTANCE }o--|| SYSTEM_TAXON : "required taxon_id"
    PLANT_INSTANCE ||--o{ PHOTO : documents
    PLANT_INSTANCE }o--o{ PLANT_LIST : included_in

    SYSTEM_TAXON ||--o| POWO_TAXON : "species subtype"
    SYSTEM_TAXON ||--o| CULTIVATED_ENTITY : "cultivar/grex subtype"

    PUBLIC_PAGE ||--o{ PLANT_LIST : exposes
    PUBLIC_PAGE ||--o{ PLANT_INSTANCE : exposes_selected

    ORGANIZATION {
        uuid id PK
        string public_name
        string slug
        string visibility
    }

    ORG_UNIT {
        uuid id PK
        uuid organization_id FK
        uuid parent_id FK
        string name
    }

    PLANT_INSTANCE {
        uuid id PK
        uuid organization_id FK
        uuid org_unit_id FK
        uuid place_id FK
        uuid taxon_id FK "mandatory"
        string accession_number
        string individual_code
        string status
        string provenance_type
        geometry point
        jsonb custom_fields
    }

    SYSTEM_TAXON {
        uuid id PK
        string display_name
        string normalized_name
        string taxon_type
        string rank
    }

    POWO_TAXON {
        uuid id PK
        uuid system_taxon_id FK
        string powo_id
        string ipni_id
        string family
        string genus
        string species_epithet
        string scientific_name
    }

    CULTIVATED_ENTITY {
        uuid id PK
        uuid system_taxon_id FK
        string genus
        string cultivar_or_grex_name
        string breeder_name
        string registrar_name
        int registration_year
        string visibility_scope
    }

    PLACE {
        uuid id PK
        uuid organization_id FK
        uuid parent_id FK
        string name
        geometry point
        geometry polygon
    }

    PLANT_LIST {
        uuid id PK
        uuid organization_id FK
        string name
        string list_type
        string visibility
    }

    PHOTO {
        uuid id PK
        uuid plant_instance_id FK
        string caption
        string photo_tag
        boolean publication_allowed
    }

    PUBLIC_PAGE {
        uuid id PK
        uuid organization_id FK
        string slug
        boolean visible
    }
```

### Ключевая идея модели

Центральная сущность системы - **PlantInstance**, цифровой двойник конкретного растения в живой коллекции. Это не просто строка справочника и не абстрактный вид, а учётная запись конкретного экземпляра: с инвентарным номером, статусом, местом размещения, принадлежностью к организации, фотографиями, списками и публичным представлением.

Обязательный атрибут **`taxon_id`** является ядром модели. Он связывает каждый экземпляр растения с единой корневой сущностью **SystemTaxon**. Благодаря этому все операционные сценарии - учёт, импорт, поиск, списки, обмен, QR-страницы, отчётность и публичная карта -работают не с произвольным текстовым названием растения, а с устойчивым идентификатором таксона.

**SystemTaxon** выступает общей корневой сущностью для двух крупных таксономических контуров:

* **PowoTaxon** - видовые таксоны, поступающие из авторитетного каталога POWO/IPNI.
* **CultivatedEntity** - культивары и грексы, которые могут быть признанными глобальными записями, поступающими от регистраторов, либо локальными записями, созданными внутри конкретной организации.

Такой подход позволяет пользователю выбирать растение из единого taxon lookup, не разделяя искусственно поиск по видам и поиск по культиварам. Для пользователя это выглядит как единый справочник растений, а внутри системы сохраняется различие между научными видовыми таксонами, глобальными культиварами, грексами и локальными культиварами организации.

Архитектурная ценность решения состоит в том, что все коллекционные данные становятся сопоставимыми между организациями. Один и тот же `taxon_id` может использоваться в карточках растений, списках коллекций, wishlists, списках обмена, публичных страницах и отчётах. Это создаёт основу для сетевых сценариев: система может сопоставлять, какие таксоны одна организация ищет, а другая готова передать, не полагаясь на нестабильные текстовые названия, синонимы, локальные варианты и опечатки.

В портфолио модель показана верхнеуровнево. Внутренние вспомогательные сущности, механизмы разграничения видимости, таблицы доступа, workflow глобализации культиваров и технические детали реализации намеренно опущены.
