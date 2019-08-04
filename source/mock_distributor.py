
from distributor_interface import Distributor
from receiver_interface import Receiver

class MockDistributor(Distributor):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver
        
    def distribute(self, package):
        self.receiver.onReceivedPackage(package)

from receiver import Receiver
from distributor import Distributor
from distributor import NamingDistributor

class MockDistributor(Distributor):
    def distribute(self, package):
        self.receiver.onReceivedPackage(package)

    def connectToReceiver(self, receiver: Receiver):
        self.receiver = receiver

    def disconnect(self): pass


class MockNamingDistributor(NamingDistributor):
    def __init__(self):
        self.receiver = {}
    
    def distribute(self, package):
        self.receiver[package.name].onReceivedPackage(package)
        
    def connectToReceiver(self, name: str, receiver: Receiver):
        self.receiver[name] = receiver
        
    def disconnect(self): pass
