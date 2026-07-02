# System Model

## Domain Model

The solution was based on a simple but practical domain model:

* consumable item;
* consumable type;
* equipment model;
* compatibility between consumables and equipment;
* stock balance;
* receipt;
* issue;
* write-off;
* department or place of use;
* movement history;
* planned demand;
* purchase request or procurement need.

## Data Model

## Class Diagram

```mermaid
classDiagram
    class ConsumableItem {
      id
      name
      sku
      type_id
    }

    class ConsumableType {
      id
      name
    }

    class EquipmentModel {
      id
      vendor
      model
    }

    class StockMovement {
      id
      type
      quantity
      date
      item_id
      consumer_id
      comment
    }

    class Department {
      id
      name
    }

    class Place {
      id
      name
      department_id
    }

    class ConsumerEquipment {
      id
      name
      place_id
      model_id
    }

    ConsumableItem --> ConsumableType
    ConsumableType --> EquipmentModel
    StockMovement --> ConsumableItem
    StockMovement --> ConsumerEquipment
    ConsumerEquipment --> Place
    Place --> Department
```

## API Contracts
