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
            return self._counter, value
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
        if not self.validate(data):
            raise ValueError('Invalid numeric data')
        if isinstance(data, (int, float)):
            self._data.append(str(data))
        elif isinstance(data, list):
            for item in data:
                self._data.append(str(item))

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
        if not self.validate(data):
            raise ValueError('Invalid text data')

        if isinstance(data, str):
            self._data.append(data)

        elif isinstance(data, list):
            for item in data:
                self._data.append(item)
    
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
        if isinstance(data, dict):
            self._data.append(data.items())
        if isinstance(data, list) and self.validate(data):
            for item in data:
                self._data.append(item)

    def output(self):
        return super().output()
        

def numeric_try():
    print('Testing Numeric Processor...')
    true_numeric = NumericProcessor()
    true_try = true_numeric.validate(42)
    print(f'Trying to validate input "42": {true_try}')
    false_numeric = NumericProcessor()
    false_try = false_numeric.validate('hello')
    print(f'Trying to validate input "hello": {false_try}')
    invalid_numeric = NumericProcessor()
    print('Test invalid ingestion of string "foo" without prior validation:')
    try:
        invalid_numeric.ingest('foo') 
    except ValueError as e:
        print(e)
    numeric_data = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    if numeric_data.validate(data):
        numeric_data.ingest(data)
    print('Processing data: [1, 2, 3, 4, 5]')
    print('Extracting 3 values...')
    i = 0
    while i < 3:
        print(numeric_data.output())
        i += 1


def text_try():
    print('Testing Text Processor...')
    text = TextProcessor()
    false_try = text.validate(42)
    print(f'Trying to validate input "42": {false_try}')
    data = ['Hello', 'Nexus', 'World']
    true_try = text.validate(data)
    print(f'Trying to validate input "{data}": {true_try}')
    print(f'Processing data {data}')
    text_data = TextProcessor()
    if text_data.validate(data):
        text_data.ingest(data)
    print('Extracting 1 value...')
    print(text_data.output())


def log_try():
    print('Testing Log Processor...')
    log = LogProcessor()
    false_log = log.validate('hello')
    print(f'Trying to validate input "Hello": {false_log}')
    data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    true_log = log.validate(data)
    print(f'Trying to validate input "{data}": {true_log}')
    print('Extracting 2 values...')
    log_data = LogProcessor()
    if log_data.validate(data):
        log_data.ingest(data)
    i = 0
    while i < 2:
        print(log_data.output())
        i += 1

if __name__ == '__main__':
    print('=== Code Nexus - Data Processor ===\n')
    numeric_try()
    print()
    text_try()
    print()
    log_try()