def comparison(word):
    if word < 'banana':
        print 'Your word, ' + word + ', comes before banana.'
    elif word > 'banana':
        print 'Your word, ' + word + ', comes after banana.'
    else:
        print 'All right, bananas.'

comparison('Pineapple')
comparison('pineapple')
comparison('banana')
comparison('Banana')