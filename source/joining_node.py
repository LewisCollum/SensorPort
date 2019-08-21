import abc
import distributor as d
from connector import Connector
from receiver import Receiver
import package as pk

class JoiningNode(Receiver):
    def __init__(self, *joinableNames):
        self.joinables = dict.fromkeys(joinableNames)
        self.distributor = d.SingleDistributor()

    @abc.abstractmethod
    def join(self, joinables: dict): pass
        
    def onReceivedPackage(self, package):
        self.setJoinablePackage(package)
        if self.hasPackageForEachJoinable():
            joinedPackage = self.join(self.joinables)
            self.distributor.distribute(joinedPackage)        
            self.clearJoinablePackages()

    def setJoinablePackage(self, package):
        self.joinables[pk.PackageConfig.nameFromDict(package)] = package
            
    def hasPackageForEachJoinable(self):
        return None not in self.joinables.values()        
        
    def clearJoinablePackages(self):
        self.joinables = dict.fromkeys(self.joinables)

    def connect(self, receiver):
        self.distributor.connect(receiver)

    def disconnect(self):
        self.distributor.disconnect()
