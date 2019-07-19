class Observer:
    def onUpdateFromSubject(self, package):
        pass

    def onCloseFromSubject(self):
        pass

    
class Subject:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer: Observer):
        self.observers.append(observer)
        
    def notifyObservers(self, package):
        for observer in self.observers:
            observer.onUpdateFromSubject(package)

    def closeObservers(self):
        for observer in self.observers:
            observer.onCloseFromSubject()
