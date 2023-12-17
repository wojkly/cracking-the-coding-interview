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

def kth_to_last(node, k):
    if not node:
        return 1, False 
    
    index, is_result = kth_to_last(node.next, k)
    
    if is_result:
        return index, is_result
    
    if index == k:
        return node.v, True
    
    return index + 1, False
    
    
head = create_list([9,8,7,6,5,4,3,2,1])
print_list(head)
print(kth_to_last(head,5))
print(kth_to_last(head,9))
print(kth_to_last(head,1))
print(kth_to_last(head,10))
print(kth_to_last(head,17))
print(kth_to_last(head,0))