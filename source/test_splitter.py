import unittest
import splitter
import mock_associative_distributor as mock_ad
import mock_distributor as mock_d
import mock_handler
import package as pk
import mock_package as mock_pk

class TestSplitter(unittest.TestCase):
    def setUp(self):
        self.A = mock_handler.MockHandler()
        self.B = mock_handler.MockHandler()

        self.distributor = mock_ad.MockAssociativeDistributor()
        self.distributor.connect("A", self.A)
        self.distributor.connect("B", self.B)

        self.packageDistributor = mock_d.MockDistributor()
        self.splitter = splitter.Splitter(self.distributor)
        self.packageDistributor.connect(self.splitter)        
        
    def test_distribute_packageSentToANotB(self):
        packageForA = pk.Package.make(name = "A")
        self.packageDistributor.distribute(packageForA)

        self.assertEqual(packageForA, self.A.package)
        self.assertEqual(None, self.B.package) 

if __name__ == '__main__':
    unittest.main()
