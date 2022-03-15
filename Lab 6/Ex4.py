def All_uppercase(s_in):
    i = 0
    s_in = list(s_in)
    for char in s_in:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
            s_in[i] = char
            i +=1
        else:
            i += 1
    s_cap = ""
    return s_cap.join(s_in)


def main():
    s = str(input("Please enter a string: "))
    capstr = All_uppercase(s)
    print(capstr)


if __name__ == "__main__":
    main()