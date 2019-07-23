import sys
sys.path.append("../source")
import terminal as term
from datetime import datetime
import os
import distributor as d

timeOfRecording = f"{datetime.now():%Y-%m-%d_%H:%M:%S}"
os.makedirs("output/" + timeOfRecording)

terminal = term.TerminalDistributor(distributor = d.MultiDistributor())
stdoutWriter = term.StdoutWriter()
fileWriter = term.FileWriter(f"output/{timeOfRecording}/raw")

terminal.connect(stdoutWriter)
terminal.connect(fileWriter)
terminal.startDistributing()
