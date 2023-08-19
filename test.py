import re

from engine.google import GoogleTranslateEngine
from config.config import GetConfig

config = GetConfig()
if config is not None:
    engine = GoogleTranslateEngine(config)
    text = """
    Come on, Phil.
    Hurry up.
    """
    s = engine.Translate(text)
    print(s)
    
#regex = re.compile(r"([\w|\[, '-]*[?|.|!|\]])|(♪[\w|, ']*♪*)")
#matches = regex.finditer(text.replace("\n", " "))
#s = [match.group(0).strip() for match in matches]
#for match in matches:
#    s.append(match.group(0))


#sentences = [s.strip() for s in re.split(r"\.|\?", text.replace("\n", " ")) if len(s.strip()) > 0]
#print(sentences)

#sentences = [s.strip() for s in re.split(r"([.|?])", text) if len(s.strip()) > 0]
#print(sentences)

#translated = [engine.Translate(s) for s in sentences]
#print(translated)
#
#print(engine.Translate(text))
