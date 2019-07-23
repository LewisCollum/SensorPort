import node
import abc
import distributor as d


class Joiner(node.Node):
    def __init__(self, distributor: d.Distributor):
        super(Joiner, self).__init__(distributor)
        self.joinables = {}
        self.name = None
        
    def handlePackage(self, package):
        joined = self.join(self.joinables)
        self.joinables = dict.fromkeys(self.joinables)
        return joined

    #TODO REMOVE HACK 
    def onReceivedPackage(self, package):
        self.joinables[package.name] = package
        if None not in self.joinables.values(): 
            self.distributor.distribute(self.handlePackage(package))
    
    def addJoinableName(self, name: str):
        self.joinables[name] = None

    def addJoinableNames(self, *names):
        for name in names:
            self.joinables[name] = None
        
    def removeJoinableName(self, name: str):
        del self.joinables[name]

    @abc.abstractmethod
    def join(self, joinables: dict): pass
