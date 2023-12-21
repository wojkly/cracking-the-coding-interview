from data.graph_parser import GraphParser
from collections import deque

# graph = GraphParser.parse("D:\\shared\\dev\\cracking-the-coding-interview\\4-trees-and-graphs\\data\\graph2")
graph = GraphParser.parse("C:\\Users\\Paulina\\OneDrive - Uniwersytet Jagielloński\\Pulpit\\cracking-the-coding-interview\\4-trees-and-graphs\\data\\graph2")

print(graph)

def build_order(graph):
    ingoing_edges = [0 for _ in range(len(graph))]
    for i in range(len(graph)):
        for dest in graph[i]:
            ingoing_edges[dest] += 1

    q = deque()
    for i in range(len(graph)):
        if ingoing_edges[i] == 0:
            q.append(i)

    order = []
    while q:
        u = q.popleft()
        order.append(u)

        for v in graph[u]:
            ingoing_edges[v] -= 1
            if ingoing_edges[v] == 0:
                q.append(v)

    if len(order) < len(graph):
        return []

    return order

print("=" * 100) 
order = build_order(graph)
print(order)
print("=" * 100)

graph[2].add(0)
order = build_order(graph)
print(order)
print("=" * 100)