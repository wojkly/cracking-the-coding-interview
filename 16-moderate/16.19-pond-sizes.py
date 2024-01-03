from collections import deque

def is_valid_position(i, j, m) -> bool:
    return 0 <= i and i < len(m) and 0 <= j and j < len(m[0])
    
def is_pond(i, j, m) -> bool:
    return m[i][j] == 0

def bfs_visit_pond(i, j, m, visited):
    q = deque()
    
    q.append((i,j))
    pond_size = 0
    while q:
        i, j = q.popleft()
        
        if visited[i][j]:
            continue
        
        visited[i][j] = True
        pond_size += 1
        
        for k in range(-1,2):
            new_i = i + k
            for l in range(-1,2):
                new_j = j + l 
                if is_valid_position(new_i, new_j, m) and is_pond(new_i, new_j, m) and not visited[new_i][new_j]:
                    q.append((new_i, new_j))
                    
    return pond_size
        
    

def get_pond_sizes(m):
    visited = [[False for j in range(len(m[0]))] for i in range(len(m))]
    
    pond_sizes = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if is_pond(i, j, m) and not visited[i][j]:
                pond_size = bfs_visit_pond(i, j, m, visited)
                pond_sizes.append(pond_size)
                
    return pond_sizes
                
m = [
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
]

pond_sizes = get_pond_sizes(m)

print(pond_sizes)


m = [
    [0, 2, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 3],
    [1, 1, 0, 1, 0, 5],
    [0, 1, 0, 1, 0, 3],
]

pond_sizes = get_pond_sizes(m)

print(pond_sizes)