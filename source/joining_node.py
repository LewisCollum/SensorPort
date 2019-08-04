
import abc
import distributor as d
from connector import Connector
from receiver import Receiver
import package as pk

class JoiningNode(Receiver, Connector):
    def __init__(self, *joinableNames):
        self.joinables = dict.fromkeys(joinableNames)

    @abc.abstractmethod
    def join(self, joinables: dict): pass
        
    def onReceivedPackage(self, package):
        self.setJoinablePackage(package)
        if self.hasPackageForEachJoinable():
            self.sendJoinedPackageToNextReceiver()
            self.clearJoinablePackages()

    def setJoinablePackage(self, package):
        self.joinables[pk.PackageConfig.nameFromDict(package)] = package

    def sendJoinedPackageToNextReceiver(self):
        joinedPackage = self.join(self.joinables)
        self.nextReceiver.onReceivedPackage(joinedPackage)        
            
    def hasPackageForEachJoinable(self):
        return None not in self.joinables.values()        
        
    def clearJoinablePackages(self):
        self.joinables = dict.fromkeys(self.joinables)

    def connectToReceiver(self, receiver):
        self.nextReceiver = receiver

    def disconnect(self):
        self.nextReceiver = None
