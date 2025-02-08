test_cases = [
        {
            'input':
                {
                    'books' : ["Harry Potter", "The Hobbit", "1984", "To Kill a Mockingbird", "The Great Gatsby"],
                    'search_book' : '1984'
                },
            'output' : 2
        },
        
        {
            'input':
                {
                    'books' : ["Harry Potter", "The Hobbit", "1984", "To Kill a Mockingbird", "The Great Gatsby"],
                    'search_book' : 'The Catcher in the Rye'
                },
            'output' : 'Book not Found'
         }
        
    ]

'''
Edge Cases

1. if the book is in the list
2. if the book appear more than 1 in the list
3. if the book is not in the list
4. if the book is at the middle of the list
5. if the book is at the end of the list
6. if the book is at the beginning of the list
'''

def find_book(books, search_book):

    if search_book in books:
        #check if the book is in the list
        return books.index(search_book)
    else:
        #if the book is not in the list
        return 'Book not Found'
        
for i,test in enumerate(test_cases):
    result = find_book(**test['input'])
    expected = test['output']
    print('Passed') if result == expected else print('Failed')