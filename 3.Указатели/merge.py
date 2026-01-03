def merge(a, b):
    f = 0
    s = 0
    ans = []
    while f != len(a) or s != len(b):
        if f != len(a) and (s == len(b) or a[f] < b[s]):
            ans.append(a[f])
            f += 1
        else:
            ans.append(b[s])
            s += 1
    return ans

print(merge([1, 3, 4, 6, 7, 8], [2, 4, 5, 5, 6, 6]))