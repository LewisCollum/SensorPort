from receiver import Receiver

class MockReceiver(Receiver):
    def __init__(self): self.package = None
    def onReceivedPackage(self, package): self.package = package
