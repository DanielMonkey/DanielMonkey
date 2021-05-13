def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    return uses_only(required, word)

input_wd = input("Please input the word: ")
input_lt = input("Please input the letters: ")

print uses_all(input_wd, input_lt)

