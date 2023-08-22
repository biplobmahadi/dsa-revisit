class MyArray: 
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -=1
        return lastItem
    
    def delete(self, index):
        delItem =self.data[index]
        self.shift(index)
        self.length -=1
        return delItem
    
    def shift(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]


myArr = MyArray()

print(myArr.push(3))
print(myArr.push(33))
print(myArr.push(333))
print(myArr.push(334))
# print(myArr.pop())
# print(myArr.pop())
print(myArr.delete(2))
print(myArr.delete(0))

print(f'len -> {myArr.length}')
print(f'data -> {myArr.data}')