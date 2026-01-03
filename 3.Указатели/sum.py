a = list(map(int, input().split()))
w = int(input())

su = 0
for i in range(w):
    su += a[i]
ma = su
l = 0
for r in range(w - 1, len(a) - 1):
    su -= a[l]
    su += a[r + 1]
    l += 1
    ma = max(ma, su)
print(ma)