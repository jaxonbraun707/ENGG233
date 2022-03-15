i = int(input("How many rows would you like in your multiplication table (between 1 and 15): "))

while(i < 1 or i > 15):
    i = int(input("How many rows would you like in your multiplication table (between 1 and 15): "))

for x in range(i + 1):
    if (x == 0):
        print("X", end = "    ")
    else:
        print(x, end = "    ")
print()
print()

for y in range(i + 1):  
    x = 1
    if (y == 0):
        continue
    print(y, end = "    ")
    while (x <= y):
        print(x * y, end = "   ")
        x += 1
    print()
    print()
        
        


    
    








