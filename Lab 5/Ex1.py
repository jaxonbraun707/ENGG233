f0 = 1
f1 = 1
counter = 2
n = int(input("Please enter a positive integer number greater than or equal to three: "))

while(n < 3):
    n = int(input("Please enter a positive integer number greater than or equal to three: "))

print(f0, end = ", ")
print(f1, end = ", ")

while(counter <= n):
    fn = f1 + f0
    print(fn, end = ", ")
    counter += f1
    f0 = f1
    f1 = fn
    
