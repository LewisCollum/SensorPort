import abc

class Receiver:
    @abc.abstractmethod
    def onReceivedPackage(self, package): pass
