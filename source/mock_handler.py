import handler

class MockHandler(handler.Handler):
    def __init__(self):
        self.wasConnected = False
        self.wasDisconnected = False
        self.package = None
        
    def onReceivedPackage(self, package): self.package = package
    def onConnected(self): self.wasConnected = True
    def onDisconnected(self): self.wasDisconnected = True
