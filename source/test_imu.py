
import unittest
import imu
import mock_distributor as md
import mock_receiver as mr
import package_imu as pk_imu
import package as pk

class TestQuaternionVectorJoiningNode(unittest.TestCase):
    def setUp(self):
        self.vectorDistributor = md.MockDistributor()
        self.quaternionDistributor = md.MockDistributor()
        self.joiner = imu.QuaternionVectorJoiningNode.makeFromNames(
            quaternionName = "Quaternion",
            vectorName = "Vector")
        self.receiver = mr.MockReceiver()

        self.quaternionDistributor.connect(self.joiner)
        self.vectorDistributor.connect(self.joiner)
        self.joiner.connect(self.receiver)
        
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
