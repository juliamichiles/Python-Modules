#!/usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"
    
    def ft_len(self, data: Any) -> int:
        count = 0
        for element in data:
            count += 1
        return (count)
    
    def count_words(self, data: Any) -> int:
        started: int = 0
        count: int = 0
        for c in data:
            if (c != ' ' and c != '\t') and started == 0:
                started = 1
                count += 1
            if started == 1 and (c == ' ' or c == '\t'):
                started = 0
        return count
    
class NumericProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
    # Validate if data is appropriate for this processor    
        try:
            for element in data:
                element * 1
            return True
        except TypeError:
            return False

    def ft_sum(self, data: Any) -> int:
        total = 0
        for element in data:
            total += element
        return total
    
    def process(self, data: Any) -> str:
        #  Process the data and return result string
        if self.validate(data):
            count = self.ft_len(data)
            elm_sum = self.ft_sum(data)
            avg = elm_sum / count
            return f"Processed {count} numeric values, sum={elm_sum}, avg={avg}"~
        else:
            return "Invalid numeric data"

    def format_output(self, result: str) -> str:
        # Format the output string
        # I think I could remove it, but check subejct
        pass

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data + ""
            return True
        except TypeError:
            return False
            
    def process(self, data: Any) -> str:
        if self.validate(data):
            chars: int = self.ft_len(data) 
            words: int = self.count_words(data)
            return f"Processed text: {chars} characters, {words} words"
        else:
            return "Invalid text data"

    def format_output(self, result: str) -> str:
        # Format the output string
        # I think I could remove it, but check subejct
        pass   


class LogProcessor(DataProcessor):
    def split_log(self, data: Any) -> tup:
        log_type: str = ""
        message: str = ""
        sep: int = 0

        for c in data:
            if sep == 0:
                if c == ':':
                    sep = 1
                else:
                    log_type += c
            else:
                message += c
        return log_type, message

    def validate(self, data: Any) -> bool:
        found_sep: int = 0
        i: int = 0

        # maybe change this? Should only handle a few known types of logs
        for c in data:
            if found_sep == 0:
                if c == ':':
                    found_sep = 1
                elif not ('A' <= c <= 'Z'):
                    return False
            else:
                if i == 0:
                    if c != ' ':
                        return False
                i += 1
        return found_sep == 1

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            # is this proper tuple unpacking?
            log_type, message: str = self.split_log(data)
            return f""
            # unfinished
            # should also categorize each log


def processor_demo() -> None:
    # function that actually creates the streams and prints 
    # output as expected by the example


if __name__ == "__main__":
