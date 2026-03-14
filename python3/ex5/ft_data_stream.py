class Player():
    def __init__(self, name, level, action):
        self.name = name
        self.level = level
        self.action = action

    def __str__(self):
        return f"Player {self.name} (level {self.level}) {self.action}"


def create_player(events):
    for i in range(events):
        if i % 3 == 0:
            yield Player("alice", 5, "killed monster")
        elif i % 3 == 1:
            yield Player("bob", 12, "found treasure")
        else:
            yield Player("charlie", 8, "leveled up")
        if i == 2:
            print('...\n')


def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        temp = a + b
        a = b
        b = temp
    

def prime_num(n):
    counter = 0
    prime = 2

    while counter < n:
        divisor = 2
        is_prime = True

        while divisor <= prime / 2:
            if prime % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            yield prime
            counter += 1
            
        prime += 1


def main():
    print('=== Game Data Stream Processor ===')

    total_events = 1000
    print(f'Processing {total_events} game events...')
    print()

    event_number = 1
    high_level = 0
    treasure_events = 0
    level_up = 0
    for player in create_player(total_events):
        if event_number < 4:
            print(f"Event {event_number}: {player}")
            event_number += 1
        if player.level >= 10:
            high_level += 1
        if player.action == 'found treasure':
            treasure_events += 1
        elif player.action == 'leveled up':
            level_up += 1


    print ('=== Stream Analytics ===')
    print(f'Total events processed: {total_events}')
    print(f'High-level players (10+): {high_level}')
    print(f'Treasure events: {treasure_events}')
    print(f'Level-up events: {level_up}')
    print('\n=== Generator Demonstration ===')
    print(f'Fibonacci sequence (first 10): {list(fibonacci(10))}')
    print(f'Prime numbers (first 5): {list(prime_num(5))}')

if __name__ == '__main__':
    main()