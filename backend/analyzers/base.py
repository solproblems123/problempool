from abc import ABC, abstractmethod
from typing import Any

class TextAnalyzer(ABC):
    @abstractmethod
    def analyze(self, text: str) -> Any:
        raise NotImplementedError
