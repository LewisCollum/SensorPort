from joining_node import JoiningNode
import distributor
import package as pk

class MockAddJoiningNode(JoiningNode):
    def join(self, joinables): return pk.Package.make(name = None, value = sum(package.value for package in joinables.values()))
