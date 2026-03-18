def main():
    print('=== Current Inventory ===')

    sword = {
        "name": "sword",
        "type": "weapon",
        "quantity": 1,
        "value": 150
    }

    potion = {
        "name": "potion",
        "type": "consumable",
        "quantity": 5,
        "value": 10
    }

    armor = {
        "name": "armor",
        "type": "wearable",
        "quantity": 3,
        "value": 80
    }

    shield = {
        "name": "shield",
        "type": "equipable",
        "quantity": 2,
        "value": 30
    }

    helmet = {
        "name": "helmet",
        "type": "equipable",
        "quantity": 1,
        "value": 50
    }

    inventory = {
        "sword": sword,
        "potion": potion,
        "armor": armor,
        "shield": shield,
        "helmet": helmet
    }

    biggest = 0
    for name, item in inventory.items():
        print(f"Item: {name}")
        print(f" Type: {item['type']}")
        print(f" Quantity: {item['quantity']}")
        print(f" Value: {item['value']}\n")
        if biggest < item['quantity']:
            biggest = item['quantity']
    smallest = biggest
    for name, item in inventory.items():
        if smallest > item['quantity']:
            smallest = item['quantity']
    print(f"Kind of items in inventory: {len(inventory)}")
    print(f'The biggest amount of one item you have is {biggest}')
    print(f'The smallest amount of one item you have is {smallest}')

    abundance = {
        'low': [],
        'mid': [],
        'high': []
    }

    for name, item in inventory.items():
        if item["quantity"] >= 5:
            abundance["high"].append(name)
        elif item["quantity"] >= 2:
            abundance["mid"].append(name)
        elif item["quantity"] == 1:
            abundance["low"].append(name)
    print(f"\n{abundance}")


if __name__ == '__main__':
    main()
