def is_array_unique(array_in):
    counter_i = -1
    for i in array_in:
        counter_i += 1
        counter_j = 0
        for j in array_in:
            if i == j:
                if counter_i == counter_j:
                    continue
                else:
                    return False
            counter_j += 1             
    return True

def main():
    array = [3, 5, 5, 20, 10]
    print(array)
    if is_array_unique(array) == True:
        print("The array is unique!")
    else: 
        print("The array is not unique!")

if __name__ == "__main__":
    main()
