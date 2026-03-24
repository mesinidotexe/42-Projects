import random


def main():

    players = ["alice", "Bob", "charlie", "Diana"]

    all_caps = [p.capitalize() for p in players]
    only_caps = [p for p in players if p[0].isupper()]

    print('=== Game Analytics Dashboard ===')
    print()
    print('=== List Comprehension ===')
    print(f'All capitalized: {all_caps}')
    print(f'Already capitalized: {only_caps}')

    scores = {p: random.randint(1000, 3000) for p in all_caps}

    print()
    print("=== Dict Comprehension  ===")
    print(f"Players scores: {scores}")

    average = sum(scores.values()) / len(scores)
    print(f'Average score: {round(average, 2)}')

    above_avg = {p: s for p, s in scores.items() if s > average}
    print(f'Above average: {above_avg}')

    print()

    print('=== Extra Analysis ===')
    print(f'Total players: {len(players)}')

    max_score = max(scores.values())
    top_performer = ""
    for name, score in scores.items():
        if score == max_score:
            top_performer = name
            break

    print(f'Top Performer: {top_performer} ({max_score} points)')


if __name__ == '__main__':
    main()
