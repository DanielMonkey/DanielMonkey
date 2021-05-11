def avoids(word, string):
    for letter_str in string:
        for letter_word in word:
            if letter_word == letter_str:
                return False
    return True

cnt_wd = 0
cnt_no_let = 0

string_let = input("Please input the forbidden letters: ")
fin = open('words.txt')
for line in fin:
    word = line.strip()
    cnt_wd = cnt_wd + 1
    if avoids(word, string_let):
        print(word)
        cnt_no_let = cnt_no_let + 1

percentage_no_let = cnt_no_let * 100.0 / cnt_wd
print("The percentage of words in the list that has no forbidden letters is %5.3f%%."%(percentage_no_let))


