import observer
import categorizer as cat
import strategy
import json

class CategoryNode(observer.Observer, observer.Subject):
    def __init__(self, categorizer: cat.Categorizer):
        super(CategoryNode, self).__init__()
        self.categorizer = categorizer
        
    def onUpdateFromSubject(self, package: str):
        self.categorizer.categorizeLine(line = json.loads(package))

    def onCloseFromSubject(self):
        self.notifyObservers(self.categorizer.categorized)

class StrategyNode(observer.Observer, observer.Subject):
    def __init__(self, strategy: strategy.Strategy):
        super(StrategyNode, self).__init__()
        self.strategy = strategy

    def onUpdateFromSubject(self, package):
        self.package = package
        self.package["values"] = self.strategy.execute(input = package["values"])
        package.setdefault("strategies", []).append(self.strategy.__class__.__name__)
        self.notifyObservers(self.package)

class JsonLoadNode(observer.Observer, observer.Subject):
    def onUpdateFromSubject(self, package):
        self.notifyObservers(json.loads(package))

class JsonDumpNode(observer.Observer, observer.Subject):
    def __init__(self, jsonEncoder = None):
        super(JsonDumpNode, self).__init__()
        self.jsonEncoder = jsonEncoder

    def onUpdateFromSubject(self, package):
        self.notifyObservers(package=json.dumps(package, cls = self.jsonEncoder))
