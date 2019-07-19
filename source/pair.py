class Pair:
    def __init__(self, initial = None):
        self.pair = [None, initial]
        
    def shift(self, new = None):
        self.pair[0] = self.pair[1]
        self.pair[1] = new

    def offsetFromPrevious(self, offset):
        self.pair[1] = self.pair[0] + offset
                
    @property
    def current(self):
        return self.pair[1]

    @property
    def previous(self):
        return self.pair[0]

    @property
    def difference(self):
        return self.pair[1] - self.pair[0]
