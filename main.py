import srt
import os

from typing import Any, Generator, TypedDict
from tqdm import tqdm

from config.config import GetConfig, GetEngine, Config
from engine.engine import Engine

class TranslateCandidates(TypedDict):
    filename : str
    srt_generator : Generator[srt.Subtitle, Any, None]

def parseSrt(c: Config) -> list[TranslateCandidates]:
    srts = []
    for filename in os.listdir(c.srcFolder):
        if not filename.endswith(".srt"):
            continue
        with open(os.path.join(c.srcFolder, filename)) as inp:
            parsedSrt = srt.parse(inp.read())
            srts.append({
                "filename": filename,
                "srt_generator": parsedSrt
            })
    return srts

def DoTranslate(engine: Engine, srts: list[TranslateCandidates], tgtFolder: str):
    with tqdm(total=len(srts)) as fbar:
        for s in srts:
            try:
                fbar.set_description(f"file: {s['filename']}")
                translated = engine.TranslateList(list(s["srt_generator"]))
                with open(os.path.join(tgtFolder, s['filename']), "w") as out:
                    out.write(srt.compose(translated))
            except Exception as e:
                print(f"Error occurred {e} on file {s['filename']}")
            finally:
                fbar.update(1)

if __name__ == "__main__":
    config = GetConfig()
    if config is None:
        raise SystemExit()
    engine = GetEngine(config)
    if engine is None:
        raise SystemExit()
    srts = parseSrt(config)
    DoTranslate(engine, srts, config.tgtFolder)
