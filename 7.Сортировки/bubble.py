def bubble_sort(arr):
    n = len(arr)
    for it in range(n - 1):
        for i in range(n - 1 - it):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

arr = [6, 5, 3, 1, 8, 7, 2, 4]
bubble_sort(arr)
print(arr)
