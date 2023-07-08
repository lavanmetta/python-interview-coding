

# how to check given number is prime number or not ?


"""  Any whole number greater than 1 that is divisible only by 1 and itself,
    is defined as a prime number. Consider an example of number 5,
    which has only two factors 1 and 5. This means it is a prime number. """


number = int(input())


if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is Not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is Not a prime number")
