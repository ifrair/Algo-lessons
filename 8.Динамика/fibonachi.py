# 1 1 2 3 5 8
# f[i] = f[i-1] + f[i-2]

# 1) f[i] - i-е число Фибоначчи
# 2) f[i] = f[i-1] + f[i-2]
# 3) f[0] = f[1] = 1
# 4) f[n] - ans

n = int(input())
f = [1] * (n + 1)
for i in range(2, n + 1):
    f[i] = f[i - 1] + f[i - 2]

print(f[n])
