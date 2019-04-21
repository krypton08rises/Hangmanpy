from tkinter import *

root = Tk()
root.geometry('1280*720')
root.title("Hangman")

f1 = Frame()

text = "Admin please enter line:"
Label(f1, text).grid(row=0)
line = Entry(root)
line.grid(row=0, column=1)
text = "All players have 6 tries"
Label(root, text).grid(row=1)
ch = Entry(root)
ch.grid(row=1, column=1)
count = 6
ans = ''
while count!=0:
    ch = input()
    if ch.isalpha() != 1 | len(ch) != 1:
        print("Please enter alphabet!")
        continue

    for i in line:
        if i == ch:
            ans = ans + i
            text = "Your guess was right!!!"
            label1 = Label(root, text)
            label1.pack()
            continue
        else:
            ans = ans + _
            text = "Your guess was wrong!!!"
            label2 = Label(root, text)
            label2.pack()
            count = count-1
root.mainloop()