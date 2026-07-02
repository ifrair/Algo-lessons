def floyd(graph):
    n = len(graph)
    for k in range(n):
        for f in range(n):
            for t in range(n):
                graph[f][t] = min(graph[f][t], graph[f][k] + graph[k][t])
    return graph

graph = [
    [0, 1, 3, 1e9],
    [1, 0, 1, 1e9],
    [3, 1, 0, 2],
    [1e9, 1e9, 2, 0],
]
print(floyd(graph))