from tkinter import *

root = Tk()  # a window was formed
root.geometry("500x300")
root.resizable(FALSE, FALSE)
root.title("Li Foong's Project - Website Blocker")
# resizable(height, width),
# make it not resizable -> false, false or 0,0

Label(root, text="Website Blocker", font="arial 20 bold").pack()
Label(root, text="Li Foong's Project", font="arial 10 bold").pack(side=BOTTOM)
# Label() - one or more lines of text that cannot be changed

host_path = "C:\Windows\System32\drivers\etc\hosts"
ip_address = "127.0.0.1"
# this is loopback ip address that can be known as localhost
# it is the universal home address for all computer

Label(root, text="Enter Website: ", font="arial 13 bold").place(x=5, y=60)
Websites = Text(root, font="arial 10", height=2, width=40, wrap=WORD, padx=5, pady=5)
# Text() -> multi-line text fileds
# wrap = WORD -> break the line
# Padx adds more room to the widget's left and right sides
# Pady adds extra space to the top and bottom
Websites.place(x=140, y=60)


# make "Block" function
# .get() read input from Text widget
# "1.0" means input will be read from line 1 (character zero)
# END read until the end of the text box can be reached, but it adds a new line
# "end-1c" -1c deletes 1 character
def Blocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    # returns all websites users have input

    # save the list in a website with open, the open statement terminate
    # the file handler. r+ will read and write the file
    with open(host_path, "r+") as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text="Already Blocked", font="arial 12 bold").place(x=200, y=200)
                pass

            else:
                host_file.write(ip_address + "" + website + "\n")
                Label(root, text="Blocked", font="arial 12 bold").place(x=230, y=200)


#create block button that execute the function
block = Button(root, text='Block', font='arial 12 bold', pady=5, command=Blocker, width=6, bg='royal blue1', activebackground='sky blue')
block.place(x=230, y=150)

root.mainloop()