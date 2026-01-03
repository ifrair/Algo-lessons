def can_place(a, b, n, sz):
    num_hor = sz // a
    num_ver = sz // b
    return (num_hor * num_ver >= n)

a, b, n = map(int, input().split())

l = -1
r = n * max(a, b) + 1
while r - l > 1:
    mid = (l + r) // 2
    if can_place(a, b, n, mid):
        r = mid
    else:
        l = mid
print(r)
