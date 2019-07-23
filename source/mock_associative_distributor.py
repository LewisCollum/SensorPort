import associative_distributor
import handler
import package as pk

class MockAssociativeDistributor(associative_distributor.AssociativeDistributor):
    def __init__(self): self.handler = {}
    def connect(self, name: str, handler: handler.Handler): self.handler[name] = handler
    def distribute(self, package): self.handler[package.name].onReceivedPackage(package)
    def disconnect(self): pass
