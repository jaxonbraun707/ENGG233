def is_leap_year(year_in):
    if ((year_in % 4 == 0) and not(year_in % 100 == 0)) or (year_in % 400 == 0):
        return True
    else:
        return False

    
def not_vowel(letter_in):
    x = ord(letter_in)
    if (x == 65) or (x == 97) or (x == 69) or (x == 101) or (x == 73) or (x == 105) or (x == 79) or (x == 111) or (x == 85) or (x == 117):
        return False
    else: 
        return True

def printPrice(float(price_in), str(name_in)):
    print(name_in, end = ": ")
    print("$", end = "")
    print(price_in)


def sizeOf(string_in):
    return len(string_in)
         

def main():
    string = str(input("Enter string: "))
    length = sizeOf(string)
    print(length)


if __name__ == "__main__":
    main()
