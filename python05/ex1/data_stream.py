from ex0.data_processor import DataProcessor, NumericProcessor
import typing

class DataStream():

    def __init__(self):
        self.procs = []
        self.count = 0

    def register_processor(self, proc: DataProcessor) -> None:
        self.procs.append(proc)


    def process_stream(self, stream: list[typing.Any]) -> None:
        if not stream:
            print('No processor found, no data')
        for data in stream:
            found = False
            for proc in self.procs:
                if proc.validate(data):
                    proc.ingest(data)
                    found = True
                    break
            if not found:
                    print(f'DataStream error - Cant process element in stream: {data}')

    def print_processors_stats(self) -> None:
        for proc in self.procs:
            print(f"Processor: {proc.__class__.__name__}")


def numeric_process():
    data_stream = DataStream()
    print('\nRegistering Numeric Processor\n')
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]
    print(f'Send first batch of data on stream {data}\n')
    numeric_processor = NumericProcessor()
    data_stream.register_processor(numeric_processor)
    data_stream.process_stream(data)
    data_stream.print_processors_stats()


def main():
    print('=== Code Nexus - Data Stream ===')
    print('\nInitialize Data Stream...')
    data_stream = DataStream()
    data = []
    data_stream.process_stream(data)
    numeric_process()


if __name__ == '__main__':
    main()