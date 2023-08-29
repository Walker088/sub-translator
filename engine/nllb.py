
import torch
from transformers import pipeline, Pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm
from srt import Subtitle

from engine.engine import Engine

class NllbEngine(Engine):
    translator: Pipeline

    def __init__(self, c) -> None:
        ec = c.engine.engine_configs
        tokenizer = AutoTokenizer.from_pretrained(ec["model"])
        model = AutoModelForSeq2SeqLM.from_pretrained(ec["model"])
        
        device = -1
        if (torch.cuda.is_available()):
            device = torch.cuda.current_device()
        
        self.translator = pipeline(
            "translation",
            device=device,
            model=model,
            tokenizer=tokenizer,
            src_lang=ec["srcLang"],
            tgt_lang=ec["tgtLang"],
            max_length=ec["maxLength"]
        )

    def Translate(self, query:str) -> str:
        return self.translator(query)[0]["translation_text"] # type: ignore
    
    def TranslateList(self, queries: list[Subtitle]) -> list[Subtitle]:
        st_idx = 0
        res = queries.copy()
        stream = (sub.content for sub in queries)

        for result in tqdm(self.translator(stream, batch_size=1), total=len(queries)):
            #if (type(result) is list):
            #    translated = result[0]["translation_text"]
            #    res[st_idx].content = translated
            #    st_idx += 1
            translated = result[0]["translation_text"] # type: ignore
            res[st_idx].content = translated
            st_idx += 1
        return res
