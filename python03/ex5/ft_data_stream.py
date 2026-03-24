import random
import typing


def gen_event():
    players = ["alice", "bob", "charlie", "david"]
    actions = ["killed monster", "found treasure", "leveled up", "died"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list):
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main():
    print('=== Game Data Stream Processor ===')

    event_gen = gen_event()

    for i in range(1000):
        event = next(event_gen)
        print(f'Event {i + 1}: {event}')

    print('\n=== Create list of 10 events ===')

    event_list = []
    for _ in range(10):
        event_list.append(next(event_gen))

    print('Event list:', event_list)

    print('\n=== Consuming events ===')

    for event in consume_event(event_list):
        print(event)


if __name__ == '__main__':
    main()
