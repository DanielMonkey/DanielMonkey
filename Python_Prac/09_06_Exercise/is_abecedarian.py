def is_abecedarian(word):
    index_wd = 0
    while index_wd < (len(word) - 1):
        if word[index_wd] > word[index_wd + 1]:
            return False
        index_wd = index_wd + 1
    return True

#letter_word = input("Please input the word: ")

#print is_abecedarian(letter_word)

cnt_wd = 0
cnt_abc = 0

fin = open('words.txt')

for line in fin:
    letter_wd = line.strip()
    cnt_wd = cnt_wd + 1
    if is_abecedarian(letter_wd):
        print(letter_wd)
        cnt_abc = cnt_abc + 1

percentage_abc = cnt_abc * 100.0 / cnt_wd
print("The percentage of words in the list that is abecedarian is %5.3f%%."%(percentage_abc))


