import matplotlib.pyplot as pyplot
import json
import sys
import re

class SensorPlotable:
    def __init__(self):
        self.values = []
        self.seconds = []

    def update(self, seconds: float, values: list):
        self.values.append(values)
        self.seconds.append(seconds)
        

class SensorPlotableManager:
    def __init__(self, title: str):
        self.sensors = {}
        self.title = title
        
    def update(self, name: str, seconds: float, values: list):
        if name not in self.sensors:
            self.sensors[name] = SensorPlotable()
        self.sensors[name].update(seconds, values)

    def plotAll(self):
        figure, axes = pyplot.subplots(nrows = len(self.sensors), squeeze = False, sharex = True)
        
        axes[0, 0].set_title(self.title)
        axes[len(self.sensors)-1, 0].set_xlabel("time (ms)")
        
        for i, (name, plotable) in enumerate(self.sensors.items()):
            axes[i, 0].set_ylabel(name)
            axes[i, 0].plot([i-plotable.seconds[0] for i in plotable.seconds], plotable.values)
                
        figure.tight_layout()
        pyplot.show()

        
manager = SensorPlotableManager(title = re.sub("^.*/", "", sys.argv[1]))
with open(sys.argv[1]) as jsonFile:
    for line in jsonFile:
        sample = json.loads(line)
        manager.update(sample["name"], sample["millis"], sample["values"])

manager.plotAll()
