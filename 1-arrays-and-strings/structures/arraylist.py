class ArrayList:
    def __init__(self, maxSize = 10) -> None:
        self.size = 0
        self.maxSize = maxSize
        self.data = [None for _ in range(maxSize)]
        
    def get(self, index: int):
        if index < self.size:
            return self.data[index]
        else:
            raise IndexError('list index out of range')
            
    def add(self, value):
        self.data[self.size] = value
        self.size += 1
        
        if self.size == self.maxSize:
            self.maxSize *= 2
            
            data = [None for _ in range(self.maxSize)]
            for i in range(len(self.data)):
                data[i] = self.data[i]
                
            self.data = data
        
    def pop(self):
        self.data[self.size] = None
        self.size -= 1
        
    def print(self) -> str:
        print('[', end='')
        for i in range(self.size):
            print(self.data[i],', ', sep='', end='')
        print(']')

arr = ArrayList(5)
arr.print()
arr.add(1)
arr.add(2)
arr.print()
arr.add(3)
arr.add(4)
arr.add(5)
arr.add(6)
arr.print()
arr.pop()
arr.print()