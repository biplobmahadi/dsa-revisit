# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        
    def peek(self):
        return self.stack[len(self.stack)-1]['val']

    def pop(self):
        p = self.stack.pop()
        return p['val']

    def push(self, number):
        if not self.stack:
            self.stack.append({'val': number, 'min': number, 'max': number})
            return
        last = self.stack[len(self.stack)-1]
        obj = {'val': number, 'min': min(last['min'], number), 'max': max(last['max'], number)}
        self.stack.append(obj)

    def getMin(self):
        return self.stack[len(self.stack)-1]['min']

    def getMax(self):
        return self.stack[len(self.stack)-1]['max']

