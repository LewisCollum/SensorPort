import abc
from receiver import Receiver

class Connector:
    @abc.abstractmethod
    def connect(self, receiver: Receiver): pass

    @abc.abstractmethod
    def disconnect(self): pass

    
class NamingConnector:
    @abc.abstractmethod
    def connect(self, name: str, receiver: Receiver): pass
    
    @abc.abstractmethod
    def disconnect(self, name: str): pass
