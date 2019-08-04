
import pair 
import abc

class Strategy(abc.ABC):
    @abc.abstractmethod
    def execute(self, input): pass
            
class VarianceStrategy(Strategy):
    def __init__(self, initial):
        self.mean = pair.Pair(initial = initial)
        self.variance = initial
        self.count = 0

    def execute(self, input):
        self.mean.shift()
        self.count += 1
        deviation = input - self.mean.previous
        self.mean.offsetFromPrevious(deviation/self.count)
        deviationCurrent = input - self.mean.current
        self.variance += deviation*deviationCurrent
        return self.variance/self.count
