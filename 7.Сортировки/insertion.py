def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[j + 1]:
                break
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
