from abc import ABC, abstractmethod
from typing import Any

class QuestionGenerator(ABC):
    @abstractmethod
    def generate(self, analysis: Any, max_questions: int = 5) -> list[dict]:
        raise NotImplementedError
