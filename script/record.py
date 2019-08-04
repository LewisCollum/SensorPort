
import sys
sys.path.append("../source")
import terminal as term
from datetime import datetime
import os
import distributor as d

terminalDistributor = d.MultiDistributor()
terminal = term.Terminal(terminalDistributor)
stdoutWriter = term.StdoutWriter()
terminalDistributor.connect(stdoutWriter)

timeOfRecording = f"{datetime.now():%Y-%m-%d_%H:%M:%S}"
os.makedirs("output/" + timeOfRecording)

with term.FileWriter(f"output/{timeOfRecording}/raw.json") as fileWriter:
    terminalDistributor.connect(fileWriter)
    terminal.startDistributing()
