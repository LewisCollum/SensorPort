
import json
import numpy
import package as pk

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class PackageEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pk.Package):
            return obj.package
        elif isinstance(obj, pk.PackageValue):
            return obj.values
