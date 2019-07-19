import sys
import observer

class TerminalSubject(observer.Subject):
    def __init__(self):
        super(TerminalSubject, self).__init__()
        self.terminalInput = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
        
    def startNotifying(self):
        for line in self.terminalInput:
            self.notifyObservers(line)
        self.closeObservers()
            
class FileObserver(observer.Observer):
    def __init__(self, fileName: str):
        self.output = open(fileName, "w+")
    
    def onUpdateFromSubject(self, package: str):
        self.output.write(package)
        if not package.endswith('\n'):
            self.output.write('\n')

    def onCloseFromSubject(self):
        self.output.close()
        
class StdoutObserver(observer.Observer):
    def onUpdateFromSubject(self, package: str):
        print(package)
