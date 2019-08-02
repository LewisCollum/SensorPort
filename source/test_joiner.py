import unittest
import mock_joiner as mj
import mock_distributor as md
import mock_receiver as mr
import package as pk

class TestJoiningNode(unittest.TestCase):
    def setUp(self):
        self.distributorA = md.MockDistributor()
        self.distributorB = md.MockDistributor()
        self.adder = mj.MockAddJoiningNode("A", "B")
        self.packageReceiver = mr.MockReceiver()

        self.distributorA.connect(self.adder)
        self.distributorB.connect(self.adder)
        self.adder.connect(self.packageReceiver)

    def test_receiverReceivesFusedJoiningNodeOutput(self):
        packageA = pk.Package.make(name = "A", value = 1)
        packageB = pk.Package.make(name = "B", value = 2)
        expectedSum = packageA.value + packageB.value
        self.distributorA.distribute(packageA)
        self.distributorB.distribute(packageB)

        self.assertEqual(self.packageReceiver.package.value, expectedSum)

if __name__ == '__main__':
    unittest.main()
