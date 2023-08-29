
from abc import ABC, abstractmethod
from srt import Subtitle

class Engine(ABC):
    @abstractmethod
    def Translate(self, query: str) -> str:
        return "Default Implementation"
    
    @abstractmethod
    def TranslateList(self, queries: list[Subtitle]) -> list[Subtitle]:
        return "Default Implementation"
