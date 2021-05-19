def middle(t):
    del t[len(t) - 1]
    del t[0]
    return t

t_list = [1, 2, 3, 4]
print middle(t_list)
