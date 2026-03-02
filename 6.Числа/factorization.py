def factorization(x):
    devisors = []
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x //= i
            devisors.append(i)
    if x != 1:
        devisors.append(x)
    return devisors

print(factorization(12))