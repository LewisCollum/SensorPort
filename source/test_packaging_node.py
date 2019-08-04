
import unittest
from packaging_node import PackagingNode
import mock_distributor as md
import mock_receiver as mr
import package as pk

class TestPackagingNode(unittest.TestCase):
    def setUp(self):
        self.distributor = md.MockDistributor()
        self.unit = PackagingNode()
        self.receiver = mr.MockReceiver()

        self.distributor.connect(self.unit)
        self.unit.connect(self.receiver)

    def test_dictToPackage_namesEqual(self):
        expected = pk.Package.make(name = "A")
        self.distributor.distribute({"name": "A"})

        actual = self.receiver.package

        self.assertEqual(actual.name, expected.name)

    def test_dictToPackage_valuesEqual(self):
        expected = pk.Package.make(value = pk.PackageValue.fromContainer((1, 2)))
        self.distributor.distribute({"value": (1,2)})

        actual = self.receiver.package

        self.assertEqual(actual.value, expected.value)
