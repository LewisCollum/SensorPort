
import unittest
import quaternion

class TestQuaternion(unittest.TestCase):

    def test_rotateListVector(self):
        self.quaternion = quaternion.Quaternion((0, 0, 0), 1)        

if __name__ == '__main__':
    unittest.main()
