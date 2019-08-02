from receiver import Receiver
from distributor import Distributor
from distributor import NamingDistributor

class MockDistributor(Distributor):
    def distribute(self, package):
        self.receiver.onReceivedPackage(package)

    def connect(self, receiver: Receiver):
        self.receiver = receiver

    def disconnect(self): pass


class MockNamingDistributor(NamingDistributor):
    def __init__(self):
        self.receiver = {}
    
    def distribute(self, package):
        self.receiver[package.name].onReceivedPackage(package)
        
    def connect(self, name: str, receiver: Receiver):
        self.receiver[name] = receiver
        
    def disconnect(self): pass
