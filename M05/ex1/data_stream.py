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


class DataStream:
    # receive a stream of data containing different types and routs
    # each element to the appropriate data processor

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        # registers a new data processor to process the data stream
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        # analyzes each element of the list received as a parameter and
        # send it to the appropriate processor

        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    try:
                        proc.ingest(element)
                    except Exception as e:
                        print(f"DataStream error - Ingestion failed: {e}")
                    handled = True
                    break
            if not handled:
                print(
                        "DataStream error - Can't process"
                        f" element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        # prints stream statistics

        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = type(proc).__name__
            spaced_name = name.replace("Processor", " Processor")

            total = proc.rank
            remaining = len(proc.storage)
            print(
                    f"{spaced_name}: total {total} items processed,"
                    f" remaining {remaining} on processor"
            )


def data_stream_demo() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")

    # attempt printing empty DataStream stats
    stream = DataStream()
    stream.print_processors_stats()

    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    # adding the NumericProcessor
    print("\nRegistering Numeric Processor\n")
    num_p = NumericProcessor()
    stream.register_processor(num_p)

    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    # adding the remaining processors
    print("\nRegistering other data processors")
    txt_p = TextProcessor()
    log_p = LogProcessor()
    stream.register_processor(txt_p)
    stream.register_processor(log_p)

    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()

    print(
            "\nConsume some elements from the data processors:"
            " Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        num_p.output()

    for _ in range(2):
        txt_p.output()

    for _ in range(1):
        log_p.output()

    stream.print_processors_stats()


if __name__ == '__main__':
    data_stream_demo()
