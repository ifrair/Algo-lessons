def rec(letters, i, subset):
    if i == len(letters):
        print(subset)
        return

    subset.append(letters[i])
    rec(letters, i + 1, subset)
    subset.pop()
    rec(letters, i + 1, subset)


s = input()
rec(s, 0, [])
