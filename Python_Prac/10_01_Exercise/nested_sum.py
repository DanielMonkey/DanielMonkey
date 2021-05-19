def nested_sum(t):
    total_sum = 0
    for x in t:
        total_sum = total_sum + sum(x)
    return total_sum

t_list = [[1, 2], [3], [4, 5, 6]]
print nested_sum(t_list)

