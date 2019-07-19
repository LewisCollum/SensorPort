import sys
sys.path.append("../source")
import sys
import os
import numpy
import terminal
import observer
import encoder
import node
import strategy
import splitter

inputSubject = terminal.TerminalSubject()
jsonLoadNode = node.JsonLoadNode()

varianceNode = node.StrategyNode(strategy.VarianceStrategy(initial = numpy.zeros(3)))
#splitter = splitter.SplitterBranchReplicator(headOfBranch = varianceNode)
#varianceNodeA = node.StrategyNode(strategy.VarianceStrategy(initial = numpy.zeros(3)))
#varianceNodeB = node.StrategyNode(strategy.VarianceStrategy(initial = numpy.zeros(3)))
#splitter.addNamedNode("MPL Accelerometer", varianceNodeA)
#splitter.addNamedNode("MPL Gyroscope", varianceNodeB)

jsonDumpNode = node.JsonDumpNode(jsonEncoder = encoder.NumpyEncoder)
fileObserver = terminal.FileObserver(f"{os.path.dirname(sys.argv[1])}/variance")
stdoutObserver = terminal.StdoutObserver()

inputSubject.addObserver(jsonLoadNode)
jsonLoadNode.addObserver(splitter.SplitterBranchReplicator(headOfBranch = varianceNode))
varianceNode.addObserver(jsonDumpNode)
#varianceNodeA.addObserver(jsonDumpNode)
#varianceNodeB.addObserver(jsonDumpNode)
jsonDumpNode.addObserver(fileObserver)
jsonDumpNode.addObserver(stdoutObserver)

inputSubject.startNotifying()

        
# inputSubject = terminal.TerminalSubject()
# jsonLoadNode = node.JsonLoadNode()
# varianceNode = node.StrategyNode(strategy.VarianceStrategy(initial = numpy.zeros(3)))
# jsonDumpNode = node.JsonDumpNode(jsonEncoder = encoder.NumpyEncoder)
# fileObserver = terminal.FileObserver(f"{os.path.dirname(sys.argv[1])}/variance")
# stdoutObserver = terminal.StdoutObserver()

# inputSubject.addObserver(jsonLoadNode)
# jsonLoadNode.addObserver(varianceNode)
# varianceNode.addObserver(jsonDumpNode)
# jsonDumpNode.addObserver(fileObserver)
# jsonDumpNode.addObserver(stdoutObserver)

# inputSubject.startNotifying()
