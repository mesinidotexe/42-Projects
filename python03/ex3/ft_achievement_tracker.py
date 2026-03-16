class Player:
    def __init__(self, name, achievements):
        self.name = name
        self.achievements = set(achievements)
        

def main():
    print('=== Achievement Tracker System ===')

    alice = Player("alice", [
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    ])
    
    bob = Player("bob", [
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    ])

    charlie = Player("charlie", [
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    ])

    players = [alice, bob, charlie]
    for player in players:
        print(f'Player {player.name} achievements: {player.achievements}')
    print()
    print('=== Achievement Analytics ===')
    achievements = alice.achievements.union(bob.achievements)
    achievements = achievements.union(charlie.achievements)

    print('All unique achievements')
    for ach in achievements:
        print(f'-{ach}')
    print(f'Total achievements: {len(achievements)}\n')
    
    common = alice.achievements.intersection(bob.achievements)
    common = common.intersection(charlie.achievements)
    print(f'Common to all players: {common}')

    shared_pairs = (
        alice.achievements.intersection(bob.achievements)
        .union(alice.achievements.intersection(charlie.achievements))
        .union(bob.achievements.intersection(charlie.achievements))
    )
    rare = achievements.difference(shared_pairs)
    print(f'Rare aachievement (1 player): {rare}')

    alice_bob = alice.achievements.intersection(bob.achievements)
    print(f'alice vs bob common: {alice_bob}')
    alice_unique = alice.achievements.difference(bob.achievements)
    print(f'alice unique: {alice_unique}')
    bob_unique = bob.achievements.difference(alice.achievements)
    print(f'Bob unique: {bob_unique}')


if __name__ == '__main__':
    main()