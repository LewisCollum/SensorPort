import abc 

class PackageConfig:
    name = "name"
    value = "value"
    timestamp = "timestamp"
    
class Package:
    def __init__(self, package: dict):
        self.package = package

    @property
    def name(self):
        return self.package[PackageConfig.name]
        
    @property
    def value(self):
        return self.package[PackageConfig.value]
    
    @value.setter
    def value(self, value):
        self.package[PackageConfig.value] = value

    @property
    def timestamp(self):
        return self.package[PackageConfig.timestamp]
    
    @classmethod
    def make(cls, name: str = None, timestamp: int = None, value = None):
        return cls({PackageConfig.name: name, PackageConfig.value: value, PackageConfig.timestamp: timestamp})

    @classmethod
    def nameFromPackage(cls, package):
        return package.name
    
    @classmethod
    def valueFromPackage(cls, package):
        return package.value

    @classmethod
    def timestampFromPackage(cls, package):
        return package.timestamp
    
    
class PackageValue(abc.ABC):
    containerClass = tuple
    
    def __init__(self, values):
        self.values = values
        
    @classmethod
    def fromContainer(cls, values):
        if values.__class__ == PackageValue.containerClass:
            return cls(values) 
        return cls(cls.containerClass(values))
