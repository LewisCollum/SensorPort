import joiner
import distributor
import package as pk

class MockAddJoiner(joiner.Joiner):
    def join(self, joinables): return pk.Package.make(name = self.name, value = sum(package.value for package in joinables.values()))
    def onConnected(self): pass
    def onDisconnected(self): pass
