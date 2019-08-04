
from handling_node import HandlingNode
import numpy
import pair

class KalmanNode(HandlingNode):
    def __init__(self):
        #seconds = pair.TimePair(initial = initial["millis"]/1000)
        ms = 5
        dt = numpy.eye(9)*ms
        self.stateModel = 
        self.stateVariance = None
        self.measurementModel = None
        self.measurementVariance = None
    
        self.state = None
        self.processVariance = None

    def setStateModel(model: numpy.ndarray):
        self.stateModel = model

    def setMeasurementModel(model: numpy.ndarray):
        self.measurementModel = model
        
    def handle(self, package):
        measurement = package.value.values
        
        self.state = self.stateModel.dot(self.state)
        self.processVariance = self.stateModel.dot(self.processVariance).dot(self.stateModel.T) + self.stateVariance
        s = measurementModel.dot(processVariance).dot(measurementModel.T) + measurementVariance
        gain = processVariance.dot(measurementModel.T).dot(numpy.linalg.inv(s))
        self.state = self.state + gain.dot(measurement - measurementModel.dot(state))
        self.processVariance = self.processVariance - gain.dot(self.measurementModel).dot(self.processVariance)



            
state = numpy.zeros(State.size)
stateModel = numpy.eye(9)
measurement = numpy.zeros(State.dimensions)
measurementModel = numpy.hstack((numpy.zeros((State.dimensions, State.size-State.dimensions)), numpy.eye(State.dimensions)))
stateVariance = 0 #numpy.eye(State.size)*0.0005
measurementVariance = numpy.eye(State.dimensions)*0.0005
processVariance = numpy.eye(State.size)

first = numpy.eye(State.dimensions)*seconds.difference
second = numpy.eye(State.dimensions)*seconds.difference**2/2
stateModel[0:3,3:6] = first
stateModel[0:3,6:9] = second
stateModel[3:6,6:9] = first

state = stateModel.dot(state)
processVariance = stateModel.dot(processVariance).dot(stateModel.T) + stateVariance
s = measurementModel.dot(processVariance).dot(measurementModel.T) + measurementVariance
gain = processVariance.dot(measurementModel.T).dot(numpy.linalg.inv(s))
#gain = numpy.hstack((numpy.zeros((State.dimensions, State.size-State.dimensions)), numpy.eye(State.dimensions))).T

state = state + gain.dot(measurement - measurementModel.dot(state))
processVariance = processVariance - gain.dot(measurementModel).dot(processVariance)
