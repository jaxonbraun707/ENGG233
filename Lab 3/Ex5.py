num = str(input("Please enter a six digit number: "))
digit1 = int(num[0])
print("The digits in the number you gave that can be divided my the first digit are: ")

if(int(num[1]) % digit1 == 0):
    print(num[1])
if(int(num[2]) % digit1 == 0):
    print(num[2])
if(int(num[3]) % digit1 == 0):
    print(num[3])
if(int(num[4]) % digit1 == 0):
    print(num[4])
if(int(num[5]) % digit1 == 0):
    print(num[5])
