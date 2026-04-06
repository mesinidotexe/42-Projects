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
        for item in data:
            try:
                float(item)
                return True
            except ValueError:
                return False

    def ingest(self, data: Any) -> None:
        for item in data:
            try:
                str(item)
            except Exception as e:
                raise (f'The program found the error: {e}')
        
    def output(self):
        return super().output()


class TextProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        for item in data:
            try:
                str(item)
                return True
            except Exception:
                return False
            
    def ingest(self, data: Any) -> None:
        for item in data:
            try:
                str(item)
            except Exception as e:
                raise (f'The program found the error: {e}')
    
    def output(self):
        return super().output()


class LogProcessor(DataProcessor):
    
    def validate(self, data: Any) -> bool:
        for item in data:
            if not isinstance(item, dict):
                return False
        return True
            
    def ingest(self, data: Any) -> None:
        try:
            for chave, valor in data.items():
                if not isinstance(chave, str):
                    continue
                if not isinstance(valor, str):
                    continue
        except Exception as e:
             raise (f'The program found the error: {e}')
        
    def output(self):
        return super().output()
        

if __name__ == '__main__':
    print('=== Code Nexus - Data Processor ===\n')
    
    print('Testing Numeric Processor...')
    true_numeric = NumericProcessor()
    true_try = true_numeric.validate('42')
    print(f'Trying to validate input "42": {true_try}')
    false_numeric = NumericProcessor()
    false_try = false_numeric.validate('hello')
    print(f'Trying to validate input "hello": {false_try}')
    invalid_numeric = NumericProcessor()
    invalid_try = invalid_numeric.ingest('foo')
    print('Test invalid ingestion of string "foo" without prior validation:')
    print(invalid_try)