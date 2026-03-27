import abc


class DataProcessor(abc.ABC):
    
    @abc.abstractmethod
    def process(self, data):
        pass
    @abc.abstractmethod
    def validate(self, data):
        pass
        
    def format_output(self, result: str) -> str:
        return f'Output: {result}'


class NumericProcessor(DataProcessor):

    def process(self, data) -> str:
        soma = 0
        for item in data:
            soma += item
        return f'the sum of data is {soma}'

    def validate(self, data) -> bool:
        for num in data:
            if num < 1 or num > 10:
                return False
        return True
    
    def format_output(self, result: str) -> str:
        return f'Output: {result}'


class TextProcessor(DataProcessor):

    def process(self, data) -> str:
        word = ''
        for item in data:
            word += item
        return f'{word}'

    def validate(self, data) -> bool:
        if len(data) < 3:
            return False
        return True
    
    def count_letters(self, data):
        return len(data)

    def format_output(self, result: str) -> str:
        return f'Output: Processed text: {len(result)} words'
    

class LogProcessor(DataProcessor):

    def process(self, data) -> str:
        if data == 'ERROR: Connection timeout':
            data += '...\n\t-> Please try again'
        return data

    def validate(self, data) -> bool:
        if "ERROR" in data:
            return True
        return False

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f'Output: [ALERT] {result}'
        return f'Output: {result}'
        


def try_numeric():

    print('Initializing Numeric Processor...')

    valid_num = [1, 2, 3, 4, 5]
    invalid_num = [1, 2, 3, 4, 50]

    numeric = NumericProcessor()
    result = numeric.process(valid_num)

    try:
        if numeric.validate(valid_num):
            print(f'Processing data: {valid_num}')
            print(f'{numeric.process(valid_num)}')
            print(numeric.format_output(result))

        if numeric.validate(invalid_num):
            print(f'Processing data: {invalid_num}')
            print(f'{numeric.process(invalid_num)}')
            print(numeric.format_output(invalid_num))
    
    except Exception as e:
        print(e)


def try_text():
    
    print('Initializing Text Processor...')

    valid_text = ['Hello', 'Nexus', 'World']
    invalid_text = ['Hello', 'World']

    text = TextProcessor()

    try:
        if text.validate(valid_text):
            print(f'Processing data: "{valid_text}"')
            print(f'The string in one word is: {text.process(valid_text)}')
            print(text.format_output(valid_text))

        if text.validate(invalid_text):
            print(f'Processing data: "{invalid_text}"')
            print(f'The string in one word is: {text.process(invalid_text)}')
            print(text.format_output(invalid_text))

    except Exception as e:
        print(e)


def try_log():

    print('Initializing Log Processor...')

    valid_log = 'Connection Stablished'
    invalid_log = 'ERROR: Connection timeout'

    log = LogProcessor()

    try:
        if log.validate(invalid_log):
            print(f'Processing data: "{invalid_log}"')
            print(f'{log.process(invalid_log)}')
            print(log.format_output(invalid_log))

        if log.validate(valid_log):
            print(f'Processing data: "{valid_log}"')
            print(f'{log.process(valid_log)}')
            print(log.format_output(valid_log))

    except Exception as e:
        print(e)


def polimorfism():
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data = [[5, 4, 3, 2, 1], ['Hello', 'World', 'Sei la'], 'ERROR: Connection timeout']
    
    for processor, data_item in zip(processors, data):
        if processor.validate(data_item):
            result = processor.process(data_item)
            print(processor.format_output(result))


def main():
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n')
    try_numeric()
    print()
    try_text()
    print()
    try_log()
    print()
    print('=== POLIMORFISM ===')
    polimorfism()


if __name__ == '__main__':
    main()

