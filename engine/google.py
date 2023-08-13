from engine.engine import Engine
from googletrans import Translator

class GoogleTranslateEngine(Engine):
    translator = Translator()

    def Translate(self, query:str) -> str:
        self.translator.translate(query)
        return query
