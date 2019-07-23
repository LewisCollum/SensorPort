import unittest
import associative_distributor
import mock_handler
import mock_package as mock_pk
import package as pk

class TestKeyDistributor(unittest.TestCase):
    def setUp(self):
        self.distributor = associative_distributor.KeyDistributor()
        self.handler = mock_handler.MockHandler()

        self.distributor.connect("A", self.handler)
        
    def test_distributeToMultipleHandlers(self):
        expectedPackage = pk.Package.make(name = "A")
        self.distributor.distribute(expectedPackage)

        actualPackage = self.handler.package
        
        self.assertEqual(actualPackage, expectedPackage)
        
    def test_connectToHandlers(self):
        self.assertTrue(self.handler.wasConnected)
        
    def test_disconnectFromHandlers(self):
        self.distributor.disconnect()

        self.assertTrue(self.handler.wasDisconnected)


if __name__ == '__main__':
    unittest.main()
