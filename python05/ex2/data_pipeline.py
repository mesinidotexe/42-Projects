from ex0.data_processor import NumericProcessor, TextProcessor, LogProcessor
from ex1.data_stream import DataStream as BaseDataStream
from typing import Protocol


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExport():

    def process_output(self, data: list[tuple[int, str]]) -> None:
        self.csv = ''
        for _, value in data:
            for item in value:
                self.csv += str(item)
            self.csv += ','
        self.csv += '\n'
        print('CSV output')
        print(self.csv)


class JSONExport():

    def process_output(self, data: list[tuple[int, str]]) -> None:
        i = 1
        self.json = {}
        for _, values in data:
            self.json[f'item_{i}'] = values
            i += 1
        print('JSON Output')
        print(self.json)
        print()


class DataStream(BaseDataStream):

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.procs:
            collected = []
            i = 0
            while i < nb:
                try:
                    result = processor.output()
                    collected.append(result)
                    i += 1
                except IndexError:
                    break
            plugin.process_output(collected)


def csv_try(data):
    stream = DataStream()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    stream.process_stream(data)
    plugin = CSVExport()
    stream.print_processors_stats()
    print('\n')
    stream.output_pipeline(3, plugin)


def json_try(new_data):
    stream = DataStream()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    stream.process_stream(new_data)
    plugin = JSONExport()
    stream.print_processors_stats()
    print('\n')
    stream.output_pipeline(7, plugin)


def main():
    print('=== Code Nexus - Data Pipeline ===')
    print()
    print('Initialize Data Stream...')
    print('\n== DataStream statistics ==')
    stream = DataStream()
    stream.process_stream('')
    print('\nRegistering Processors\n')
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! '
          'Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]
    print(f'Send first batch of data on stream: {data}\n')
    csv_try(data)
    new_data = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': ' ERROR', 'log_message': '500 server crash'},
        {'log_level': 'NOTICE', 'log_message': 
         'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
        ]
    print('\n')
    print(f'Send another batch of data: {new_data}\n')
    json_try(new_data)
    

if __name__ == '__main__':
    main()