def count(word, ch, start):
    cnt = 0
    index = start
    while index < len(word):
        if word[index] == ch:
            cnt = cnt + 1
        index = index + 1
    print cnt

count('banana', 'a', 2)
