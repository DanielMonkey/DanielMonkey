def count(word, ch):
    cnt = 0
    for letter in word:
        if letter == ch:
            cnt = cnt + 1
    print cnt

count('banana', 'a')

