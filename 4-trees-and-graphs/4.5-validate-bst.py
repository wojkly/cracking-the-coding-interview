class Node:
    def __init__(self, v = None) -> None:
        self._v = v
        self._left = None
        self._right = None

def pretty_print(clas, indent=0):
    print(' ' * indent +  type(clas).__name__ +  ':')
    indent += 4
    for k,v in clas.__dict__.items():
        if '__dict__' in dir(v):
            pretty_print(v,indent)
        else:
            print(' ' * indent +  k + ': ' + str(v))


def validate_bst(root: Node):
    if root._left:
        if root._left._v > root._v:
            return False
        if not validate_bst(root._left):
            return False
        
    if root._right:
        if root._right._v <  root._v:
            return False
        if not validate_bst(root._right):
            return False
    
    return True

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

assert validate_bst(node1)

node3._left = node1
node3._right = node5

assert validate_bst(node3)

node1._right = node2
node5._left = node4
node5._right = node6

assert validate_bst(node3)

node4._right = node0
assert validate_bst(node3) == False
