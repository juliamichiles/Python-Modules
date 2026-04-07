#!/usr/bin/python3
import random 


class Player:
    def __init__(self, name: str, achievements: set):
        self.name = name
        self.achievements = achievements

    def __str__(self) -> str:
        ach = self.achievements
        return f"Player {self.name} achievements: {ach}"

    def count_achievements(self) -> int:  # remove??
        return len(self.achievements)


def gen_player_achievements(all_achievements: list) -> set:
    count = random.randint(3, len(all_achievements) - 2)
    return set(random.sample(all_achievements, count))


def ft_achievement_tracker() -> None:

    all_achievements = [
        'First Steps',
        'Treasure Hunter',
        'Master Explorer',
        'Speed Runner',
        'Survivor',
        'Strategist',
        'Untouchable',
        'Unstoppable',
        'Boss Slayer',
        'Crafting Genius',
        'World Savior',
        'Collector Supreme',
        'Sharp Mind',
        'Hidden Path Finder'
    ]

    players = [
        Player("Alice", gen_player_achievements(all_achievements)),
        Player("Bob", gen_player_achievements(all_achievements)),
        Player("Charlie", gen_player_achievements(all_achievements)),
        Player("Dylan", gen_player_achievements(all_achievements)),
    ]

    print("=== Achievement Tracker System ===\n")
    for p in players:
        print(p)

    # ======== calculating achievement's stats' ======== 
    
    unique = set()
    for p in players:
        unique = unique.union(p.achievements)

    print(f"\nAll distinct achievements: {unique}")

    common = players[0].achievements
    for p in players[1:]:
        common = common.intersection(p.achievements)
    
    print(f"\nCommon achievements: {common}")


    # ======== calculating rare achievements ======== 
    for p in players:
        others = set()
        for other in players:
            if other != p:
                others = others.union(other.achievements)
        rare = p.achievements.difference(others)
        print(f"Only {p.name} has: {rare}")

    # ======== calculating missing achievements ========
    print("")
    for p in players:
        missing = set(all_achievements).difference(p.achievements)
        print(f"{p.name} is missing: {missing}")

if __name__ == "__main__":
    ft_achievement_tracker()
