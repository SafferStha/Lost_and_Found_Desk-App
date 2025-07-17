from tkinter import *

root = Tk()
root.title("Lost and Found Desk - Login")
root.geometry("400x300")

# entry fields for username and password using grid
Label(root, text="Username:").grid(row=0, column=0 )
username_entry = Entry(root)
username_entry.grid(row=0, column=1)

Label(root, text="Password:").grid(row=1, column=0)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

# login button
login_button = Button(root, text="Login")
login_button.grid(row=2, column=0)

root.mainloop()