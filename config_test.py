import unittest

from config.config import GetConfig, Config

class TestConfig(unittest.TestCase):
    def test_get_config(self):
        c = GetConfig()
        print(c)
