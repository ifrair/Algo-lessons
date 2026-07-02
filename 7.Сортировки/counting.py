def counting_sort(arr):
    n = len(arr)
    mi = min(arr)
    ma = max(arr)
    counts = [0] * (ma - mi + 1)
    for x in arr:
        counts[x - mi] += 1

    arr.clear()
    for x in range(len(counts)):
        arr += [x + mi] * counts[x]
