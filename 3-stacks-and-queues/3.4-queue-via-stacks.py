class Node:
    def __init__(self, v = None) -> None:
        self.v = v
        self.next = None
        
class Stack:
    def __init__(self) -> None:
        self._top = Node()
        
    def push(self, v):
        n = Node(v)
        n.next = self._top
        self._top = n
        
    def pop(self):
        if self._top.next:
            top = self._top.v
            self._top = self._top.next
            return top
    
    def top(self):
        if self._top.next:
            return self._top.v
        
    def is_empty(self):
        return not self._top.next

class StackQueue:
    def __init__(self) -> None:
        self.stack_to_put = Stack()
        self.stack_to_get = Stack()
        
    def put(self, v):
        self.stack_to_put.push(v)
    
    def get(self):
        if self.stack_to_get.is_empty():
            while not self.stack_to_put.is_empty():
                self.stack_to_get.push(self.stack_to_put.pop())
                
        return self.stack_to_get.pop()
    
queue = StackQueue()

assert queue.get() == None
queue.put(1)
assert queue.get() == 1
assert queue.get() == None
assert queue.get() == None
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
assert queue.get() == 1
assert queue.get() == 2
assert queue.get() == 3
queue.put(6)
queue.put(7)
assert queue.get() == 4
assert queue.get() == 5
assert queue.get() == 6
assert queue.get() == 7
assert queue.get() == None