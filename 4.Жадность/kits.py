n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
kits = list(zip(a, b))
kits.sort(key=lambda elem: (elem[0] + elem[1]), reverse=True)
sleep_time = sum(a)
cur_time = 0
for kit in kits:
    cur_time += kit[0]
    if cur_time + kit[1] <= sleep_time:
        print("NO!")
        exit(0)
print("YES")