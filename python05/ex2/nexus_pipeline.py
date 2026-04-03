from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class ProcessingPipeline(ABC):

    def process(self, data: Any) -> Any:
        pass

