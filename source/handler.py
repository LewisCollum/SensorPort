import abc

class Handler(abc.ABC):
    @abc.abstractmethod
    def onReceivedPackage(self, package): pass

    @abc.abstractmethod
    def onConnected(self): pass
    
    @abc.abstractmethod
    def onDisconnected(self): pass
