from handling_node import HandlingNode
import pair
import package as pk

class Integrator(HandlingNode):
    def __init__(self, name: str = None):
        self.name = name
        self.time = pair.Pair()
        self.value = pair.Pair()
        
    def handle(self, package):
        self.time.shift(package.timestamp)
        self.value.shift(package.value.values)
        if self.time.previous != None:
            PackageValueClass = package.value.__class__
            value = self.value.previous + self.value.current*self.time.difference
            value = PackageValueClass(value)
            return pk.Package.make(self.name, value, self.time.current)
