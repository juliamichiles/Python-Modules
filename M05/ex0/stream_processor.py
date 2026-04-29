#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Sequence


class DataProcessor(ABC):
    def __init__(self) -> None:
        # empty list and idx to internally store data
        self.storage: List[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # validates received data
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        # processes and stores received data
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data to output!")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    # processes ints, floats and lists of them

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            # is that right? I think so...
            if len(data) == 0:
                return False
            for element in data:
                if not isinstance(element, (int, float)):
                    return False
            return True
        else:
            return False

    # changed List[Union[...]] to Sequence[Union[...]] bc of mypy
    def ingest(
        self,
        data: Union[
            int,
            float,
            Sequence[Union[int, float]]
        ]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for element in data:
                self.storage.append((self.rank, str(element)))
                self.rank += 1
        else:
            self.storage.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    # processes strings and lists of strings

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            if len(data) == 0:
                return False
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for element in data:
                self.storage.append((self.rank, element))
                self.rank += 1
        else:
            self.storage.append((self.rank, data))
            self.rank += 1


class LogProcessor(DataProcessor):
    # processes log data aka a dict or a list of dicts

    def validate(self, data: Any) -> bool:
        def validate_log(log_data: Any) -> bool:
            if not isinstance(log_data, dict):
                return False
            for key, value in log_data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        if isinstance(data, list):
            return len(data) > 0 and all(validate_log(d) for d in data)

        if validate_log(data):
            return True
        return False

    def ingest(
               self,
               data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:

        if not self.validate(data):
            raise ValueError("Improper log data")

        # turns data into a list if it only has one element
        data_to_process = data if isinstance(data, list) else [data]

        for element in data_to_process:
            val_str = ": ".join(element.values())
            self.storage.append((self.rank, val_str))
            self.rank += 1


def expected_demo() -> None:

    print("=== Code Nexus - Data Processor ===\n")

    # Numeric Processor Demo
    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # will generate mypy error!! (and its ok)
        num_proc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    demo_num = [1, 2, 3, 4, 5]
    print(f" Processing data: {demo_num}")
    num_proc.ingest(demo_num)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    # Text Processor Demo
    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()
    demo_txt = ['Hello', 'Nexus', 'World']
    print(f" Trying to validate input '42': {txt_proc.validate(42)}")
    print(f" Processing data: {demo_txt}")
    txt_proc.ingest(demo_txt)
    print(" Extracting 1 value...")
    rank, value = txt_proc.output()
    print(f" Text value {rank}: {value}")

    # Log Processor Demo
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    demo_log = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]

    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    print(f" Processing data: {demo_log}")
    print(" Extracting 2 values...")

    log_proc.ingest(demo_log)
    for _ in range(2):
        rank, value = log_proc.output()
        print(f" Log entry {rank}: {value}")


# COMMENT THE FUNCTION BELLOW BEFORE SUBMISSION!
# def more_tests() -> None:
#
#     print("\n\n--- MORE TESTS! ---\n")
#     # larger and longer tests for each processor
#     # tests with empty data sets for each processor
#
#     # directly instantiate base class to see what happens
#     print("1 - What happens when we try to instantiate an abc directly?")
#     try:
#         data_proc = DataProcessor()
#         data = "haha"
#         print(f"Validating 'haha': {data_proc.validate(data)}")
#     except Exception as e:
#         print(f"Caught expected TypeError: {e}")
#
#     # FIFO and Rank persistence (for NumericProcessor)
#     print("\n2 - Now let's check if FIFO is being followed...")
#     n_proc = NumericProcessor()
#     n_proc.ingest(100)
#     n_proc.ingest([200, 300])
#
#     # First out
#     r1, v1 = n_proc.output()
#     print(f"First out (Expect 0, '100'): {r1}, {v1}")
#
#     # Now, rank should continue from 3
#     n_proc.ingest([400, 500, 600, 700, 1000, -1000])
#     while True:
#         try:
#             r, v = n_proc.output()
#             print(f"Extracted Rank {r}: {v}")
#         except (IndexError, ValueError):
#             break
#
#     # Mixed-Type "sabotage"
#     print("\n3 - Let's \"sabotage\" our processor with mixed data now!")
#     t_proc = TextProcessor()
#     poisoned_list = ["Good", 123, "Good"]
#     is_valid = t_proc.validate(poisoned_list)
#     print(f"Is list with '123' valid? {is_valid}")
#     try:
#         if not is_valid:
#             print("Attempt to ingest invalid data!")
#             t_proc.ingest(poisoned_list)
#     except ValueError as e:
#         print(f"{e}")
#
#     # Log chaos
#     print("\n4 - Now it's the log processor's turn...")
#     l_proc = LogProcessor()
#     chaos = [
#         ({}, "Empty Dict"),
#         ({"key": 123}, "Non-string value"),
#         ({"level": "INFO", "msg": "Hi", "extra": "data"}, "Multi-key")
#     ]
#
#     for data, test in chaos:
#         valid = l_proc.validate(data)
#         print(f"Testing {test}: Valid={valid}")
#         if valid:
#             l_proc.ingest(data)
#             print("Resulting output: {l_proc.output()}")
#
#     # Output from empty processor
#     print("\n5 - Let's try to get output from an empty processor")
#     empty_proc = TextProcessor()
#     try:
#         empty_proc.output()
#     except IndexError:
#         print("Caught IndexError: Cannot output from empty processor.")
#     except Exception as e:
#         print(f"Caught unexpected exception: {type(e).__name__}")
#
#     print("\nNow we're done :)")
#
#
if __name__ == '__main__':
    expected_demo()
#    more_tests() #  COMMENT this line before submission
