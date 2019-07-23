import sys
sys.path.append("../source")
import distributor as d
import terminal as term
import associative_distributor as ad
import splitter
import imu
import node
import package as pk
import package_imu as pk_imu
import encoder
import os

pk.PackageConfig.timestamp = "millis"
pk.PackageConfig.value = "values"

terminalDistributor = d.SingleDistributor()
jsonLoadDistributor = d.SingleDistributor()
#packageDistributor = d.SingleDistributor()
splitDistributor = ad.KeyDistributor()
imuDistributor = d.SingleDistributor()
jsonDumpDistributor = d.MultiDistributor()

#how to name node vs handler vs joiner, splitter? Too many names
#better name for TerminalDistributor
terminal = term.TerminalDistributor(terminalDistributor)
jsonLoadNode = node.JsonLoadNode(jsonLoadDistributor)
packageSplitter = splitter.PackageSplitter(splitDistributor)
#packagingNode = node.PackagingNode(packageDistributor)
#splitNode = splitter.Splitter(splitDistributor)
imuNode = imu.QuaternionVectorJoiner(imuDistributor)
jsonDumpNode = node.JsonDumpNode(jsonDumpDistributor, encoder.PackageEncoder)
stdoutWriter = term.StdoutWriter()
fileWriter = term.FileWriter(f"{os.path.dirname(sys.argv[1])}/imu")

acceleration = "Linear Acceleration"
rotation = "Rotation Vector"

#refactor here
packageSplitter.addPackageClass(rotation, pk_imu.Quaternion)
packageSplitter.addPackageClass(acceleration, pk_imu.Vector3D)

terminalDistributor.connect(jsonLoadNode)
jsonLoadDistributor.connect(packageSplitter)
#packageDistributor.connect(splitNode)
splitDistributor.connect(acceleration, imuNode)
splitDistributor.connect(rotation, imuNode)
imuDistributor.connect(jsonDumpNode)
jsonDumpDistributor.connect(stdoutWriter)
jsonDumpDistributor.connect(fileWriter)

imuNode.addQuaternionName(rotation)
imuNode.addVectorName(acceleration)

terminal.startDistributing()

#needs to be a way to not distribute every time
