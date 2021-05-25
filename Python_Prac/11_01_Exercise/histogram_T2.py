def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d

def print_hist(h):
    for c in h:
        print(c, h[c])

#print histogram('brontosaurus')
h = histogram('parrot')
#print_hist(h)
for key in sorted(h):
    print(key, h[key])

