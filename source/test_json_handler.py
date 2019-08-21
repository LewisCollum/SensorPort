import unittest
from json_handler import JsonLoadHandler, JsonDumpHandler
import mock_distributor as md
import mock_receiver as mr

class TestJsonLoadHandler(unittest.TestCase):
    def setUp(self):
        self.jsonLoadHandler = JsonLoadHandler()
        
    def test_load(self):
        expected = {"A": 0}
        actual = self.jsonLoadHandler.handle('{"A": 0}')
        
        self.assertEqual(actual, expected)
        
class TestJsonDumpHandler(unittest.TestCase):
    def setUp(self):
        self.jsonDumpHandler = JsonDumpHandler()
        
    def test_load(self):
        expected = '{"A": 0}'
        actual = self.jsonDumpHandler.handle({"A": 0})

        self.assertEqual(actual, expected)
