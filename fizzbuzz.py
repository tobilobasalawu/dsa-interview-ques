def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if (i % 3 == 0) & (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzBuzz(15)