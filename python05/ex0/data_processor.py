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
            ingested = (DataProcessor.ingest(self))
            return f'{ingested}'


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        self.data = ''
        if isinstance(data, (int, float)):
            self.data = str(data)
        if isinstance(data, (list)):
            for item in data:
                self.data += item
        if not self.validate(data):
            raise ValueError('Got exception: Improper numeric data')

    def output(self):
        return super().output()


class TextProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        for item in data:
            try:
                str(item)
            except Exception:
                return False
        return True
            
    def ingest(self, data: Any) -> None:
        for item in data:
            try:
                str(item)
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
                raise e('try again')
        
    def output(self):
        return super().output()
        

if __name__ == '__main__':
    print('=== Code Nexus - Data Processor ===\n')
    
    try:
        print('Testing Numeric Processor...')
        true_numeric = NumericProcessor()
        true_try = true_numeric.validate(42)
        print(f'Trying to validate input "42": {true_try}')
        false_numeric = NumericProcessor()
        false_try = false_numeric.validate('hello')
        print(f'Trying to validate input "hello": {false_try}')
        invalid_numeric = NumericProcessor()
        print('Test invalid ingestion of string "foo" without prior validation:')
        print(invalid_numeric.ingest('foo'))
        print('Processing data: [1, 2, 3, 4, 5]')
    except Exception as e:
        print(e)