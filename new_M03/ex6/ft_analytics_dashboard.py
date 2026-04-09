#!/usr/bin/python3
import random


def ft_data_alchemist() -> None:

    # the initial list
    initial_players = [
                    'Alice',
                    'bob',
                    'Charlie',
                    'dylan',
                    'Emma',
                    'Gregory',
                    'john',
                    'kevin',
                    'Liam'
    ]

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {initial_players}")

    # all players capitalized
    all_capi = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capi}")

    # players that were already capitalized
    og_capi = [name for name in initial_players if name == name.capitalize()]
    print(f"New list of capitalized names only: {og_capi}")

    # score dictionary for all players
    score_dict = {name: random.randint(0, 1000) for name in all_capi}
    print(f"\nScore dict: {score_dict}")

    avg = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(avg, 2)}")

    # high scores
    high_scores = {
            name: score for name, score in score_dict.items() if score > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
