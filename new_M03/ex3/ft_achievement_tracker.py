#!/usr/bin/python3

class Player:
    def __init__(self, name: str, achievements: set):
        self.name = name
        self.achievements = achievements

    def get_achievements(self) -> str:
        ach = self.achievements
        return f"Player {self.name} achievements: {ach}"

    def count_achievements(self) -> int:
        return len(self.achievements)


def ft_achievement_tracker() -> None:

    """ ====== CREATING PLAYERS ====== """
    alice = Player(
            "alice",
            {
                'first_kill',
                'level_10',
                'treasure_hunter',
                'speed_demon'
             }
    )

    bob = Player(
            "bob",
            {
                'first_kill',
                'level_10',
                'boss_slayer',
                'collector'
            }
    )

    charlie = Player(
            "charlie",
            {
                'level_10',
                'treasure_hunter',
                'boss_slayer',
                'speed_demon',
                'perfectionist'
                }
    )

    """ ======== calculating achievement's stats' ======== """
    unique = alice.achievements.union(bob.achievements)
    unique = unique.union(charlie.achievements)

    common = alice.achievements.intersection(bob.achievements)
    common = common.intersection(charlie.achievements)

    bob_alice = alice.achievements.intersection(bob.achievements)

    alice_unique = alice.achievements - bob.achievements
    bob_unique = bob.achievements - alice.achievements

    """ ======== calculating rare achievements ======== """
    bob_rare = bob.achievements - alice.achievements - charlie.achievements
    alice_rare = alice.achievements - charlie.achievements - bob.achievements
    charlie_rare = charlie.achievements - bob.achievements - alice.achievements
    rare = bob_rare.union(alice_rare).union(charlie_rare)

    print("=== Achievement Tracker System ===\n")
    print(f"{alice.get_achievements()}")
    print(f"{bob.get_achievements()}")
    print(f"{charlie.get_achievements()}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {bob_alice}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    ft_achievement_tracker()
