import random

def merge_sort(array_1, array_2, n_in, m_in):
    array_3 = []
    counter = 0
    i = 0
    j = 0
    while counter <= n_in + m_in:
        if array_1[i] <= array_2[j]:
            array_3.append(array_1[i])
            i += 1
            counter += 1
        else:
            array_3.append(array_2[j])
            j += 1
            counter += 1
        if i == n_in:
            while j < m_in:
                array_3. append(array_2[j])
                j += 1
                return array_3           
        if  j == m_in:
            while i < n_in:
                array_3.append(array_1[i])
                i += 1
                return array_3

def main():
    n = int(input("Please enter a number for the length of the first array: "))
    m = int(input("Please enter a number for the length of the second array: "))
    array_1 = []
    array_2 = []
    counter = 0
    while counter < n:
        array_1.append(random.randint(0, 50))
        counter += 1
    counter = 0
    while counter < m:
        array_2.append(random.randint(0, 50))
        counter += 1
    arrayS_1 = sorted(array_1)
    arrayS_2 = sorted(array_2)
    array_3 = merge_sort(arrayS_1, arrayS_2, n, m)
    print("The combination of the first and second array is: ", array_3)

if __name__ == "__main__":
    main()
