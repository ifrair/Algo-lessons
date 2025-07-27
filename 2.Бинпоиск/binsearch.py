a = list(map(int, input().split()))
x = int(input())

l = -1 
r = len(a) # обе границы выставляем на 1 шире чем нужно
while r - l > 1: # тут устанавливаем точность поиска
    mid = (r + l) // 2
    if a[mid] <= x: # условие меняем под задачу
        l = mid
    else:
        r = mid
print(l) # ответ обычно там где равно в условии
