from receiver import Receiver
from handler import Handler
from distributor import Distributor

class Node(Receiver):
    def __init__(self, handler: Handler, distributor: Distributor):
        self.handler = Handler
        self.distributor = Distributor

    def onReceivedPackage(self, package):
        self.distributor.distribute(self.handler.handle(package))
