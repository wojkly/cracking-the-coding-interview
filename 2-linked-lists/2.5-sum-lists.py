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

def sum_lists(head1, head2):
    headRes = Node()
    currRes = headRes
    remainder = 0
    
    curr1 = head1
    curr2 = head2
    
    while curr1 and curr2:
        sum = curr1.v + curr2.v + remainder
        digitRes = sum % 10
        remainder = sum // 10
        
        digitNode = Node(digitRes)
        currRes.next = digitNode
        
        curr1 = curr1.next
        curr2 = curr2.next
        currRes = currRes.next
        
    while curr1:
        sum = curr1.v + remainder
        digitRes = sum % 10
        remainder = sum // 10
        
        digitNode = Node(digitRes)
        currRes.next = digitNode
        
        curr1 = curr1.next
        currRes = currRes.next
        
    while curr2:
        sum = curr2.v + remainder
        digitRes = sum % 10
        remainder = sum // 10
        
        digitNode = Node(digitRes)
        currRes.next = digitNode
        
        curr2 = curr2.next
        currRes = currRes.next
        
    if remainder > 0:
        digitNode = Node(remainder)
        currRes.next = digitNode
        
        
    return headRes.next
    
def sum_lists_reverse_order(head1, head2):
    headRes = Node()
    currRes = headRes
    remainder = 0
    
    curr1 = head1
    curr2 = head2
    
    while curr1 and curr2:
        sum = curr1.v + curr2.v + remainder
        digitRes = sum % 10
        remainder = sum // 10
        
        digitNode = Node(digitRes)
        currRes.next = digitNode
        
        curr1 = curr1.next
        curr2 = curr2.next
        currRes = currRes.next
        
    return headRes.next

def test(list1, list2):
    head1 = create_list(list1)
    head2 = create_list(list2)
    print_list(head1)
    print_list(head2)
    sum1 = sum_lists(head1,head2)
    print_list(sum1)
    
test([7,1,6], [5,9,2])
print('-'*100)
test([0,0,1], [0,0,9,9,9,9,9])
print('-'*100)