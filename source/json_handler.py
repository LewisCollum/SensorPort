from receiver import Receiver
from connector import Connector
from handler import Handler
import json

class JsonLoadHandler(Handler):
    def handle(self, package):
        return json.loads(package)

class JsonDumpHandler(Handler):
    def __init__(self, jsonEncoder = None):
        self.jsonEncoder = jsonEncoder

    def handle(self, package):
        return json.dumps(package, cls = self.jsonEncoder)
