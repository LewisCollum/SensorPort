
from distributor_interface import Distributor
from connector_interface import SingleConnector, MultiConnector, NameConnector
from receiver_interface import Receiver
import package as pk
            
class SingleConnectionDistributor(Distributor, SingleConnector):
    def distributePackage(self, package):
        self.receiver.onReceivedPackage(package)

    def connectToReceiver(self, receive: Receiver):
        self.receiver = receiver
        
    def disconnectFromReceiver(self):
        self.receiver = None
        
    
class MultiConnectionDistributor(Distributor, MultiConnector):
    def __init__(self):
        self.receivers = []

    def distributePackage(self, package):
        for receiver in self.receivers:
            receiver.onReceivedPackage(package)
        
    def connectToReceiver(self, receiver: Receiver):
        self.receivers.append(receiver)

    def disconnectFromReceiver(self, receiver: Receiver):
        self.receivers.remove(receiver)

    def disconnectFromAllReceivers(self):
        self.receivers.clear()

        
class NamedConnectionDistributor(Distributor, NameConnector):
    def __init__(self):
        self.receivers = {}

    def distributePackage(self, package):
        for receiver in self.receivers[pk.PackageConfig.nameFromDict(package)]:
            receiver.onReceivedPackage(package)
        
    def connectByNameToReceiver(self, name: str, receiver: Receiver):
        self.receivers.setdefault(name, []).append(receiver)

    def disconnectByNameFromReceiver(self, name: str):
        del self.receivers[name]
    
    def disconnectFromAllReceivers(self):
        self.receivers.clear()
