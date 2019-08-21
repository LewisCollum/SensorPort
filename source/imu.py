from joining_node import JoiningNode
import distributor as d
import quaternion as quat
import package as pk
import package_imu as pk_imu

class QuaternionVectorJoiningNode(JoiningNode):
    def join(self, joinables):
        quaternionPackage = joinables[self.quaternionName]
        vectorPackage = joinables[self.vectorName]

        quaternion = quat.Quaternion(
	    quaternionPackage.value[0:3],
            quaternionPackage.value[3])

        vector = quaternion.rotateVector(vectorPackage.value)

        name = self.__class__.__name__
        value = pk_imu.Vector3D.fromContainer(vector)
        timestamp = int((quaternionPackage.timestamp + vectorPackage.timestamp)/2)

        return pk.Package.make(name, value, timestamp)

    @classmethod
    def makeFromNames(cls, quaternionName: str, vectorName: str):
        made = cls(quaternionName, vectorName)
        made.quaternionName = quaternionName
        made.vectorName = vectorName
        return made
