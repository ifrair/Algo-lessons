n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

from collections import deque

def bfs(start, graph):
    q = deque()
    q.append(start)
    used = [False] * n
    used[start] = True
    dist = [-1] * n
    dist[start] = 0
    while len(q) > 0:
        cur = q[0]
        q.popleft()
        for to in graph[cur]:
            if not used[to]:
                q.append(to)
                dist[to] = dist[cur] + 1
                used[to] = True
    return dist

print(bfs(0, graph))
