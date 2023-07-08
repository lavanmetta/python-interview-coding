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

