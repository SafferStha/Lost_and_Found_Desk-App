from tkinter import *

root = Tk()
root.title("Lost and Found Desk - Login")
root.geometry("900x600")
root.resizable(0, 0)

# Setting the background color
root.configure(bg="black")

# Creating a frame to box the login form
login_frame = Frame(root, relief="raised", bd=2, padx=20, pady=20)
login_frame.grid(row=0, column=0, padx=50, pady=170, sticky="e")

#for Login text
Label(login_frame, text="Login Here", font=("Arial", 24, "bold")).grid(row=0, column=0, columnspan=2, pady=8, sticky="w")

# entry fields for username and password using grid within the frame
Label(login_frame, text="Username:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
username_entry = Entry(login_frame, width=30, relief="sunken", bd=2)
username_entry.grid(row=1, column=1, pady=10)

Label(login_frame, text="Password:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
password_entry = Entry(login_frame, show="*", width=30, relief="sunken", bd=2)
password_entry.grid(row=2, column=1, pady=10)

# login button
login_button = Button(login_frame, text="Login", width=15, relief="raised", bd=2)
login_button.grid(row=3, column=1, columnspan=2, pady=5, sticky="e")

# text
Label(root, text="Lost and Found Desk App", font=("Arial", 25, "italic", "bold"), bg="black", fg="white").grid(row=0, column=3, columnspan=2, pady=1, sticky="e")

root.mainloop()