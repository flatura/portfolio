# Модель системы

## Доменная модель

В основе решения лежала простая, но прикладная доменная модель:

* расходный материал;
* тип расходника;
* модель оборудования;
* совместимость расходника и оборудования;
* складской остаток;
* поступление;
* выдача;
* списание;
* подразделение или место использования;
* история движения;
* плановая потребность;
* закупочная заявка или закупочная потребность.

## Модель данных

## Диаграмма классов

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

## API-контракты
