class Node:
    def __init__(self, v = None) -> None:
        self.v = v
        self.next = None
        
def print_list(node):
    while node:
        print(node.v, end=' -> ')
        node = node.next
    print()
    
def create_list(array):
    head = Node(array[0])
    current = head
    for a in array[1:]:
        n = Node(a)
        current.next = n
        current = n
        
    return head

def partition(head, value):
    headLess = Node()
    lastLess = headLess
    headGreater = Node() 
    lastGreater = headGreater
    
    current = head
    while current is not None:
        if current.v >= value:
            lastGreater.next = current
            lastGreater = lastGreater.next
        else:
            lastLess.next = current
            lastLess = lastLess.next
        current = current.next
        
    lastLess.next = headGreater.next
    lastGreater.next = None
    return headLess.next

head1 = create_list([3,5,8,5,10,2,1])
print_list(head1) 
part1 = partition(head1,5)
print_list(part1) 
        
    
            
            
    