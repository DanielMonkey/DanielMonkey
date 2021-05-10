def print_words(file_name):
    fin = open(file_name)
    for line in fin:
        word = line.strip()
        if 20 < len(word):
            print word


print_words('words.txt')

