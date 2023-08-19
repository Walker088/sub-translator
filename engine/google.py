from engine.engine import Engine
from config.config import Config

from google.cloud import translate_v2 as translate
from google.cloud.translate_v2 import Client
import os

class GoogleTranslateEngine(Engine):
    translator: Client

    def __init__(self, c: Config) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = c.engine.engine_configs.get("serviceAccKeyPath", "")
        self.translator = translate.Client()
        self.src_lang = c.engine.engine_configs.get("srcLang", "en")
        self.tgt_lang = c.engine.engine_configs.get("tgtLang", "es")

    def Translate(self, query:str) -> str:
        result = self.translator.translate(
            query,
            source_language=self.src_lang,
            target_language=self.tgt_lang
        )
        return result["translatedText"]
