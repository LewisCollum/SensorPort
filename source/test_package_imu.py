
import package as pk
import package_imu as pk_imu
import unittest

class TestVector3D(unittest.TestCase):
    def setUp(self):
        self.expected = (1, 2, 3)
        
    def test_fromContainer_vectorMatches(self):
        vector = pk_imu.Vector3D.fromContainer(self.expected)

        self.assertEqual(self.expected, vector.values)

    def test_fromComponents_vectorMatches(self):
        x, y, z = self.expected
        vector = pk_imu.Vector3D.fromComponents(x, y, z)

        self.assertEqual(self.expected, vector.values)


class TestQuaternion(unittest.TestCase):
    def setUp(self):
        self.expected = (1, 2, 3, 0)

    def test_fromContainer_valuesMatch(self):
        quaternion = pk_imu.Quaternion.fromContainer(self.expected)

        self.assertEqual(self.expected, quaternion.values)
        
    def test_fromComponents_valuesMatch(self):
        x, y, z, scalar = self.expected
        quaternion = pk_imu.Quaternion.fromComponents(x, y, z, scalar)

        self.assertEqual(self.expected, quaternion.values)

if __name__ == '__main__':
    unittest.main()
