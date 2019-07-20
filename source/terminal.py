import sys
import observer
import base

class TerminalDistributor:
    def __init__(self, distributor: base.Distributor):
        self.distributor = distributor
        self.terminalInput = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

    def connectToHandler(self, handler: base.Handler):
        self.distributor.connectToHandler(handler)
        
    def startDistributing(self):
        for line in self.terminalInput:
            self.distributor.distribute(line)
        self.distributor.disconnectHandlers()


class FileWriter(base.Handler):
    def __init__(self, fileName: str):
        self.fileName = fileName

    def onConnected(self):
        self.output = open(fileName, "w+")
    
    def onReceivedPackage(self, package: str):
        self.output.write(package)
        if not package.endswith('\n'):
            self.output.write('\n')

    def onDisconnected(self):
        self.output.close()
    

class StdoutWriter(base.Handler):
    def onUpdateFromSubject(self, package: str):
        print(package)        

    def onConnected(self): pass
    def onDisconnected(self): pass
