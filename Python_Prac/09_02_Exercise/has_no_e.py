def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return
    return True

cnt_wd = 0
cnt_no_e = 0

fin = open('words.txt')
for line in fin:
    cnt_wd = cnt_wd + 1
    word = line.strip()
    if has_no_e(word):
        cnt_no_e = cnt_no_e + 1
        print word

percentage_no_e = cnt_no_e * 100.0 / cnt_wd
print ("The percentage of words in the list that has no 'e' is %5.3f%%"%(percentage_no_e))
