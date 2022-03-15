sum_of_digits = 0
number = int(input("Please enetr a positive integer number: "))

while(number < 0):
    print("Invalid input")
    number = int(input("Please enetr a positive integer number: "))

while(number >= 1):
    sum_of_digits += number % 10
    number = int(number / 10)

print("Sum of Digits: ", sum_of_digits)




