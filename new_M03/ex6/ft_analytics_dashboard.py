#!/usr/bin/python3

def ft_analytics_dashboard() -> None:

    print("=== Game Analytics Dashboard ===\n")

    players = [
        {"name": "edilson", "score": 500, "achievements":
         ["plant", "little_devil"], "region": "north_east"},
        {"name": "jordan", "score": 2000, "achievements":
         ["ant", "popcorn"], "region": "north"},
        {"name": "cowboy", "score": 1200, "achievements":
         ["brain_eater", "ant"], "region": "general_mines"},
        {"name": "milena", "score": 3150, "achievements":
         ["popcorn", "trouble_maker", "eternal"], "region": "general_mines"},
        {"name": "juliano", "score": 2750, "achievements":
         ["dancer", "eternal"], "region": "south"},
        {"name": "babu", "score": 1200, "achievements":
         ["veteran", "unidunite", "trouble_maker"], "region": "south_east"},
    ]

    print("=== List Comprehension Examples ===")
    high_scores = [plyr["name"] for plyr in players if plyr["score"] > 2000]
    doubled_scores = [plyr["score"] * 2 for plyr in players]
    active_players = [plyr["name"] for plyr in players if plyr["score"] > 1000]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {player["name"]: player["score"] for player in players}
    score_categ = {
        "high": sum(1 for p in players if p["score"] > 2000),
        "medium": sum(1 for p in players if 1000 < p["score"] <= 2000),
        "low": sum(1 for p in players if p["score"] <= 1000)
    }
    achievement_count = {player["name"]:
                         len(player["achievements"]) for player in players}
    print(f"Player scores: {player_scores}")
    print(f"Scores categories: {score_categ}")
    print(f"Achievement counts: {achievement_count}")

    unique_players = {player["name"] for player in players}
    unique_achievements = {
        achievement
        for player in players
        for achievement in player["achievements"]
    }
    active_regions = {player["region"] for player in players}
    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(unique_players)
    average_score = sum(p["score"] for p in players) / total_players
    top_perf = players[0]
    for player in players:
        if player["score"] > top_perf["score"]:
            top_perf = player
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {average_score}")
    print(f"Top perf: {top_perf['name']} ({top_perf['score']}", end="")
    print(f" points, {len(top_perf['achievements'])} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
