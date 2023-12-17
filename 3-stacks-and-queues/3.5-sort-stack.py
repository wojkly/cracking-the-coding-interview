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

def print_list(node):
    while node.next:
        print(node.v, end=' -> ')
        node = node.next
    print()
    
def sort_stack(s1):
    s2 = Stack()
    
    while s1.top():
        current = s1.pop()
        
        if not s2.top() or current >= s2.top():
            s2.push(current)
        else:
            while s2.top() and current < s2.top():
                s1.push(s2.pop())
            s2.push(current)
            
    
    while s2.top():
        s1.push(s2.pop())
    
            
        
    
s1 = Stack()
s1.push(1)
s1.push(3)
s1.push(2)
s1.push(4)
s1.push(6)
s1.push(5)

print_list(s1._top)
sort_stack(s1)
print_list(s1._top)
