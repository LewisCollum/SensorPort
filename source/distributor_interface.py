
import abc

class Distributor(abc.ABC):
    @abc.abstractmethod
    def distributePackage(self, package): pass
