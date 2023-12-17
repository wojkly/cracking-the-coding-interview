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
            
            
def list_of_depths_rec(node: Node, depth: int, depths: list[list[int]]):
    if node:
        if len(depths) <= depth:
            depths.append([])
        depths[depth].append(node._v)
        list_of_depths_rec(node._left, depth + 1, depths)
        list_of_depths_rec(node._right, depth + 1, depths)
    
def list_of_depths(root: Node) -> list[list[int]]:
    depths = []
    list_of_depths_rec(root, 0, depths)
    return depths
    


node1 = Node(1)
node21 = Node(2)
node22 = Node(3)
node31 = Node(4)
node33 = Node(5)
node34 = Node(6)
node41 = Node(7)
node42 = Node(8)

node1._left = node21
node1._right = node22

node21._left = node31
node22._left = node33
node22._right = node34

node34._left = node41
node34._right = node42

depths = list_of_depths(node1)
for d in depths:
    print(d)