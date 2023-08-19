import unittest

from engine.google import GoogleTranslateEngine
from config.config import GetConfig

class TestGoogleTranslateEngine(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.config = GetConfig()
    
    def testTranslate(self):
        pass
        