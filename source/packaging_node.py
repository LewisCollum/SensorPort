from handling_node import HandlingNode
import package as pk

class PackagingNode(HandlingNode):
    def __init__(self, PackageValueClass: pk.PackageValue = pk.PackageValue):
        self.PackageValueClass = PackageValueClass

    def handle(self, package: dict):
        values = pk.PackageConfig.valueFromDict(package)
        return pk.Package.make(
            name = pk.PackageConfig.nameFromDict(package),
            value = self.PackageValueClass.fromContainer(values),
            timestamp = pk.PackageConfig.timestampFromDict(package))
