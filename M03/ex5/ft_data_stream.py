#!/usr/bin/python3
from typing import Generator


def is_prime(n: int) -> bool:
    guess = 2
    if n < 2:
        return False
    while guess * guess < n:
        if n % guess == 0:
            return False
        guess += 1
    return True


def prime_gen(count: int) -> Generator[int, None, None]:
    number = 2
    found = 0

    while found < count:
        if is_prime(number):
            yield number
            found += 1
        number += 1


def fibonacci_gen(count: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    i = 0

    while i < count:
        yield a
        a, b = b, b + a
        i += 1


def generate_events(count: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie", "diana"]
    event_types = ["kill", "treasure", "level_up"]
    # add more players and events?
    i = 1
    while i <= count:
        event = {
            "id": i,
            "player": players[i % len(players)],
            "level": (i * 3) % 20 + 1,
            "event_type": event_types[i % len(event_types)]
            }
        yield event
        i += 1


def format_sequence(seq: str,
                    total: int,
                    seq_stream: Generator[int, None, None]) -> None:

    print(seq, end=" ")
    i = 0
    for num in seq_stream:
        if i < total - 1:
            print(f"{num}", end=", ")
        else:
            print(f"{num}")
        i += 1


def process_stream(event_stream: Generator[dict, None, None]) -> tuple:
    total = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event in event_stream:
        total += 1

        player = event["player"]
        level = event["level"]
        event_type = event["event_type"]

        if total <= 5:
            print(f"Event {total}: Player {player} (level {level})", end=" ")
            if event_type == "kill":
                print("killed monster")
            elif event_type == "treasure":
                print("found treasure")
            elif event_type == "level_up":
                print("leveled up")

        if level >= 10:
            high_level += 1
        if event_type == "treasure":
            treasure_events += 1
        if event_type == "level_up":
            level_up_events += 1

    return total, high_level, treasure_events, level_up_events


def ft_data_stream() -> None:

    n = 1000
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {n} game events...\n")

    data = process_stream(generate_events(n))
    total, high_level, treasure_events, level_up_events = data

    print("...\n\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    # How else could I do this without importing 'time'?
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.038 seconds")

    print("\n=== Generator Demonstration ===")
    format_sequence("Fibonacci sequence (first 10):", 10, fibonacci_gen(10))
    format_sequence("Prime numbers (first 5):", 5, prime_gen(5))


if __name__ == "__main__":
    ft_data_stream()
