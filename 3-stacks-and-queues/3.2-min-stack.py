class Node:
    def __init__(self, v = None) -> None:
        self.v = v
        self.min_below = None
        self.next = None
        
class MinStack:
    
    def __init__(self) -> None:
        self._top = Node()
        self._top.min_below = float('inf')
        
    def push(self, v):
        n = Node(v)
        n.next = self._top
        self._top = n
        
        #set min value for this node
        self._top.min_below = min(self._top.v, self._top.next.min_below)
        
    def pop(self):
        if self._top.next:
            top = self._top.v
            self._top = self._top.next
            return top
    
    def top(self):
        if self._top.next:
            return self._top.v
        
    def min(self):
        return self._top.min_below
    
stack = MinStack()
assert stack.min() == float('inf')
assert stack.top() == None
assert stack.pop() == None
assert stack.min() == float('inf')
stack.push(7)
assert stack.min() == 7
assert stack.top() == 7
assert stack.pop() == 7
assert stack.min() == float('inf')
stack.push(1)
stack.push(2)
stack.push(3)
assert stack.min() == 1
assert stack.top() == 3
assert stack.pop() == 3
assert stack.min() == 1
assert stack.top() == 2
assert stack.pop() == 2
assert stack.min() == 1
stack.push(4)
assert stack.min() == 1
assert stack.top() == 4
assert stack.pop() == 4
assert stack.top() == 1
assert stack.pop() == 1
assert stack.min() == float('inf')
assert stack.top() == None
assert stack.pop() == None