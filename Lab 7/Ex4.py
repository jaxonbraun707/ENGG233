n = int(input("Enter a number: "))
matrix = [[0 for i in range(n)] for j in range (n)]

counter = 1
row = 0
column = 0

for i in matrix:
    for j in i:
        if counter == 0:
            matrix[row][column] = 1
            counter += 1
            column += 1
        else:
            counter -= 1
            column += 1
    row += 1
    column = 0
    if counter == 0 and n % 2 == 0:
        counter = 1
    elif not(counter == 0) and n % 2 == 0: 
        counter = 0
    elif counter == 0 and not(n % 2 == 0):
        counter = 0
    else:
        counter = 1

for i in matrix:
    for j in i:
         print(j, end = " ")
    print()
    print()
