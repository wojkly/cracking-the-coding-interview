class Node:
    def __init__(self, v = None) -> None:
        self.v = v
        self.next = None
        
def print_list(node):
    while node:
        print(node.v, end=' -> ')
        node = node.next
    print()
    
def create_list(nodes):
    head = nodes[0]
    last = head
    for node in nodes[1:]:
        last.next = node
        last = node
        
    return head
 
def list_intersection_point(head1, head2):
    nodeDict = {}
    
    curr1 = head1
    
    while curr1:
        nodeDict[curr1] = True
        curr1 = curr1.next
    
    curr2 = head2
    
    while curr2:
        if curr2 in nodeDict:
            return curr2
        curr2 = curr2.next
        
    return None
    
node11 = Node(1)
node12 = Node(1)
node21 = Node(2)
node22 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

list1 = create_list([node11, node21, node3, node4, node5])
list2 = create_list([node12, node22, node3, node4, node5])

print_list(list1)
print_list(list2)
 
point1 = list_intersection_point(list1, list2)
print(point1.v)