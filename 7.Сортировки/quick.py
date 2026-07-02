from random import randint

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[randint(0, n - 1)]
    less = []
    equal = []
    greater = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    less = quick_sort(less)
    greater = quick_sort(greater)
    return less + equal + greater
