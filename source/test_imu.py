import unittest
import imu
import mock_distributor
import mock_handler
import package_imu as pk_imu
import package as pk

class TestQuaternionVectorJoiner(unittest.TestCase):
    def setUp(self):
        self.vectorDistributor = mock_distributor.MockDistributor()
        self.quaternionDistributor = mock_distributor.MockDistributor()
        self.joinerDistributor = mock_distributor.MockDistributor()
        self.joiner = imu.QuaternionVectorJoiner(self.joinerDistributor)
        self.receiver = mock_handler.MockHandler()

        self.joiner.addQuaternionName("Quaternion")
        self.quaternionDistributor.connect(self.joiner)
        self.joiner.addVectorName("Vector")
        self.vectorDistributor.connect(self.joiner)
        self.joinerDistributor.connect(self.receiver)
        
    def test_receivedRotatedVector(self):
        vectorPackage = pk.Package.make(
            name="Vector",
            value=pk_imu.Vector3D.fromComponents(x=1,y=0,z=0),
            timestamp=1)
        quaternionPackage = pk.Package.make(
            name="Quaternion",
            value=pk_imu.Quaternion.fromComponents(x=0,y=0,z=1,scalar=0),
            timestamp=3)
        self.vectorDistributor.distribute(vectorPackage)
        self.quaternionDistributor.distribute(quaternionPackage)

        expected = pk_imu.Vector3D.fromComponents(x=-1,y=0,z=0).values
        actual = self.receiver.package.value.values
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
