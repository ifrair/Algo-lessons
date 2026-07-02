import heapq

# Ищем кратчайшие расстояния от 0 вершины до остальных
def dejkstra(graph):
    n = len(graph)
    visited = [False] * n
    dist = [1e9] * n
    dist[0] = 0
    heap = [(0, 0)] # (dist, num)
    while len(heap) != 0:
        # достаем ближайший к старту элемент из кучи
        cur = heapq.heappop(heap)[1]
        if visited[cur]:
            continue
        visited[cur] = True
        # ставим в очередь всех непосещенных соседей
        for to, w in graph[cur]:
            if not visited[to] and dist[to] > dist[cur] + w:
                dist[to] = dist[cur] + w
                heapq.heappush(heap, (dist[to], to))

    return dist

graph = [
    [(1, 1), (2, 2)], # (to, w)
    [(0, 1), (3, 2)],
    [(0, 2), (5, 3), (4, 1)],
    [(1, 2)],
    [(2, 1), (5, 1)],
    [(2, 3), (4, 1), (6, 3)],
    [(5, 3)],
]
print(dejkstra(graph))

