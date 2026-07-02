n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j] = max((dp[i - 1][j] if i > 0 else 0), (dp[i][j - 1] if j > 0 else 0)) + a[i][j]

print(dp[n - 1][m - 1])
