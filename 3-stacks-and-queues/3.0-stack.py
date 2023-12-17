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
        
stack = Stack()
assert stack.top() == None
assert stack.pop() == None
stack.push(7)
assert stack.top() == 7
assert stack.pop() == 7
stack.push(1)
stack.push(2)
stack.push(3)
assert stack.top() == 3
assert stack.pop() == 3
assert stack.top() == 2
assert stack.pop() == 2
stack.push(4)
assert stack.top() == 4
assert stack.pop() == 4
assert stack.top() == 1
assert stack.pop() == 1
assert stack.top() == None
assert stack.pop() == None