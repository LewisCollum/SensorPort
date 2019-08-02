import abc 

class PackageConfig:
    name = "name"
    value = "value"
    timestamp = "timestamp"

    @classmethod
    def nameFromDict(cls, d):
        return d.get(cls.name)

    @classmethod
    def valueFromDict(cls, d):
        return d.get(cls.value)

    @classmethod
    def timestampFromDict(cls, d):
        return d.get(cls.timestamp)
    
class Package:
    def __init__(self, package: dict):
        self.package = package

    def get(self, key):
        return self.package.get(key)

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
    def make(cls, name: str = None, value = None, timestamp: int = None):
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

    def __eq__(self, other):
        return self.values == other.values
        
    @classmethod
    def fromContainer(cls, values):
        if values == None:
            return None
        elif values.__class__ == PackageValue.containerClass:
            return cls(values) 
        return cls(cls.containerClass(values))
