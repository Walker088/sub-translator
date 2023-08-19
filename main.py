from tqdm import tqdm
import srt
import os

from config.config import GetConfig, GetEngine, Config
from engine.engine import Engine

def DoTranslate(c: Config, engine: Engine):
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

                for entry in tqdm(parsedSrt, desc="translating"):
                    entry.content = engine.Translate(entry.content)
                with open(os.path.join(c.tgtFolder, filename), "w") as out:
                    out.write(srt.compose(parsedSrt))
            except Exception as e:
                print(f"Error occurred {e} on file {filename}")
            finally:
                fbar.update(1/len(files))

if __name__ == "__main__":
    config = GetConfig()
    if config is None:
        raise SystemExit()
    engine = GetEngine(config)
    if engine is None:
        raise SystemExit()
    DoTranslate(config, engine)

