import distributor
import handler

class MockDistributor(distributor.Distributor):
    def connect(self, handler: handler.Handler): self.handler = handler
    def distribute(self, package): self.handler.onReceivedPackage(package)
    def disconnect(self): pass
