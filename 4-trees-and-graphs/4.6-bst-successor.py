class Node:
    def __init__(self, v = None) -> None:
        self._v = v
        self._parent = None
        self._left = None
        self._right = None

    def add_left_child(self, child):
        self._left = child
        child._parent = self

    def add_right_child(self, child):
        self._right = child
        child._parent = self

def pretty_print(clas, indent=0):
    print(' ' * indent +  type(clas).__name__ +  ':')
    indent += 4
    for k,v in clas.__dict__.items():
        if '__dict__' in dir(v):
            pretty_print(v,indent)
        else:
            print(' ' * indent +  k + ': ' + str(v))

def has_parent(node: Node) -> bool:
    return node._parent

def is_left_child(node: Node) -> bool:
    return node._parent._left == node

def is_right_child(node: Node) -> bool:
    return node._parent._right == node

def has_left_child(node: Node) -> bool:
    return node._left

def has_right_child(node: Node) -> bool:
    return node._right

def successor(node: Node) -> Node:
    successor = None
    if has_right_child(node):
        successor = node._right

        while has_left_child(successor):
            successor = successor._left

    elif has_parent(node) and is_left_child(node):
        successor = node._parent

    elif has_parent(node) and is_right_child(node):
        successor = node._parent
        while has_parent(successor) and is_right_child(successor):
            successor = successor._parent

        if has_parent(successor) and is_left_child(successor):
            successor = successor._parent
        else:
            successor = None
    
    return successor

nodes = [Node(i) for i in range(17)]

nodes[8].add_left_child(nodes[4])
nodes[8].add_right_child(nodes[12])

nodes[4].add_left_child(nodes[2])
nodes[4].add_right_child(nodes[6])

nodes[2].add_left_child(nodes[1])
nodes[2].add_right_child(nodes[3])

nodes[6].add_left_child(nodes[5])

nodes[12].add_left_child(nodes[10])
nodes[12].add_right_child(nodes[14])

nodes[10].add_right_child(nodes[11])

nodes[14].add_left_child(nodes[13])
nodes[14].add_right_child(nodes[15])

nodes[16].add_left_child(nodes[8])

current = nodes[1]

while current:
    print("now at node ", current._v)
    current = successor(current)


    
