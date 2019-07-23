import distributor
import handler
import abc
import package as pk

class AssociativeDistributor(distributor.Distributor):
    @abc.abstractmethod
    def connect(self, name: str, handler: handler.Handler): pass
    
        
class KeyDistributor(AssociativeDistributor):
    def __init__(self):
        self.handlers = {}

    def connect(self, name: str, handler: handler.Handler):
        self.handlers.setdefault(name, []).append(handler)
        handler.onConnected()
        
    def distribute(self, package):
        for handler in self.handlers[package.name]:
            handler.onReceivedPackage(package)

    def disconnect(self):
        for name, handlers in self.handlers.items():
            for handler in handlers:
                handler.onDisconnected()
        self.handlers.clear()
