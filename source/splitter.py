import handler
import node
import distributor

class Splitter(node.AssociativeNode):
    def __init__(self, distributor: distributor.AssociativeDistributor):
        super(Splitter, self).__init__(distributor)

    def handlePackage(self, package): return package

# class Splitter(handler.Handler):
#     def __init__(self):
#         self.nodes = {}
        
#     def addNamedNode(self, name: str, node: node.Node):
#         self.nodes[name] = node

#     def hasNamedNode(self, name: str):
#         return name in self.nodes
        
#     def onReceivedPackage(self, package):
#         self.nodes[package["name"]].onReceivedPackage(package)
