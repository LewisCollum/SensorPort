import unittest
import mock_joiner
import mock_distributor as mock_d
import mock_handler
import mock_package as mock_pk
import package as pk

class TestJoiner(unittest.TestCase):
    def setUp(self):
        self.distributorA = mock_d.MockDistributor()
        self.distributorB = mock_d.MockDistributor()
        self.adderDistributor = mock_d.MockDistributor()
        self.adder = mock_joiner.MockAddJoiner(self.adderDistributor)
        self.adder.addJoinableNames("A", "B")
        self.packageReceiver = mock_handler.MockHandler()

        self.distributorA.connect(self.adder)
        self.distributorB.connect(self.adder)
        self.adderDistributor.connect(self.packageReceiver)

    def test_handlerReceivesFusedJoinerOutput(self):
        packageA = pk.Package.make(name = "A", value = 1)
        packageB = pk.Package.make(name = "B", value = 2)
        expectedSum = packageA.value + packageB.value
        self.distributorA.distribute(packageA)
        self.distributorB.distribute(packageB)

        self.assertEqual(self.packageReceiver.package.value, expectedSum)

if __name__ == '__main__':
    unittest.main()
