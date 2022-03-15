import tkinter as tk

def evaluate(event):
    myString = entry.get()
    char1 = myString[3]
    char2 = myString[2]
    char3 = myString[1]
    char4 = myString[0]
    reverseString = str(char1+char2+char3+char4)
    #reverseString = myString[::-1] could be used if we wanted to be reverse
    #strings of any length, but this hasnt been taught yet so I didn't use

    results = reverseString
    res.configure(text = "The Reverse String is: " + results)

w = tk.Tk()
tk.Label(w, text="Please Enter a string with 4 characters  (e.g. ABCD):").pack()
entry = tk.Entry(w)
myString = entry.get()
print(myString)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()

