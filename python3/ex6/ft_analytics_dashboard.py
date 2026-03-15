def main():

    players = ["alice", "bob", "charlie", "diana"]
    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
    }

    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer"],
        "bob": ["first_kill", "level_10", "boss_slayer"],
        "charlie": ["first_kill", "level_10", "boss_slayer",],
        "diana": ["first_kill", "level_10", "boss_slayer"]
    }

    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north"
    }

    status = {
        "alice": "active",
        "bob": "active",
        "charlie": "active",
        "diana": "unactive"
    }

    print('=== Game Analytics Dashboard ===')
    print()
    print('=== List Comprehension Examples ===')
    high_score_players = [player for player in players if scores[player] > 2000]
    print(f'High Scores (>2000): {high_score_players}')
    doubled_scores = [score * 2 for score in scores.values()]
    print(f'Scores doubled: {doubled_scores}')
    active_players = [player for player, state in status.items() if state == "active"]
    print(f'Active players: {active_players}')

    print()

    print("=== Dict Comprehension Examples ===")
    print(f"Players scores: {scores}")
    score_categories = {
        "high:": len([score for score in scores.values() if score >= 2000]),
        "mid": len([score for score in scores.values() if score <= 2050]),
        "low": len([score for score in scores.values() if score < 1900])
    }
    print(f'Score Categories: {score_categories}')
    achievement_counts = {
        "alice": len(achievements["alice"]),
        "bob": len(achievements["bob"]),
        "charlie": len(achievements["charlie"])
    }
    print(f'Achievement counts: {achievement_counts}')

    print()

    print('=== Set Comprehension Examples ===')
    print(f'Unique players: {players}')
    unique_achievements = {
        ach
        for player_ach in achievements.values()
        for ach in player_ach
    }
    print(f'Unique achievements: {unique_achievements}')
    active_regions = {
        regions[player]
        for player in players if status[player] == "active"
    }
    print(f'Active regions: {active_regions}')

    print()

    print('=== Combined Analysis ===')
    print(f'Total players: {len(players)}')
    total_achievements = [
        content for each_list in achievements.values()
        for content in each_list
    ]
    print(f'Total unique achievements: {len(total_achievements)}')
    average = sum(a for a in scores.values()) / len(scores)
    print(f'Average score: {average}')
    max_score = max(scores.values())
    top_performer = ""
    for mvp, score in scores.items():
        if max_score == score:
            top_performer = mvp
    print(f'Top Performer: {top_performer}, ({max_score} points, '
          f'{len(achievements[top_performer])} achievements')

if __name__ == '__main__':
    main()