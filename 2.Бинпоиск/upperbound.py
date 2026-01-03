a = list(map(int, input().split()))
x = int(input())

l = -1 
r = len(a) 
# ищем первый элемент больше данного
while r - l > 1:
    mid = (r + l) // 2
    if a[mid] <= x:
        l = mid
    else:
        r = mid
print(r)
