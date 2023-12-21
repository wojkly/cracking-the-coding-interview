class Node:
    def __init__(self, v = None) -> None:
        self._v = v
        self._left = None
        self._right = None
        self._parent = None
        
    def add_left_child(self, child):
        self._left = child
        child._parent = self
        
    def add_right_child(self, child):
        self._right = child
        child._parent = self
        
    def is_left_child(self):
        return self._parent._left == self
        
    def has_parent(self):
        return self._parent != None

def pretty_print(clas, indent=0):
    print(' ' * indent +  type(clas).__name__ +  ':')
    indent += 4
    for k,v in clas.__dict__.items():
        if '__dict__' in dir(v):
            pretty_print(v,indent)
        else:
            print(' ' * indent +  k + ': ' + str(v))  
            
def find_node_by_value(node: Node, v: int) -> Node:
    if node:
        if node._v == v:
            return node
        
        left_subtree_result = find_node_by_value(node._left, v)
        if left_subtree_result:
            return left_subtree_result
        
        right_subtree_result = find_node_by_value(node._right, v)
        if right_subtree_result:
            return right_subtree_result
    return None
            
def first_common_ancestor(root: Node, p: int, q: int) -> Node:
    p_node = find_node_by_value(root, p)
    
    if not p_node:
        return None
    
    if find_node_by_value(p_node, q):
        return p_node
    
    
    possible_common_ancestor = p_node
    
    while possible_common_ancestor.has_parent():
        #check if parent is q
        parent = possible_common_ancestor._parent
        if parent._v == q:
            return parent
        
        #check other child of parent
        if possible_common_ancestor.is_left_child():
            #search right child of parent
            if find_node_by_value(parent._right, q):
                return parent
        else:
            if find_node_by_value(parent._left, q):
                return parent
        
        possible_common_ancestor = parent
        
    return None

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
    
assert first_common_ancestor(nodes[8], 1, 15)._v == 8

assert first_common_ancestor(nodes[8], 1, 70) == None
assert first_common_ancestor(nodes[8], 70, 15) == None

assert first_common_ancestor(nodes[8], 2, 2)._v == 2
assert first_common_ancestor(nodes[8], 11, 12)._v == 12
assert first_common_ancestor(nodes[8], 8, 1)._v == 8