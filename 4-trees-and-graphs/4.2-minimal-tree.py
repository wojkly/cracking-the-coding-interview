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
        
def create_tree_node(array, start_index, last_index):
    #one value left to handle
    if start_index == last_index:
        return Node(array[start_index])
    
    #two values left to handle
    if start_index + 1 == last_index:
        result = Node(array[last_index])
        
        left_child = create_tree_node(array, start_index, last_index - 1)
        
        result._left = left_child
        return result
    
    #more than two values left to handle
    middle_index = (start_index + last_index) // 2
    
    result = Node(array[middle_index])
    
    left_child = create_tree_node(array, start_index, middle_index - 1)
    right_child = create_tree_node(array, middle_index + 1, last_index)
        
    result._left = left_child
    result._right = right_child
    return result


def minimal_tree(array: list[int]) -> Node:
    
    root = create_tree_node(array, 0, len(array) - 1)
    
    pretty_print(root)
    
minimal_tree([i for i in range(1,16)])