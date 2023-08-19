import yaml

from engine.engine import Engine
from engine.nllb import NllbEngine
from engine.google import GoogleTranslateEngine

class TranslateEngine():
    name: str
    engine_configs: dict

    def __init__(self, name):
        self.name = name

class Config(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!Config'
    def __init__(
        self,
        engine: TranslateEngine,
        srcFolder: str,
        tgtFolder: str,
    ) -> None:
        self.engine = engine
        self.srcFolder = srcFolder
        self.tgtFolder = tgtFolder
    
    def __repr__(self):
        return "%s(engine=(%r, %r), srcFolder=%r, tgtFolder=%r)" % (
            self.__class__.__name__,
            self.engine.name,
            self.engine.engine_configs,
            self.srcFolder,
            self.tgtFolder
        )
    
    @classmethod
    def from_yaml(cls, loader, node):
        values = loader.construct_mapping(node, deep=True)
        engine = TranslateEngine(values["translator"]["engine"])
        if values["translator"]["engine"] == "nllb":
            engine.engine_configs = {
                "model": values["engines"]["nllb"]["model"],
                "srcLang": values["engines"]["nllb"]["srcLang"],
                "tgtLang": values["engines"]["nllb"]["tgtLang"],
                "maxLength": values["engines"]["nllb"]["maxLength"],
            }
        if values["translator"]["engine"] == "google":
            engine.engine_configs = {
                "projectId": values["engines"]["google"]["projectId"],
                "serviceAccKeyPath": values["engines"]["google"]["serviceAccKeyPath"],
                "srcLang": values["engines"]["google"]["srcLang"],
                "tgtLang": values["engines"]["google"]["tgtLang"],
            }
        srcFolder = values["translator"]["srcFolder"]
        tgtFolder = values["translator"]["tgtFolder"]
        return cls(
            engine,
            srcFolder,
            tgtFolder
        )

def GetConfig() -> Config | None:
    with open("config.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            print(e)
            return None

def GetEngine(c: Config) -> Engine | None:
    if c.engine.name == "nllb":
        return NllbEngine(c)
    if c.engine.name == "google":
        return GoogleTranslateEngine(c)
    return None
