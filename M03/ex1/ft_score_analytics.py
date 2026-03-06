#!/usr/bin/python3
import sys


class NoPlayersError(Exception):
    pass


def ft_score_analytics() -> None:

    print("=== Player Score Analytics ===")

    score_list = []
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            score_list.append(score)
        except ValueError:
            print(f"'{arg}' is invalid!")

    if not score_list:
        print("No scores provided. Usage: python3", end=" ")
        print("ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(score_list)
    print(f"Scores processed: {score_list}")
    print(f"Total players: {total_players}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / total_players}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    score_range = max(score_list) - min(score_list)
    print(f"Score range: {score_range}\n")


if __name__ == "__main__":
    ft_score_analytics()
