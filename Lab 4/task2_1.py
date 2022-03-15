counter = 1
odd_sum = 0
number_of_odds = 0
number = int(input("Please input a positive integer number: "))

while(counter <= number):
    print(counter)
    odd_sum += counter
    number_of_odds += 1
    counter += 2
average = odd_sum / number_of_odds
print("Sum: ", odd_sum)
print("Average: ", average)