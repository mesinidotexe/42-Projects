from ex0.data_processor import DataProcessor, NumericProcessor, TextProcessor, LogProcessor
from ex1.data_stream import DataStream as BaseDataStream
from typing import Protocol


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExport():

    def process_output(self, data: list[tuple[int, str]]) -> None:
        self.cvs = ''
        for id, value in data:
            if isinstance(value, str):
                self.cvs += str(id)
                self.cvs += ','
                self.cvs += value
                self.cvs += '\n'
        print('CVS output')
        print(self.cvs)

class DataStream(BaseDataStream):

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        collected = []
        for processor in self.procs:
            data = list(processor.output())
            collected.append(data)
        plugin.process_output(collected)


def cvs_try():
    stream = DataStream()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]
    stream.process_stream(data)
    plugin = CSVExport()
    stream.print_processors_stats()
    print('\n')
    stream.output_pipeline(3, plugin)



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
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]
    print(f'Send first batch of data on stream: {data}')
    cvs_try()
    
    
    

if __name__ == '__main__':
    main()