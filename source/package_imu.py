import package as pk

class Vector3D(pk.PackageValue):
    @property
    def x(self):
        return self.values[0]
    
    @property
    def y(self):
        return self.values[1]
    
    @property
    def z(self):
        return self.values[2]
            
    @classmethod
    def fromComponents(cls, x, y, z):
        return cls.fromContainer(values = (x, y, z))

    def toTuple(self):
        return (self.x, self.y, self.z)
        
    
class Quaternion(pk.PackageValue):
    @property
    def vector(self):
        return self.values[0:3]

    @property
    def x(self):
        return self.values[0]
    
    @property
    def y(self):
        return self.values[1]
    
    @property
    def z(self):
        return self.values[2]

    @property
    def scalar(self):
        return self.values[3]
        
    @classmethod
    def fromComponents(cls, x, y, z, scalar):
        return cls.fromContainer(values = (x, y, z, scalar))

    def toTuple(self):
        return (self.x, self.y, self.z, self.scalar)
