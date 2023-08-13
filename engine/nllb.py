
from transformers import pipeline, Pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import re

from config import Config
from engine.engine import Engine

class NllbEngine(Engine):
    translator: Pipeline

    def __init__(self, c: Config) -> None:
        tokenizer = AutoTokenizer.from_pretrained(c.model)
        model = AutoModelForSeq2SeqLM.from_pretrained(c.model)
        self.translator = pipeline(
            "translation",
            model=model,
            tokenizer=tokenizer,
            src_lang=c.srcLang,
            tgt_lang=c.tgtLang,
            max_length=c.maxLength
        )

    def Translate(self, query:str) -> str:
        #regex = re.compile(r"([\w|\[, '-]*[?|.|!|\]])|(♪[\w|, ']*♪*)")
        #matches = regex.finditer(query.replace("\n", " "))
        #cleaned = [match.group(0).strip() for match in matches]
        #translated = [self.translator(s)[0]["translation_text"] for s in cleaned]
        #return "\n".join(translated)
        return self.translator(query)[0]["translation_text"]
