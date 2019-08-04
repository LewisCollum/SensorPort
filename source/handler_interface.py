
import abc

class Handler(abc.ABC):
    @abstractmethod
    def handlePackage(self, package): pass
