class Categorizer:
    def __init__(self, keysToKeep: list):
        self.categorized = {}
        self.keys = keysToKeep
        
    def categorizeLine(self, line: dict):
        name = line["name"]
        if name not in self.categorized:
            self.categorized[name] = {}
            for key in self.keys:
                self.categorized[name][key] = []
                
        for key in self.keys:
            self.categorized[name][key].append(line[key])

    def items(self):
        return self.categorized.items()
