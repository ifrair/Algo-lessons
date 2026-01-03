a = list(map(int, input().split()))
w = int(input())

diff = {}
for i in range(w):
    diff.setdefault(a[i], 0)
    diff[a[i]] += 1
ma = len(diff)
l = 0
for r in range(w - 1, len(a) - 1):
    diff.setdefault(a[r + 1], 0)
    diff[a[r + 1]] += 1
    diff[a[l]] -= 1
    if diff[a[l]] == 0:
        del diff[a[l]]
    l += 1
    ma = max(ma, len(diff))
print(ma)