from abc import abstractmethod, ABC
from typing import Any

class DataProcessor(ABC):
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if DataProcessor.validate(self):
            return self.ingest


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        self.data = ''
        if not self.validate(data):
            raise ValueError('Got exception: Improper numeric data')
        if isinstance(data, (int, float)):
            self.data = str(data)
        if isinstance(data, (list)):
            for item in data:
                self.data += str(item)

    def output(self):
        return 


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
        self.data = ''
        for item in data:
            try:
                self.data += str(item)
            except Exception as e:
                raise (f'Got exception: Improper numeric data {e}')
    
    def output(self):
        return super().output()


class LogProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        for item in data:
            if not isinstance(item, dict):
                return False
        return True
            
    def ingest(self, data: Any) -> None:
        arr = ''
        for chave, valor in data.items():
            try:
                arr += str(chave)
                arr += str(valor)
            except Exception as e:
                raise ValueError('try again') from e
        
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
        print(f'Numeric value {i}: {data[i]}')
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
    print('Extracting 1 value...')
    print(f'Text value 0: {data[0]}')


if __name__ == '__main__':

    print('=== Code Nexus - Data Processor ===\n')
    numeric_try()
    print('')
    text_try()