def rec(letters, i, perm, is_used):
    if i == len(letters):
        print(*perm, sep='')
        return
    for idx in range(len(letters)):
        if not is_used[idx]:
            perm.append(letters[idx])
            is_used[idx] = True
            rec(letters, i + 1, perm, is_used)
            is_used[idx] = False
            perm.pop()

s = input()
rec(s, 0, [], [False] * len(s))
