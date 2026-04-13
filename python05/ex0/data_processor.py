from abc import abstractmethod, ABC
from typing import Any

class DataProcessor(ABC):
    
    def __init__(self):
        self._data = []
        self._counter = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            value = self._data.pop(0)
            self._counter += 1
            return (self._counter, value)
        except Exception as e:
            if not self._data:
                raise IndexError("No data available")


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        self._counter += 1
        if not self.validate(data):
            raise ValueError('Invalid numeric data')
        if isinstance(data, (int, float)):
            self._data.append(str(data))
            self._counter += 1
        elif isinstance(data, list):
            for item in data:
                self._data.append(str(item))
                self._counter

    def output(self):
        return super().output()


class TextProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        if isinstance (data, str):
                return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False
            
    def ingest(self, data: Any) -> None:
        self._counter += 1
        if not self.validate(data):
            raise ValueError('Invalid text data')

        if isinstance(data, str):
            self._data.append(data)
            self._counter += 1

        elif isinstance(data, list):
            for item in data:
                self._data.append(item)
                self._counter += 1
    
    def output(self):
        return super().output()


class LogProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError('Invalid log data')
        if isinstance(data, dict):
            level = data.get('log_level')
            message = data.get('log_message')
            self._data.append(f"{level}: {message}")
        elif isinstance(data, list):
            for item in data:
                level = item.get('log_level')
                message = item.get('log_message')
                self._data.append(f"{level}: {message}")

    def output(self):
        return super().output()
        

def numeric_try():
    print('Testing Numeric Processor...')
    numeric = NumericProcessor()
    print(f'Trying to validate input "42": {numeric.validate(42)}')
    print(f'Trying to validate input "hello": {numeric.validate("hello")}')
    print('Test invalid ingestion of string "foo" without prior validation:')
    try:
        numeric.ingest('foo') 
    except ValueError as e:
        print(e)
    data = [1, 2, 3, 4, 5]
    if numeric.validate(data):
        numeric.ingest(data)
    print('Processing data: [1, 2, 3, 4, 5]')
    print('Extracting 3 values...')
    i = 0
    while i < 3:
        print(numeric.output())
        i += 1


def text_try():
    print('Testing Text Processor...')
    text = TextProcessor()
    print(f'Trying to validate input "42": {text.validate(42)}')
    data = ['Hello', 'Nexus', 'World']
    print(f'Trying to validate input "{data}": {text.validate(data)}')
    print(f'Processing data {data}')
    if text.validate(data):
        text.ingest(data)
    print('Extracting 1 value...')
    print(text.output())


def log_try():
    print('Testing Log Processor...')
    log = LogProcessor()
    print(f'Trying to validate input "Hello": {log.validate("hello")}')
    data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f'Trying to validate input "{data}": {log.validate(data)}')
    print('Extracting 2 values...')
    if log.validate(data):
        log.ingest(data)
    i = 0
    while i < 2:
        print(log.output())
        i += 1

if __name__ == '__main__':
    print('=== Code Nexus - Data Processor ===\n')
    numeric_try()
    print()
    text_try()
    print()
    log_try()