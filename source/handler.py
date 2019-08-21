import abc

class Handler(abc.ABC):
    @abc.abstractmethod
    def handle(self, package): pass
