def backpack(w, c, backpack_w):
    w = [0] + w
    c = [0] + c
    n = len(w)
    dp = [[0] * (backpack_w + 1) for _ in range(n)]
    for i in range(1, n):
        for j in range(backpack_w + 1):
            dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - w[i]] + c[i] if j - w[i] >= 0 else 0))
    return max(dp[n - 1])

print(backpack([7, 4, 1, 5], [8, 4, 2, 5], 10))