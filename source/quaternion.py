
import copy

class Quaternion:
    normalizingStrategy = None
    
    def __init__(self, vector, scalar):        
        self.vector = vector
        self.scalar = scalar
        
    def rotateVector(self, vector):
        quaternionFromVector = Quaternion(vector=vector, scalar=0)
        resultantQuaternion = self * quaternionFromVector * self.conjugate()
        return resultantQuaternion.vector
        
    def conjugate(self):
        conjugatedVector = self.vector.__class__((-i for i in self.vector))
        return Quaternion(vector=conjugatedVector, scalar=self.scalar)
        
    def __mul__(self, other):
        b1, c1, d1 = self.vector
        a1 = self.scalar
        b2, c2, d2 = other.vector
        a2 = other.scalar

        w = a1*a2 - b1*b2 - c1*c2 - d1*d2
        x = a1*b2 + b1*a2 + c1*d2 - d1*c2
        y = a1*c2 - b1*d2 + c1*a2 + d1*b2
        z = a1*d2 + b1*c2 - c1*b2 + d1*a2
        return Quaternion(vector=self.vector.__class__([x, y, z]), scalar=w)
    
    def normalize(self):
        Quaternion.normalizingStrategy(self)
