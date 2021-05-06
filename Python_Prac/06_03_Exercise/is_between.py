def is_between(x, y, z):
    if x <= y:
        if z >= y:
            return True
        else:
            return False
    else:
        return False

print is_between(1, 5, 4)
print is_between(3, 5, 8)

