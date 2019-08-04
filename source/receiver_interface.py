
import abc

class Receiver(abc.ABC):
    @abc.abstractmethod
    def onReceivedPackage(self, package): pass
