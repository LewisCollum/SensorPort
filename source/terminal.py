import sys
from connector import Connector
from distributor import Distributor
from receiver import Receiver

class Terminal:
    def __init__(self, distributor: Distributor):
        self.distributor = distributor
        self.terminalInput = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

    def startDistributing(self):
        for line in self.terminalInput:
            self.distributor.distribute(line)

            
class TerminalDistributor(Distributor, Connector):
    def __init__(self):
        self.terminalInput = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

    def startDistributing(self):
        for line in self.terminalInput:
            self.distribute(line)
        
    def distribute(self, package):
        self.receiver.onReceivedPackage(package)
        
    def connect(self, receiver: Receiver):
        self.receiver = receiver

    def disconnect(self):
        self.receiver = None


class FileWriter(Receiver):
    def __init__(self, fileName: str):
        self.fileName = fileName
        self.output = open(self.fileName, "w+")
    
    def onReceivedPackage(self, package: str):
        self.output.write(package)
        if not package.endswith('\n'):
            self.output.write('\n')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.output.close()
        

class StdoutWriter(Receiver):
    def onReceivedPackage(self, package: str):
        print(package)
