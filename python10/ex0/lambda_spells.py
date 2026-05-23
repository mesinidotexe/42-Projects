def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    rsorted = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return rsorted


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = filter(lambda x: x['power'] >= min_power, mages)
    return list(filtered)


def spell_transformer(spells: list[str]) -> list[str]:
    mapped = map(lambda x: '* ' + x + ' *', spells)
    return list(mapped)


def mage_stats(mages: list[dict]) -> dict:
    _max = max(mages, key=lambda x: x['power'])
    _min = min(mages, key=lambda x: x['power'])
    try:
        average = round(sum(mage['power'] for mage in mages) / len(mages), 2)
    except ZeroDivisionError:
        print('Mage list cannot be empty', ZeroDivisionError)
        quit()
    return {'max_power': _max, 'min_power': _min, 'avg_power': average}


def main():
    artifacts = [{'name': 'Fire Staff', 'power': 114, 'type': 'armor'},
                 {'name': 'Water Chalice', 'power': 113, 'type': 'focus'},
                 {'name': 'Crystal Orb', 'power': 95, 'type': 'weapon'},
                 {'name': 'Light Prism', 'power': 63, 'type': 'relic'}]

    mages = [{'name': 'Sage', 'power': 78, 'element': 'light'},
             {'name': 'Riley', 'power': 66, 'element': 'fire'},
             {'name': 'Nova', 'power': 61, 'element': 'shadow'},
             {'name': 'Ash', 'power': 75, 'element': 'shadow'},
             {'name': 'Ember', 'power': 59, 'element': 'lightning'}]

    spells = ['flash', 'tsunami', 'freeze', 'darkness']

    print('Testing artifact sorter...')
    _sorted = artifact_sorter(artifacts)
    for mage in _sorted:
        print(mage.values())
    print()

    print('Testing power filter...')
    filtered = power_filter(artifacts, 100)
    for item in filtered:
        print(item.values())
    print()


    print('Testing Mage stats')
    stats = mage_stats(mages)
    print(stats)
    print()


    print('Testing Spell Transformer...')
    transformed = spell_transformer(spells)
    print(transformed)


if __name__ == '__main__':
    main()
