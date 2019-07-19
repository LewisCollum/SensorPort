import observer
import copy

class Splitter(observer.Observer):
    def __init__(self):
        self.nodes = {}
        
    def addNamedNode(self, name: str, node):
        self.nodes[name] = node

    def hasNamedNode(self, name: str):
        return name in self.nodes
        
    def onUpdateFromSubject(self, package):
        self.nodes[package["name"]].onUpdateFromSubject(package)


class BranchBuilder:
    def __init__(self, 
        
class SplitterBranchReplicator(observer.Observer):
    def __init__(self, headOfBranch):
        self.head = headOfBranch
        self.splitter = Splitter()
        
    def onUpdateFromSubject(self, package):
        if not self.splitter.hasNamedNode(name=package["name"]):
            self.splitter.addNamedNode(name=package["name"], node=copy.copy(self.head))
