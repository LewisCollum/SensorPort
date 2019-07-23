import sys
import handler
import distributor as d
class TerminalDistributor:
    def __init__(self, distributor: d.Distributor):
        self.distributor = distributor
        self.terminalInput = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

    def connect(self, handler: handler.Handler):
        self.distributor.connect(handler)
        
    def startDistributing(self):
        for line in self.terminalInput:
            self.distributor.distribute(line)
        self.distributor.disconnect()


class FileWriter(handler.Handler):
    def __init__(self, fileName: str):
        self.fileName = fileName

    def onConnected(self):
        self.output = open(self.fileName, "w+")
    
    def onReceivedPackage(self, package: str):
        self.output.write(package)
        if not package.endswith('\n'):
            self.output.write('\n')

    def onDisconnected(self):
        self.output.close()
    

class StdoutWriter(handler.Handler):
    def onReceivedPackage(self, package: str):
        print(package)        

    def onConnected(self): pass
    def onDisconnected(self): pass
