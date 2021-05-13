def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

input_wd = input("Please input the word: ")
input_lt = input("Please input the letters: ")

print uses_only(input_wd, input_lt)
