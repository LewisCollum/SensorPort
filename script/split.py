
import sys
sys.path.append("../source")
import os
import terminal as term
import distributor as d
from handling_node import HandlingNode
import package as pk
import json_node as jn

pk.PackageConfig.value = "values"
pk.PackageConfig.timestamp = "millis"

class RotationModifier(HandlingNode):
    def handle(self, package):
        package[pk.PackageConfig.name] = "Rotation (Quaternion)"
        package[pk.PackageConfig.value] = package[pk.PackageConfig.value][:4]
        return package

class AccelerationModifier(HandlingNode):
    def handle(self, package):
        package[pk.PackageConfig.name] = "Acceleration (m/s^2)"
        return package

    
fileName = os.path.splitext(os.path.basename(sys.argv[1]))[0]

accelerometerName = "MPL Accelerometer"
accelerometerPath = f"{os.path.dirname(sys.argv[1])}/{fileName}_accelerometer.json"

rotationName = "Rotation Vector"
rotationPath = f"{os.path.dirname(sys.argv[1])}/{fileName}_rotation.json"


terminalDistributor = d.MultiDistributor()
terminal = term.Terminal(terminalDistributor)

loadDistributor = d.NamingDistributor()
loader = jn.JsonLoadNode()
loader.setDistributor(loadDistributor)

rotationDistributor = d.SingleDistributor()
rotationModifier = RotationModifier()
rotationModifier.setDistributor(rotationDistributor)
accelerometerDistributor = d.SingleDistributor()
accelerometerModifier = AccelerationModifier()
accelerometerModifier.setDistributor(accelerometerDistributor)

rotationDumpDistributor = d.SingleDistributor()
rotationDumper = jn.JsonDumpNode()
rotationDumper.setDistributor(rotationDumpDistributor)
accelerometerDumpDistributor = d.SingleDistributor()
accelerometerDumper = jn.JsonDumpNode()
accelerometerDumper.setDistributor(accelerometerDumpDistributor)

accelerometerWriter = term.FileWriter(accelerometerPath)
rotationWriter = term.FileWriter(rotationPath)

terminalDistributor.connect(loader)
loadDistributor.connect(accelerometerName, accelerometerModifier)
loadDistributor.connect(rotationName, rotationModifier)
rotationDistributor.connect(rotationDumper)
accelerometerDistributor.connect(accelerometerDumper)

rotationDumpDistributor.connect(rotationWriter)
accelerometerDumpDistributor.connect(accelerometerWriter)

terminal.startDistributing()
