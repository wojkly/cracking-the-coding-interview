from data.graph_parser import GraphParser

def dfs_visit(G, v, E, visited):
    for u in G[v]:
        if visited[E]:
            return
        if not visited[u]:
            visited[u] = True
            dfs_visit(G, u, E, visited) 
    

def route_between_nodes(G, S, E):
    # DFS lets gooo
    
    visited = [False for _ in range(len(G))]
    visited[S] = True
    
    dfs_visit(G, S, E, visited)
    
    # print(visited)
    return visited[E]
    
    


graph = GraphParser.parse("D:\\shared\\dev\\cracking-the-coding-interview\\4-trees-and-graphs\\data\\graph1")

print(graph)

test_cases = [
    [1, 3, True],
    [1, 1, True],
    [0 , 1, False],
    [4, 3, True],
]

for S, E, expected_result in test_cases:
    print('Testing ', S, E, expected_result)
    assert route_between_nodes(graph, S, E) == expected_result