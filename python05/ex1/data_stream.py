from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"processed": 0}
    

class SensorStream(DataStream):

    def process_batch(self, data_batch):
        data_batch = self.filter_data(data_batch)
        avg = 0
        for i in data_batch:
            avg += float(i)
        try:
            return str(avg / len(data_batch))
        except ZeroDivisionError:
            return f'Tried to calculate average but list is empty'

    def filter_data(self, data_batch, criteria = None):
        filtered = [i for i in data_batch if isinstance(i, float)]
        return filtered


class TransactionStream(DataStream):

    def process_batch(self, data_batch):
        data_batch = self.filter_data(data_batch)
        total = 0
        for value in data_batch:
            total += value
        return str(total)

    def filter_data(self, data_batch, criteria = None):
        filtered = [i for i in data_batch if isinstance(i, (int, float))]
        return filtered


class EventStream(DataStream):

    def process_batch(self, data_batch):
        filtered = self.filter_data(data_batch)
        errors = len(data_batch) - len(filtered)
        return errors
    
    def filter_data(self, data_batch, criteria = None):
        filtered = [s for s in data_batch if isinstance(s, str)]
        return filtered


def sensor_try():

    print('Initializing Sensor Stream...')
    print('Stream ID: SENSOR_001, Type: Environmental Data')
    sensor_batch = {
        'temp': 22.5,
        'humidity': 65,
        'pressure': 1013
    }
    values = list(sensor_batch.values())
    stream = SensorStream()
    print(f'Processing sensor batch {sensor_batch}')
    print(f'Sensor analysis: {len(sensor_batch)} readings processed, avg temp: {stream.process_batch(values)}')


def transaction_try():

    print('Initializing Transaction Stream...')
    print('Stream ID: TRANS_001, Type: Financial Data')
    trasaction_batch = {
        'buy1': 100,
        'sell': -150,
        'buy2': 75
    }
    values = list(trasaction_batch.values())
    stream = TransactionStream()
    print(f'Processing transaction batch {trasaction_batch}')
    print(f'Transaction analysis: {len(trasaction_batch)} operations,'
          f'net flow: {stream.process_batch(values)}')


def events_try():
    
    print('Initializing Event Stream...')
    print('Stream ID: EVENT_001, Type: System Events')
    events_batch = ['login', 42, 'logout']
    stream = EventStream()
    error = stream.process_batch(events_batch)
    print(f'Processing event batch: {events_batch}')
    print(f'Event analysis: {len(events_batch)} events, {error} error detected')



def poli():
    print('=== Polymorphic Stream Processing ===')
    print('Processing mixed stream types through unified interface...')
    print()
    sensor_data = [22.5, 65.5, 1013]
    transaction_data = [100, -150, 75]
    event_data = ['login', 42, 'logout']
    process = [
        (SensorStream(), sensor_data),
        (TransactionStream(), transaction_data),
        (EventStream(), event_data)
    ]
    for stream, data in process:
        try:
            result = stream.process_batch(data)
            print(result)
        except Exception as e:
            print("Erro:", e)


def main():

    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')
    print()
    sensor_try()
    print()
    transaction_try()
    print()
    events_try()
    print()
    poli()


if __name__ == '__main__':

    main()
