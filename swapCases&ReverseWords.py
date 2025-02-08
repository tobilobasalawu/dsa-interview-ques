def reverse_words_order_and_swap_cases(sentence):
    newWords = ''
    splittedWords = sentence.split(' ')
    
    reversedWords = splittedWords[::-1]
    print(' '.join(reversedWords).swapcase())
    
reverse_words_order_and_swap_cases('aWESOME is cODING')
