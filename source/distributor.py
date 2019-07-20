import abc
import handler

class Distributor(abc.ABC):
    @abc.abstractmethod
    def distribute(self, package): pass
    
    @abc.abstractmethod
    def connect(self, handler: handler.Handler): pass

    @abc.abstractmethod
    def disconnect(self): pass

    
class MultiDistributor(Distributor):
    def __init__(self):
        self.handlers = []

    def connect(self, handler: handler.Handler):
        self.handlers.append(handler)
        handler.onConnected()
        
    def distribute(self, package):
        for handler in self.handlers:
            handler.onReceivedPackage(package)

    def disconnect(self):
        for handler in self.handlers:
            handler.onDisconnected()
        self.handlers.clear()


class SingleDistributor(Distributor):
    def connect(self, handler: handler.Handler):
        self.handler = handler
        self.handler.onConnected()
        
    def distribute(self, package):
        self.handler.onReceivedPackage(package)

    def disconnect(self):
        self.handler.onDisconnected()
        self.handler = None


class AssociativeDistributor(Distributor):
    @abc.abstractmethod
    def connect(self, name: str, handler: handler.Handler): pass
    
        
class KeyDistributor(AssociativeDistributor):
    def __init__(self):
        self.handlers = {}

    def connect(self, name: str, handler: handler.Handler):
        self.handlers.setdefault(name, []).append(handler)
        handler.onConnected()
        
    def distribute(self, package):
        for handler in self.handlers[package["name"]]:
            handler.onReceivedPackage(package)

    def disconnect(self):
        for name, handlers in self.handlers.items():
            for handler in handlers:
                handler.onDisconnected()
        self.handlers.clear()
