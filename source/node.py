import strategy
import json
import abc
import distributor
import handler

class Node(handler.Handler): 
    def __init__(self, distributor: distributor.Distributor):
        self.distributor = distributor

    def onReceivedPackage(self, package):
        self.distributor.distribute(self.handlePackage(package))

    @abc.abstractmethod
    def handlePackage(self, package): pass
    

class StrategyNode(Node):
    def __init__(self, distributor: distributor.Distributor, strategy: strategy.Strategy):
        super(StrategyNode, self).__init__(distributor)
        self.strategy = strategy

    def handlePackage(self, package):
        package["values"] = self.strategy.execute(input = package["values"])
        package.setdefault("strategies", []).append(self.strategy.__class__.__name__)
        return package

class JsonLoadNode(Node):
    def handlePackage(self, package):
        return json.loads(package)

class JsonDumpNode(Node):
    def __init__(self, distributor: distributor.Distributor, jsonEncoder = None):
        super(JsonDumpNode, self).__init__(distributor)
        self.jsonEncoder = jsonEncoder

    def handlePackage(self, package):
        return json.dumps(package, cls = self.jsonEncoder)
