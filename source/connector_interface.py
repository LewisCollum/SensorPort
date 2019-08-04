
import abc
from receiver_interface import Receiver

class SingleConnector(abc.ABC):
    @abc.abstractmethod
    def connectToReceiver(self, receiver: Receiver): pass

    @abc.abstractmethod
    def disconnectFromReceiver(self): pass

    
class MultiConnector(abc.ABC):
    @abc.abstractmethod
    def connectToReceiver(self, receiver: Receiver): pass

    @abc.abstractmethod
    def disconnectFromReceiver(self, receiver: Receiver): pass

    @abc.abstractmethod
    def disconnectFromAllReceivers(self): pass

    
class NameConnector(abc.ABC):
    @abc.abstractmethod
    def connectByNameToReceiver(self, name: str, receiver: Receiver): pass

    @abc.abstractmethod
    def disconnectByNameFromReceiver(self, name: str): pass

    @abc.abstractmethod
    def disconnectFromAllReceivers(self): pass
