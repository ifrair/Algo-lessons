n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur, graph, used):
    if used[cur]:
        return
    used[cur] = True
    for to in graph[cur]:
        dfs(to, graph, used)

components_count = 0
used = [False] * n
for i in range(n):
    if not used[i]:
        components_count += 1
        dfs(i, graph, used)

print(components_count)
