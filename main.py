# how to swap two variables

variable_one = "Blue Color"
variable_two = "Green Color"

# approach one
temp_var = variable_two  # green color
variable_two = variable_one  # blue color
variable_one = temp_var   # green color

print("blue color to : ", variable_one)
print("green color to : ", variable_two)

# approach 2

variable_one , variable_two = variable_two, variable_one

print(variable_one)
print(variable_two)



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



# prime numbers given range

for number in range(1, 21):
    if number > 1:
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number, "is a prime number")


# how to find a factorial number ?

num = int(input())

fac_count = 1

if num < 0:
    print("Factorial does not exit in negative number")
elif num == 0:
    print("Factorial of 0 is one(1)")
else:
    for i in range(1, num + 1):
        fac_count *= i

print("Factorial of {}, is  {}". format(num, fac_count))





# how to check given string is palindrome or not ?

"""
    a palindrome is a word, phrase, number, or sequence of characters
    that reads the same forward and backward. In other words,
    > madam <  reversed => madam = same word
"""

def is_palindrome(string):
    reversed_string = string[::-1]
    # Create a reversed version of the string
    if string.lower() == reversed_string.lower():
        return True
    else:
        return False


input_string = "Madam"

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



# another approach

def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True


input_string = "level"

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")





# write a python program to reverse a number ?

def reverse_number(number):
    reversed_num = 0

    while number != 0:
        # Extract the last digit of the number
        digit = number % 10

        # Append the digit to the reversed number
        reversed_num = (reversed_num * 10) + digit

        # Remove the last digit from the original number
        number //= 10

    return reversed_num

input_number = 54321

reversed_number = reverse_number(input_number)
print(f"The reversed number is: {reversed_number}")



# Write a program in Python to check whether an integer is Armstrong number or not.


"""
     an Armstrong number is a number that is equal to the sum of its own digits,
     each raised to the power of the number of digits in the number.
"""

number = input()

result = 0

for i in number:
    power_of_digits = int(i) ** len(number)
    result += power_of_digits

if int(number) == result:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")







# Write a program in Python to print the Fibonacci series using iterative method.

"""
    The Fibonacci series is the sequence of numbers (also called Fibonacci numbers),
    where every number is the sum of the preceding two numbers, such that the first two terms are '0' and '1'.
    In some older versions of the series, the term '0' might be omitted.
     A Fibonacci series can thus be given as, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . .
"""

def fibonacci_series(n):
    fib_series = [0, 1]

    for i in range(2, n + 1):
        calc = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(calc)

    return fib_series

N = 10
res = fibonacci_series(N)
for each in res:
    print(each)


# recursive

def fibonacci_seris(n):
    if n <= 1:
        return n
    else:
        return fibonacci_seris(n - 1) + fibonacci_seris(n - 2)


number = 10
for i in range(number):
    res = fibonacci_seris(i)
    print(res)





# Write a program in Python to find greatest among three integers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

greatest_num = num1

if num2 > greatest_num:
    greatest_num = num2
if num3 > greatest_num:
    greatest_num = num3

print("Greatest number is", greatest_num)




 # Write a program in Python to check if a number is binary?

def is_binary(number):
     number_str = str(number)

     for digit in number_str :
         if digit != '0' and digit != '1':
             return False

     return True


n = int(input())

if is_binary(n):
    print("Number is Binary")
else:
    print("Number is not Binary")



"""
 Write a program in Python to
 find sum of digits of a number using recursion?
"""


def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + sum_of_digits(number // 10)


n = int(input())
res = sum_of_digits(n)
print(res)







