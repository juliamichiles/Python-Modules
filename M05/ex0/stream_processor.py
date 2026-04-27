#!/usr/bin/python3
from abc import ABC
from typing import Any, List, Dict, Union, Optional


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
                if not isinstance(data, (int, float)):
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
    
    def validate(self, data: Any) - bool:
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
