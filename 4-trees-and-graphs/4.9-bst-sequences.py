class Node:
    def __init__(self, v = None) -> None:
        self._v = v
        self._left = None
        self._right = None
        
        
def sequence_gen_rec(sequence: list[int], nodePool: set[Node]):
    if nodePool:
        nodePoolCopy = nodePool.copy()
        
        for node in nodePool:
            nodePoolCopy.remove(node)
            sequence.append(node._v)
            
            if node._left:
                nodePoolCopy.add(node._left)
            if node._right:
                nodePoolCopy.add(node._right)
                
            sequence_gen_rec(sequence, nodePoolCopy)
                
            if node._left:
                nodePoolCopy.remove(node._left)
            if node._right:
                nodePoolCopy.remove(node._right)
                
            sequence.pop()
            nodePoolCopy.add(node)
        
    else:
        print(sequence) 

def bst_sequences(root: Node):
    sequence_gen_rec([], set([root]))
    print("=" * 100)
    
nodes = [Node(i) for i in range(7)]

nodes[2]._left = nodes[1]
nodes[2]._right = nodes[3]

nodes[3]._right = nodes[5]

nodes[5]._left = nodes[4]
nodes[5]._right = nodes[6]

bst_sequences(nodes[2])