m_type = str(input("Do you want an 'open' or 'closed' mortgage?: "))
m_term = str(input("Do you want a '1 yr', '3 yr', or '5 yr' term?: "))

if(m_type == "open"):
    if(m_term == "1 yr"):
        print("Your mortgage rate will be 7.10%")
    elif(m_term == "3 yr"):
        print("Your mortgage rate will be 7.50%")
    elif(m_term == "5 yr"):
        print("Your desired mortgage is unavaible, please try again")
    else:
        print("invalid term duration, please try again")
elif(m_type == "closed"):
    if(m_term == "1 yr"):
        print("Your mortgage rate will be 5.30%")
    elif(m_term == "3 yr"):
        print("Your mortgage rate will be 5.00%")
    elif(m_term == "5 yr"):
        print("Your mortgage rate will be 5.75%")
    else:
        print("Invalid term duration, please try again")
else:
    print("Invalid mortage type, please try again")
   