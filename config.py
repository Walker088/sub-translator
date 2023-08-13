import yaml

class Config(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = u'!Config'
    def __init__(
        self,
        model: str,
        srcLang: str,
        tgtLang: str,
        maxLength: int,
        tgtFolder: str,
        destFolder: str,
    ) -> None:
        self.model = model
        self.srcLang = srcLang
        self.tgtLang = tgtLang
        self.maxLength = maxLength
        self.tgtFolder = tgtFolder
        self.destFolder = destFolder
    
    def __repr__(self):
        return "%s(model=%r, srcLang=%r, tgtLang=%r, maxLength=%r, tgtFolder=%r, destFolder=%r)" % (
            self.__class__.__name__,
            self.model,
            self.srcLang,
            self.tgtLang,
            self.maxLength,
            self.tgtFolder,
            self.destFolder
        )
    
    @classmethod
    def from_yaml(cls, loader, node):
        values = loader.construct_mapping(node, deep=True)
        model = values["languageEngine"]["model"]
        srcLang = values["languageEngine"]["srcLang"]
        tgtLang = values["languageEngine"]["tgtLang"]
        maxLength = values["languageEngine"]["maxLength"]
        tgtFolder = values["translator"]["tgtFolder"]
        destFolder = values["translator"]["destFolder"]
        return cls(
            model, srcLang, tgtLang,
            maxLength, tgtFolder, destFolder
        )

def GetConfig() -> Config | None:
    with open("config.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            print(e)
            return None
