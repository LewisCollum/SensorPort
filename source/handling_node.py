
import abc
from receiver_interface import Receiver
from handler_interface import Handler
from distributor import Distributor

class HandlingNode(Receiver):
    def __init__(self, handler: Handler, distributor: Distributor):
        self.handler = handler
        self.distributor = distributor
            
    def onReceivedPackage(self, package):
        self.distributor.distribute(self.handle(package))
