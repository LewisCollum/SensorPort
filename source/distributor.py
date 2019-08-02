import abc
from connector import Connector
from connector import NamingConnector
from receiver import Receiver
import package as pk

class Distributor:
    @abc.abstractmethod
    def distribute(self, package): pass

            
class SingleDistributor(Distributor, Connector):
    def distribute(self, package):
        self.receiver.onReceivedPackage(package)

    def connect(self, receiver: Receiver):
        self.receiver = receiver
        
    def disconnect(self):
        self.receiver = None
        
    
class MultiDistributor(Distributor, Connector):
    def __init__(self):
        self.receivers = []

    def distribute(self, package):
        for receiver in self.receivers:
            receiver.onReceivedPackage(package)
        
    def connect(self, receiver: Receiver):
        self.receivers.append(receiver)

    def disconnect(self):
        self.receivers.clear()

        
class NamingDistributor(Distributor, NamingConnector):
    def __init__(self):
        self.receivers = {}

    def distribute(self, package):
        for receiver in self.receivers[pk.PackageConfig.nameFromDict(package)]:
            receiver.onReceivedPackage(package)
        
    def connect(self, name: str, receiver: Receiver):
        self.receivers.setdefault(name, []).append(receiver)
        
    def disconnect(self):
        self.receivers.clear()
