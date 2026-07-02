n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
