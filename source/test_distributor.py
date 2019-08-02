import unittest
import distributor as d
import mock_receiver as mh
import package as pk

class TestSingleDistributor(unittest.TestCase):
    def setUp(self):
        self.receiver = mh.MockReceiver()
        self.distributor = d.SingleDistributor()
        self.distributor.connect(self.receiver)
        
    def test_distributeToSingleReceiver(self):
        expected = "abc"
        self.distributor.distribute(expected)
        actual = self.receiver.package

        self.assertEqual(actual, expected)
        

class TestMultiDistributor(unittest.TestCase):
    def setUp(self):
        self.receiverA = mh.MockReceiver()
        self.receiverB = mh.MockReceiver()
        self.distributor = d.MultiDistributor()
        self.distributor.connect(self.receiverA)
        self.distributor.connect(self.receiverB)
        
    def test_distributeToReceiverA(self):
        expected = "abc"
        self.distributor.distribute(expected)
        actualA = self.receiverA.package
        
        self.assertEqual(actualA, expected)

    def test_distributeToReceiverB(self):
        expected = "abc"
        self.distributor.distribute(expected)
        actualB = self.receiverB.package
        
        self.assertEqual(actualB, expected)


class TestNamingDistributor(unittest.TestCase):
    def setUp(self):
        self.distributor = d.NamingDistributor()
        self.receiver = mh.MockReceiver()

        self.distributor.connect("A", self.receiver)
        
    def test_distributeToReceiverA(self):
        expectedPackage = pk.Package.make(name = "A")
        self.distributor.distribute(expectedPackage)

        actualPackage = self.receiver.package
        
        self.assertEqual(actualPackage, expectedPackage)
        
        
if __name__ == '__main__':
    unittest.main()
