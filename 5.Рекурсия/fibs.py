def f(i, n, pr, prpr):
    if i == n: # условие выхода
        return pr + prpr
    cur = pr + prpr # вход
    print(i)
    res = f(i + 1, n, cur, pr) # переходы
    print(i)
    return res # выход
# O(w^h + h)

n = int(input())
print(f(2, n, 1, 0))
# 0 1 1 2 3 5 8 13 21