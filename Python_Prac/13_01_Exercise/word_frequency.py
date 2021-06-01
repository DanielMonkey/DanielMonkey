import string

def word_freq(file_name):
    fin = open(file_name)
    t = tuple()
    for line in fin:
        t = line.strip()
    return t

print word_freq('words.txt')
