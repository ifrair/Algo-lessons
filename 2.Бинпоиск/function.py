def f(x):
    return x / 2 + 1

y = int(input())

l = -1000
r = 1000
eps = 1e-4
while r - l > eps:
    mid = (r + l) / 2
    if f(mid) < y:
        l = mid
    else:
        r = mid
print(r)
