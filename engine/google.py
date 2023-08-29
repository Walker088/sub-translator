from engine.engine import Engine

from google.cloud import translate_v2 as translate
from google.cloud.translate_v2 import Client
from srt import Subtitle
from tqdm import tqdm
from typing import TypedDict

import asyncio
import os

class SubTitleQuery(TypedDict):
    idx : int
    subtitle : str

class GoogleTranslateEngine(Engine):
    translator: Client

    def __init__(self, c) -> None:
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
    
    def TranslateList(self, queries: list[Subtitle]) -> list[Subtitle]:
        async def translate(sq: SubTitleQuery):
            sq["subtitle"] = self.translator.translate(
                sq["subtitle"],
                source_language=self.src_lang,
                target_language=self.tgt_lang
            )["translatedText"]
            return sq
        async def run():
            jobs = [translate({"idx": q.index, "subtitle": q.content}) for q in queries]
            for job in tqdm(asyncio.as_completed(jobs), desc="translating", total=len(jobs)):
                try:
                    translated = (await job)
                    queries[translated["idx"] - 1].content = translated["subtitle"]
                except asyncio.TimeoutError as e:
                    print(e)
        asyncio.run(run())
        return queries
