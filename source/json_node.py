
from receiver import Receiver
from connector import Connector
from handling_node import HandlingNode
import json

class JsonLoadNode(HandlingNode):
    def handle(self, package):
        return json.loads(package)

class JsonDumpNode(HandlingNode):
    def __init__(self, jsonEncoder = None):
        self.jsonEncoder = jsonEncoder

    def handle(self, package):
        return json.dumps(package, cls = self.jsonEncoder)
