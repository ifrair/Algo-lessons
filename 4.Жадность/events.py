n = int(input())
events = []
for i in range(n):
    l, r = map(int, input().split())
    events.append((l, r))
events.sort(key=lambda elem: elem[1])
ans = 0
free_time_point = -1
for event in events:
    if event[0] >= free_time_point:
        ans += 1
        free_time_point = event[1]
print(ans)