n = int(input())
costs = list(map(int, input().split()))
ma = costs[-1]
stonks = 0
for i in range(n - 1, -1, -1):
    ma = max(ma, costs[i])
    stonks += ma
print(stonks)