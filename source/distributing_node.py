
import abc
from receiver import Receiver
from connector import Connector
from distributor import Distributor

class DistributionNode(Receiver):
    def __init__(self, distributor: Distributor):
        self.distributor = distributor

    def onReceivedPackage(self, package):
        self.distributor.distribute(package)
