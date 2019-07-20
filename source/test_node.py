import unittest
import mock_distributor
import mock_node
import mock_handler

class TestNode(unittest.TestCase):
    def setUp(self):
        self.packageDistributor = mock_distributor.MockDistributor()
        self.nodeDistributor = mock_distributor.MockDistributor()
        self.node = mock_node.MockNode(distributor = self.nodeDistributor)
        self.packageReceiver = mock_handler.MockHandler()

        self.packageDistributor.connect(self.node)
        self.nodeDistributor.connect(self.packageReceiver)

    def test_packageReceivedFromDistributor(self):
        package = "abc"
        self.packageDistributor.distribute(package)

        actualPackage = self.packageReceiver.package
        
        self.assertEqual(actualPackage, package)

        
class TestAssociativeNode(unittest.TestCase):
    def setUp(self):
        self.packageDistributor = mock_distributor.MockDistributor()
        self.nodeDistributor = mock_distributor.MockAssociativeDistributor()
        self.node = mock_node.MockNode(distributor = self.nodeDistributor)
        self.packageReceiver = mock_handler.MockHandler()

        self.packageDistributor.connect(self.node)
        self.nodeDistributor.connect("A", self.packageReceiver)

    def test_packageReceivedFromDistributor(self):
        package = {"name": "A"}
        self.packageDistributor.distribute(package)

        actualPackage = self.packageReceiver.package
        
        self.assertEqual(actualPackage, package)


if __name__ == '__main__':
    unittest.main()
