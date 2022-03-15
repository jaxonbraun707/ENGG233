import random

def print_result(m, n):
    print("The max and min are: ", m, n)

def bigger_of_two(a_in, b_in):
    if a_in > b_in:
        return a_in
    else:
        return b_in

def max_of_three(g, h, i):
    if (bigger_of_two(g, h) == g) and (bigger_of_two(g, i) == g):
        return g
    elif (bigger_of_two(h, g) == h) and (bigger_of_two(h, i) == h):
        return h
    elif (bigger_of_two(i, g) == i) and (bigger_of_two(i, h) == i):
        return i

def smaller_of_two(x_in, y_in):
    if x_in < y_in:
        return x_in
    else:
        return y_in

def min_of_three(d, e, f):
    if (smaller_of_two(d, e) == d) and (smaller_of_two(d, f) == d):
        return d
    elif (smaller_of_two(e, d) == e) and (smaller_of_two(e, f) == e):
        return e
    elif (smaller_of_two(f, d) == f) and (smaller_of_two(f, e) == f):
        return f

def is_different (a, b, c):
    if a == b == c:
        return False
    else:
        return True

def main():
    counter = 0

    while counter < 10:
        x = random.random()   #random float x, 0.0 <= x < 1.0
        y = random.uniform(1,100)  # random float x, 1.0 <= x < 100.0
        z = random.randint(1,100)  #random int from 1 to 100, endpoints included
        print("The three random numbers generated are: ", x, y, z)
        if (is_different (x, y, z)):
            print_result (min_of_three(x, y, z), max_of_three(x, y, z))
        else:
            print("The three numbers are the same")
        counter += 1

if __name__ == "__main__":
    main()