#!/usr/bin/python3
import random
from typing import Generator


# generates random events
def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "use", "release", "swim"]
    while True:
        yield (random.choice(players), random.choice(actions))

def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event

def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")

    # generate 1000 events
    event_generator = gen_event()
    for i in range(1000):
        player, action = next(event_generator)
        print(f"Event {i}: Player {player} did action {action}")
    
    # creates list with 10 events
    event_list = [next(event_generator) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}\n")

    # Consume events from the list
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()

