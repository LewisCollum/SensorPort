
import unittest
from connection_distributor import SingleConnectionDistributor, MultiConnectionDistributor, NamedConnectionDistributor
import mock_receiver as mh
import package as pk

class TestSingleConnectionDistributor(unittest.TestCase):
    def setUp(self):
        self.distributor = SingleConnectionDistributor()
        self.receiver = mh.MockReceiver()
        self.distributor.connectToReceiver(self.receiver)
        
    def test_distributeToSingleReceiver(self):
        expected = "abc"
        self.distributor.distributePackage(expected)
        actual = self.receiver.package

        self.assertEqual(actual, expected)
        

class TestMultiConnectionDistributor(unittest.TestCase):
    def setUp(self):
        self.receiverA = mh.MockReceiver()
        self.receiverB = mh.MockReceiver()
        self.distributor = MultiConnectionDistributor()
        self.distributor.connectToReceiver(self.receiverA)
        self.distributor.connectToReceiver(self.receiverB)
    
    def test_distributeToReceiverA(self):
        expected = "abc"
        self.distributor.distributePackage(expected)
        actualA = self.receiverA.package
        
        self.assertEqual(actualA, expected)

    def test_distributeToReceiverB(self):
        expected = "abc"
        self.distributor.distributePackage(expected)
        actualB = self.receiverB.package
        
        self.assertEqual(actualB, expected)


class TestNamedConnectionDistributor(unittest.TestCase):
    def setUp(self):
        self.distributor = NamedConnectionDistributor()
        self.receiver = mh.MockReceiver()

        self.distributor.connectByNameToReceiver("A", self.receiver)
        
    def test_distributeToReceiverA(self):
        expectedPackage = pk.Package.make(name = "A")
        self.distributor.distributePackage(expectedPackage)

        actualPackage = self.receiver.package
        
        self.assertEqual(actualPackage, expectedPackage)
        
        
if __name__ == '__main__':
    unittest.main()
