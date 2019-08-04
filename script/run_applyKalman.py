
import sys
sys.path.append("../source")
import sys
import json
import numpy
import pykalman
import pair
import enum
import datetime
import fileinput
import os

class State:
    size = 9
    dimensions = 3
    
    class Position(enum.IntEnum):
        x, y, z = 0, 1, 2

    class Velocity(enum.IntEnum):
        x, y, z = 3, 4, 5

    class Acceleration(enum.IntEnum):
        x, y, z = 6, 7, 8
        

state = numpy.zeros(State.size)
stateModel = numpy.eye(9)
measurement = numpy.zeros(State.dimensions)
measurementModel = numpy.hstack((numpy.zeros((State.dimensions, State.size-State.dimensions)), numpy.eye(State.dimensions)))
stateVariance = numpy.eye(State.size)*0.00000005#0.00000005
measurementVariance = numpy.eye(State.dimensions)*0.0005#0.0005
processVariance = numpy.eye(State.size)

for sample in fileinput.input():
    if fileinput.isfirstline():
        initial = json.loads(sample)
        seconds = pair.Pair(initial = initial["millis"]/1000)
        acceleration = numpy.asarray(initial["values"])

        if fileinput.isstdin():
            output = sys.stdout
        else:
            output = open(f"{os.path.dirname(sys.argv[1])}/kalman.json", "w+")
    else:
        sensor = json.loads(sample)
        seconds.shift(sensor["millis"]/1000)

        measurement = numpy.asarray(sensor["values"])

        first = numpy.eye(State.dimensions)*seconds.difference
        second = numpy.eye(State.dimensions)*seconds.difference**2/2
        stateModel[0:3,3:6] = first
        #stateModel[0:3,6:9] = second
        stateModel[3:6,6:9] = first

        state = stateModel.dot(state)
        processVariance = stateModel.dot(processVariance).dot(stateModel.T) + stateVariance
        s = measurementModel.dot(processVariance).dot(measurementModel.T) + measurementVariance
        gain = processVariance.dot(measurementModel.T).dot(numpy.linalg.inv(s))
        #gain = numpy.hstack((numpy.zeros((State.dimensions, State.size-State.dimensions)), numpy.eye(State.dimensions))).T

        state = state + gain.dot(measurement - measurementModel.dot(state))
        processVariance = processVariance - gain.dot(measurementModel).dot(processVariance)
        
        # output.write(json.dumps({
        #     "name": "Meters",
        #     "millis": seconds.current,
        #     "values": [state[State.Position.x],state[State.Position.y]]}))#,state[State.Position.z]]}))
        # output.write('\n')
        
        # output.write(json.dumps({
        #     "name": "Meters/Seconds",
        #     "millis": seconds.current,
        #     "values": [state[State.Velocity.x],state[State.Velocity.y]]}))#,state[State.Velocity.z]]}))
        # output.write('\n')
        
        output.write(json.dumps({
            "name": "Meters/Second/Second",
            "millis": seconds.current*1000,
            "values": [state[State.Acceleration.x],state[State.Acceleration.y]]}))#,state[State.Acceleration.z]]}))
        output.write('\n')
        
output.close()
