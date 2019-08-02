import abc
from receiver import Receiver
from connector import Connector
from distributor import Distributor

class HandlingNode(Receiver):
    @abc.abstractmethod
    def handle(self, package): pass

    def setDistributor(self, distributor: Distributor):
        self.distributor = distributor
    
    def onReceivedPackage(self, package):
        self.distributor.distribute(self.handle(package))
