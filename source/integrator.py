import pair
import package as pk
from handler import Handler

class Integrator(Handler):
    def __init__(self, name: str = None):
        self.name = name
        self.time = pair.Pair()
        self.value = pair.Pair()
        
    def handle(self, package):
        self.time.shift(package.timestamp)
        self.value.shift(package.value)
        if self.time.previous != None:
            value = self.value.previous + self.value.current*self.time.difference
            return pk.Package.make(self.name, value, self.time.current)
