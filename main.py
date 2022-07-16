from tabnanny import check
from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Bruteforce by HackTeam")
root.resizable(0, 0)

def checkstatus():
    file = open("basepass.txt", "r")
    passwords = file.readlines()
    passwords = list(map(str.strip, passwords))
    file.close()
    password = entrypass.get()
    if password in passwords:
        checkstatus["text"] = "Password is detected"
    else:
        checkstatus["text"] = "Password not detected"
        file = open("passwords.txt", "a")
        file.write("\n"+password+"\n")
        file.close()


root["bg"]="black"

labelmain = Label(text="Bruteforce by HackTeam", font="Calibri 20", bg="black", fg="dark green")
labelmain.place(x=270, y=10)

labelpass = Label(text = "Enter your password:", font="Calibri 15", bg="black", fg="dark green")
labelpass.place(x=320, y=65)

entrypass = Entry(width=20, font="Calibri 20", bg="dim gray", fg="dark green")
entrypass.place(x=270, y=100)

btnpasscheck = Button(text="Check", bg="dim grey", fg="black", font="Calibri 15", activebackground='dark green', command=checkstatus)
btnpasscheck.place(x=375, y=150)

checkstatus = Label(text="", font="Calibri 20", bg="black", fg="dark green")
checkstatus.place(x=285, y=350)

root.mainloop()
