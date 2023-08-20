import asyncio
from time import sleep
from tqdm import tqdm
import srt
import os

from config.config import GetConfig, GetEngine, Config
from engine.engine import Engine

async def DoTranslate(c: Config, engine: Engine):
    files = os.listdir(c.srcFolder)
    with tqdm(total=len(files)) as fbar:
        for filename in files:
            try:
                fbar.set_description(f"file: {filename}")
                if not filename.endswith(".srt"):
                    continue
                parsedSrt = None
                with open(os.path.join(c.srcFolder, filename)) as inp:
                    parsedSrt = list(srt.parse(inp.read()))

                if parsedSrt is None:
                    print(f"Failed to parse {filename}")
                    continue
                
                async def _translate(s: srt.Subtitle):
                    s.content = engine.Translate(s.content)
                    return s
                jobs = [_translate(s) for s in parsedSrt]
                for job in tqdm(asyncio.as_completed(jobs), desc="translating"):
                    result = await job
                    parsedSrt[result.index-1] = result

                with open(os.path.join(c.tgtFolder, filename), "w") as out:
                    out.write(srt.compose(parsedSrt))
            except Exception as e:
                print(f"Error occurred {e} on file {filename}")
            finally:
                fbar.update(1)

if __name__ == "__main__":
    config = GetConfig()
    if config is None:
        raise SystemExit()
    engine = GetEngine(config)
    if engine is None:
        raise SystemExit()
    asyncio.run(DoTranslate(config, engine))

