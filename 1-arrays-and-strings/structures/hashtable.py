class HashTable:
    def __init__(self, size = 1000) -> None:
        self.size = size
        self.data = [[]] * size
    
    def put(self, object):
        h = hash(object)
        index = h % self.size
        if object not in self.data[index]:
            self.data[index].append(object)
            
    def delete(self, object):
        h = hash(object)
        index = h % self.size
        if object in self.data[index]:
            self.data[index].remove(object)
            
    def get(self, object):
        h = hash(object)
        index = h % self.size
        return object in self.data[index]
    
    
dict = HashTable()
assert dict.get('aaa') == False

dict.put('aaa')
dict.put('aaa')
dict.put('aaa')
assert dict.get('aaa') == True

dict.delete('aaa')
assert dict.get('aaa') == False

dict2 = HashTable(50)

for i in range(100):
    dict2.put(i)
    
for i in range(100):
    assert dict2.get(i) == True
    
for i in range(50):
    dict2.delete(i)
    
for i in range(50):
    assert dict2.get(i) == False
for i in range(50, 100):
    assert dict2.get(i) == True