def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d

def print_hist(h):
    for c in h:
        print(c, h[c])

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


#print histogram('brontosaurus')
h = histogram('parrot')
#print_hist(h)
#for key in sorted(h):
#    print(key, h[key])
print h
inverse = invert_dict(h)
print inverse
