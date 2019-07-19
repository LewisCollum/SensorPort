import sys
sys.path.append("../source")
import terminal
import datetime
import os

timeOfRecording = f"{datetime.datetime.now():%Y-%m-%d_%H:%M:%S}"
os.makedirs("output/" + timeOfRecording)

terminalSubject = terminal.TerminalSubject()
stdoutObserver = terminal.StdoutObserver()
fileObserver = terminal.FileObserver(f"output/{timeOfRecording}/raw")

terminalSubject.addObserver(stdoutObserver)
terminalSubject.addObserver(fileObserver)
terminalSubject.startNotifying()
