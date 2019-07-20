import node

class MockNode(node.Node):
    def handlePackage(self, package): return package
    def onConnected(self): pass
    def onDisconnected(self): pass
