def middle(t):
    t.pop(len(t) - 1)
    t.pop(0)
    return t

t_list = [1, 2, 3, 4]
print middle(t_list)


