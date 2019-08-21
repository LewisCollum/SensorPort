import sys
sys.path.append("../source")
import os

import imu
import package_imu as pk_imu
import distributor as d
import terminal as term
import package as pk
import packaging_handler as pn
import json_handler as jn
import encoder
        
pk.PackageConfig.timestamp = "millis"
pk.PackageConfig.value = "values"

accelerationName = "MPL Accelerometer"
rotationName = "Rotation Vector"

terminalDistributor = d.SingleDistributor()
terminal = term.Terminal(terminalDistributor)

loadDistributor = d.NamingDistributor()
loader = jn.JsonLoadHandler()
loader.setDistributor(loadDistributor)

joiner = imu.QuaternionVectorJoiningNode.makeFromNames(
    quaternionName = rotationName,
    vectorName = accelerationName)

dumpDistributor = d.SingleDistributor()
dumper = jn.JsonDumpHandler(encoder.PackageEncoder)
dumper.setDistributor(dumpDistributor)

stdoutWriter = term.StdoutWriter()
fileWriter = term.FileWriter(f"{os.path.dirname(sys.argv[1])}/imu.json")

terminalDistributor.connect(loader)
loadDistributor.connect(accelerationName, joiner)
loadDistributor.connect(rotationName, joiner)
joiner.connect(dumper)
dumpDistributor.connect(stdoutWriter)
dumpDistributor.connect(fileWriter)
terminal.startDistributing()
