import unittest
import distributor
import mock_distributor
import mock_handler

class TestSingleDistributor(unittest.TestCase):
    def setUp(self):
        self.handler = mock_handler.MockHandler()
        self.distributor = distributor.SingleDistributor()
        self.distributor.connect(self.handler)
        
    def test_distributeToSingleHandler(self):
        expected = "abc"
        self.distributor.distribute(expected)
        actual = self.handler.package
        self.assertEqual(actual, expected)
        
    def test_connectToHandler(self):
        self.assertTrue(self.handler.wasConnected)
        
    def test_disconnectFromHandler(self):
        self.distributor.disconnect()
        self.assertTrue(self.handler.wasDisconnected)


class TestMultiDistributor(unittest.TestCase):
    def setUp(self):
        self.handlerA = mock_handler.MockHandler()
        self.handlerB = mock_handler.MockHandler()
        self.distributor = distributor.MultiDistributor()
        self.distributor.connect(self.handlerA)
        self.distributor.connect(self.handlerB)
        
    def test_distributeToMultipleHandlers(self):
        expected = "abc"
        self.distributor.distribute(expected)

        actualA = self.handlerA.package
        actualB = self.handlerB.package
        
        self.assertEqual(actualA, expected)
        self.assertEqual(actualB, expected)
        
    def test_connectToHandlers(self):
        self.assertTrue(self.handlerA.wasConnected)
        self.assertTrue(self.handlerB.wasConnected)
        
    def test_disconnectFromHandlers(self):
        self.distributor.disconnect()

        self.assertTrue(self.handlerA.wasDisconnected)
        self.assertTrue(self.handlerB.wasDisconnected)
        
if __name__ == '__main__':
    unittest.main()
