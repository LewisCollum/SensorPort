import unittest
from packaging_handler import PackagingHandler
import package as pk

class TestPackagingHandler(unittest.TestCase):
    def setUp(self):
        self.packagingHandler = PackagingHandler()

    def test_dictToPackage_namesEqual(self):
        expected = pk.Package.make(name = "A")
        actual = self.packagingHandler.handle({"name": "A"})

        self.assertEqual(actual.name, expected.name)

    def test_dictToPackage_valuesEqual(self):
        expected = pk.Package.make(value = pk.PackageValue.fromContainer((1, 2)))
        actual = self.packagingHandler.handle({"value": (1,2)})

        self.assertEqual(actual.value, expected.value)
