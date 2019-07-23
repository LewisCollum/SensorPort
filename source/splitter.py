import handler
import node
import associative_distributor as ad
import package as pk

class Splitter(node.Node):
    def handlePackage(self, package): return package
    def onConnected(self): pass
    def onDisconnected(self): pass

class PackageSplitter(node.Node):
    def __init__(self, distributor: ad.AssociativeDistributor):
        super(PackageSplitter, self).__init__(distributor)
        self.packageClasses = {}
        
    def handlePackage(self, package):
        package = pk.Package(package)
        package.value = self.packageClasses[package.name](package.value)
        return package

    def addPackageClass(self, name: str, cls: pk.PackageValue):
        self.packageClasses[name] = cls
        
    def onConnected(self): pass
    def onDisconnected(self): pass
