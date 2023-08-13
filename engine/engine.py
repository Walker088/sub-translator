
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def Translate(self, query:str) -> str:
        return "Default Implementation"
