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

def remove_duplicates(head):
    
    if not head:
        return head 
    if not head.next:
        return head
    
    values = {}
    
    current = head
    next = head.next
    
    while next:
        if next.v not in values:
            values[next.v] = True
            next = next.next
            current = current.next
        else:
            #remove 'next'
            next = next.next
            current.next = next
            
    return head


array = [1,1,1,1,9,2,2,3,4,5,5,3,2,1,9,3,8,6,6,7,8,9,4,3,5,2,6,1,1,1]

head = Node(0)
current = head
for a in array:
    n = Node(a)
    current.next = n
    current = n
    
print_list(head)
head = remove_duplicates(head)
print_list(head)
    