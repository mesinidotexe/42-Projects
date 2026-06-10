import random


class Player:
    def __init__(self, name, achievements):
        self.name = name
        self.achievements = set(achievements)


def gen_player_achievements():
    all_achievements = [
        "first_kill", "level_10", "treasure_hunter", "speed_demon",
        "boss_slayer", "collector", "perfectionist", "explorer",
        "master_miner", "puzzle_solver"
    ]

    num = random.randint(1, len(all_achievements))
    return set(random.sample(all_achievements, num))


def main():
    print('=== Achievement Tracker System ===')

    players = [
        Player("alice", gen_player_achievements()),
        Player("bob", gen_player_achievements()),
        Player("charlie", gen_player_achievements()),
        Player("david", gen_player_achievements())
    ]

    for player in players:
        print(f'Player {player.name}: {player.achievements}')
    print()

    print('=== Achievement Analytics ===')

    all_achievements = set()
    for player in players:
        all_achievements = all_achievements.union(player.achievements)

    print('All unique achievements:', all_achievements)
    print('Total:', len(all_achievements))
    print()

    common = players[0].achievements
    for player in players[1:]:
        common = common.intersection(player.achievements)

    print('Common to all players:', common)
    print()

    for player in players:
        others = set()

        for p in players:
            if p != player:
                others = others.union(p.achievements)

        unique = player.achievements.difference(others)
        missing = all_achievements.difference(player.achievements)

        print(f'--- {player.name} ---')
        print('Unique achievements:', unique)
        print('Missing achievements:', missing)
        print()


if __name__ == '__main__':
    main()
