import joiner
import distributor
import quaternion as quat
import package as pk
import package_imu as pk_imu

class QuaternionVectorJoiner(joiner.Joiner):
    def join(self, joinables):
        quaternion = quat.Quaternion(
            joinables[self.quaternionName].value.vector,
            joinables[self.quaternionName].value.scalar)

        vector = quaternion.rotateVector(joinables[self.vectorName].value.values)
        value = pk_imu.Vector3D.fromContainer(vector)
        timestamp = int((joinables[self.quaternionName].timestamp + joinables[self.quaternionName].timestamp)/2)
        return pk.Package.make(name=self.name, value=value, timestamp=timestamp)
    
    def addQuaternionName(self, name: str):
        self.quaternionName = name
        self.addJoinableName(name)

    def addVectorName(self, name: str):
        self.vectorName = name
        self.addJoinableName(name)

    def onConnected(self): pass
    def onDisconnected(self): pass
