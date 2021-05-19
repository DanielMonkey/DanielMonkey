def cumsum(t):
    t1 = t[:]
    for i in range(len(t)):
        t1[i] = sum(t[:i + 1])
    return t1

t_list = [1, 2, 3]
print cumsum(t_list)

