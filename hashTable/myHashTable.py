# print(ord('a'))

# using array with fix size and also avoid collision for that fix size of array
# we are not using Linked List to avoid collision 

# arr = [None] * 1
# arr[10] = 'hi'
# print(arr)

class MyHashTable:
    def __init__(self, size):
        self.data = [None] * size
    
    # O(n) -> it is almost O(1) for used hash function in lang 
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * (i+1)) % len(self.data)
        return hash
    
    # O(1)
    def set(self, key, value):
        address = self._hash(key)
        if(not self.data[address]):
           self.data[address]: list = []
        self.data[address].append([key, value])

    # O(n) -> for avoid collision but in lang it is O(1)
    def get(self, key):
        address = self._hash(key)
        location = self.data[address]
        for i in range(len(location)):
            if(location[i][0] == key):
                return location[i][1]
        return None

    # O(n^2) for avoid collision, but in lang it is O(n)
    # O(n) space
    def keys(self):
        keys = []
        for i in range(len(self.data)):
            location = self.data[i]
            for j in range(len(location)):
                keys.append(location[j][0])
        return keys

myHash = MyHashTable(2)

myHash.set('baba', 3)
myHash.set('babaa', 23)
myHash.set('babaaa', 233)
myHash.set('babaaaa', 2333)

print(myHash.get('babaaaa'))
print(myHash.keys())