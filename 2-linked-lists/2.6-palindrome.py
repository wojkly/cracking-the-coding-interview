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

def reverse(head):
    headRev = Node()
    
    curr = head
    while curr:
        currCopy = Node(curr.v)
        currCopy.next = headRev.next
        headRev.next = currCopy
        
        curr = curr.next
        
    return headRev.next

def is_palindrome(head):
    headRev = reverse(head)
    
    print_list(head)
    print_list(headRev)
    
    tmp1 = head
    tmp2 = headRev
    
    while tmp1 and tmp2:
        if tmp1.v != tmp2.v:
            return False
        
        tmp1 = tmp1.next
        tmp2 = tmp2.next
        
    return True
        
    

list1 = create_list([1,2,3,4,5,6,7,6,7,6,5,4,3,2,1])
palindrome1 = is_palindrome(list1)
print(palindrome1)