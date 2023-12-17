class Node:
    def __init__(self, v = None) -> None:
        self.v = v
        self.next = None
        
class Stack:
    def __init__(self) -> None:
        self._top = Node()
        self.size = 0
        
    def push(self, v):
        n = Node(v)
        n.next = self._top
        self._top = n
        self.size += 1
        
    def pop(self):
        if self._top.next:
            top = self._top.v
            self._top = self._top.next
            self.size -= 1
            return top
    
    def top(self):
        if self._top.next:
            return self._top.v
        
class SetOfStacks:
    def __init__(self, th = 5) -> None:
        self._current_stack = Node(Stack())
        self._th = th
        
    def current_stack(self):
        return self._current_stack.v
        
    def push(self, v):
        if self.current_stack().size == self._th:
            #create new stack
            new_stack = Node(Stack())
            new_stack.next = self._current_stack
            self._current_stack = new_stack
            
        #append to current stack
        self.current_stack().push(v)
        
    def pop(self):
        pop =  self.current_stack().pop()
        
        
        if self.current_stack().size == 0 and self._current_stack.next:
            #remove empty stack if not last one...
            current_stack = self._current_stack
            self._current_stack = self._current_stack.next
            
            current_stack.next = None
            del current_stack
            
        return pop
    
    def top(self):
        return self.current_stack().top()
        
stack = SetOfStacks(2)
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

stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
assert stack.top() == 1

def pretty_print(clas, indent=0):
    print(' ' * indent +  type(clas).__name__ +  ':')
    indent += 4
    for k,v in clas.__dict__.items():
        if '__dict__' in dir(v):
            pretty_print(v,indent)
        else:
            print(' ' * indent +  k + ': ' + str(v))
            
pretty_print(stack)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
pretty_print(stack)
stack.pop()
stack.pop()
stack.pop()
pretty_print(stack)