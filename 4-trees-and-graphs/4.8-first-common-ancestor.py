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

nodes = []
    