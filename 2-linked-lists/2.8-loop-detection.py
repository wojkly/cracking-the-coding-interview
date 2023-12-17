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
 
def loop_detection(head):
    nodes = {}
    
    curr = head
    
    while curr:
        if curr in nodes:
            return curr
        
        nodes[curr] = True
        curr = curr.next
    
    return None
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

list = create_list([node1, node2, node3, node4, node5, node6])
node6.next = node3
 
loop = loop_detection(list)
print(loop.v)