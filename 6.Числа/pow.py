def my_pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    res = my_pow(a, b // 2)
    if b % 2 == 0:
        return res * res
    else:
        return res * res * a

print(my_pow(2, 11))