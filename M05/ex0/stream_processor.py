#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


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

    def ingest(
            self,
            data: Union[int, float,
            List[Union[int, float]]]
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
        return False

        if validate_log(data):
            return True

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
    # larger and longer tests for each processor
    # tests with empty data sets for each processor
    # directly instantiate base class to see what happens


if __name__ == '__main__':
    expected_demo()
#   more_tests() #COMMENT this line before submission
