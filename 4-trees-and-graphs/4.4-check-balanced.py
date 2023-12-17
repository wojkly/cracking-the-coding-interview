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

class UnbalancedException(Exception):
    pass
    
def get_depth(root: Node, depth: int) -> int:
    if root:
        left_depth = get_depth(root._left, depth + 1)
        right_depth = get_depth(root._right, depth + 1)
        
        print("node: ", root._v, " children depths: ", left_depth, right_depth)
        if abs(left_depth - right_depth) > 1:
            raise UnbalancedException()
        return max(left_depth, right_depth)
    else:
        return depth
        
            
def check_balanced(root: Node) -> bool:
    try:
        get_depth(root, 0)
    except UnbalancedException:
        return False
    return True

assert check_balanced(None)

node1 = Node(1)
assert check_balanced(node1)
print('=' * 100)
node2 = Node(2)
node1._left = node2
assert check_balanced(node1)
print('=' * 100)

node3 = Node(3)
node2._left = node3
assert check_balanced(node1) == False
print('=' * 100)

root = Node(1)
root._left = Node(2)
root._left._left = Node(4)

root._right = Node(3)
root._right._right = Node(5)

assert check_balanced(root)
print('=' * 100)

root._left._left._left = Node(4)
# root._right._right._right = Node(4)
assert check_balanced(root) == False
print('=' * 100)


root._left._right = Node(4)
assert check_balanced(root)
print('=' * 100)