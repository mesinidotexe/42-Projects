import sys


def main():
    print('=== Current Inventory ===')

    inventory = {}

    # 🔹 Parsing dos argumentos
    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f'Invalid parameter: {arg}')
            continue

        parts = arg.split(':')

        if len(parts) != 2:
            print(f'Invalid parameter: {arg}')
            continue

        name = parts[0]

        try:
            quantity = int(parts[1])
        except ValueError:
            print(f'Invalid quantity: {arg}')
            continue

        if name in inventory:
            print(f'Duplicate item: {name}')
            continue

        inventory[name] = quantity

    # 🔹 Mostrar inventário
    print('Inventory:', inventory)

    # 🔹 Lista de itens
    items = list(inventory.keys())
    print('Items:', items)

    # 🔹 Total de quantidade
    total = sum(inventory.values())
    print('Total quantity:', total)

    # 🔹 Percentagem de cada item
    print('\nPercentages:')
    for name, qty in inventory.items():
        percent = (qty / total) * 100 if total > 0 else 0
        print(f'{name}: {round(percent, 2)}%')

    # 🔹 Mais e menos abundante (respeitando ordem)
    max_item = None
    min_item = None

    for name in inventory:
        if max_item is None or inventory[name] > inventory[max_item]:
            max_item = name
        if min_item is None or inventory[name] < inventory[min_item]:
            min_item = name

    print('\nMost abundant:', max_item)
    print('Least abundant:', min_item)

    # 🔹 Adicionar novo item
    new_item = "gold"
    new_quantity = 10

    inventory[new_item] = new_quantity

    print('\nUpdated inventory:', inventory)


if __name__ == '__main__':
    main()