def uses_all(word, string):
    for letter_st in string:
        flag_st = False
        for letter_wd in word:
            if letter_st == letter_wd:
                flag_st = True
        if flag_st == False:
            return False
    return True

letter_wd = input("Please input the word: ")
letter_st = input("Please input the string: ")

print uses_all(letter_wd, letter_st)
