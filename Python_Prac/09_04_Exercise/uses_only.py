def uses_only(word, string):
    for letter_wd in word:
        flag = False
        for letter_st in string:
            if letter_wd == letter_st:
                flag = True
                break
        if flag == False:
            return False
    return True


input_wd = input("Please input the word: ")
input_lt = input("Please input the letters: ")

print uses_only(input_wd, input_lt)

