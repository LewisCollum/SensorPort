import unittest
from json_node import JsonLoadNode, JsonDumpNode
import mock_distributor as md
import mock_receiver as mr

class TestJsonLoadNode(unittest.TestCase):
    def setUp(self):
        self.distributor = md.MockDistributor()
        self.jsonLoadDistributor = md.MockDistributor()
        self.jsonLoadNode = JsonLoadNode()
        self.jsonLoadNode.setDistributor(self.jsonLoadDistributor)
        self.receiver = mr.MockReceiver()

        self.distributor.connect(self.jsonLoadNode)
        self.jsonLoadDistributor.connect(self.receiver)
        
    def test_load(self):
        expected = {"A": 0}
        
        self.distributor.distribute('{"A": 0}')
        actual = self.receiver.package

        self.assertEqual(actual, expected)

        
class TestJsonDumpNode(unittest.TestCase):
    def setUp(self):
        self.distributor = md.MockDistributor()
        self.jsonDumpDistributor = md.MockDistributor()
        self.jsonDumpNode = JsonDumpNode()
        self.jsonDumpNode.setDistributor(self.jsonDumpDistributor)
        self.receiver = mr.MockReceiver()

        self.distributor.connect(self.jsonDumpNode)
        self.jsonDumpDistributor.connect(self.receiver)
        
    def test_load(self):
        expected = '{"A": 0}'
        
        self.distributor.distribute({"A": 0})
        actual = self.receiver.package

        self.assertEqual(actual, expected)
