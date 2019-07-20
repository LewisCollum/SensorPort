import distributor
import handler

class MockDistributor(distributor.Distributor):
    def connect(self, handler: handler.Handler): self.handler = handler
    def distribute(self, package): self.handler.onReceivedPackage(package)
    def disconnect(self): pass

class MockAssociativeDistributor(distributor.AssociativeDistributor):
    def __init__(self): self.handler = {}
    def connect(self, name: str, handler: handler.Handler): self.handler[name] = handler
    def distribute(self, package): self.handler[package["name"]].onReceivedPackage(package)
    def disconnect(self): pass
