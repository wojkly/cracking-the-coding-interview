class Node:
    def __init__(self, v = None) -> None:
        self._v = v
        self._left = None
        self._right = None
        
    def add_left_child(self, child):
        self._left = child
        
    def add_right_child(self, child):
        self._right = child
        

def stringify_rec(node: Node, result: list) -> list:
    if node:
        result.append(str(node._v))
        result.append('(')
        stringify_rec(node._left, result)
        stringify_rec(node._right, result)
        result.append(')')
    else:
        result.append('-')
    
def stringify(root: Node) -> str:
    array = []
    stringify_rec(root, array)
    return ''.join(array)
    
    
def is_subtree(big: Node, small: Node) -> bool:
    big_str = stringify(big)
    small_str = stringify(small)
    
    return big_str.find(small_str) != -1
    
    
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

print(is_subtree(nodes[8], nodes[12]))
print(is_subtree(nodes[7], nodes[12]))