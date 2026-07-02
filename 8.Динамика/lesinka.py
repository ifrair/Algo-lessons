n = int(input())

dp = [1] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + (dp[i - 2] if i - 2 >= 0 else 0) + (dp[i - 3] if i - 3 >= 0 else 0)

print(dp[n])