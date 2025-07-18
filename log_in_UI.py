from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Lost & Found Desk - Login")
root.geometry("900x600")
root.resizable(0, 0)


# Setting the background color
root.configure(bg="black")

# Global variable for register window
register_window = None

# Function to handle login
def handle_login():
    username = username_entry.get().strip()
    password = password_entry.get()
    
    # Basic validation
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password!")
        return
    
    
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Success", f"Welcome back, {username}!")
        
    else:
        messagebox.showerror("Error", "Invalid username or password!")
        password_entry.delete(0, END)  # Clearing password field for security

# function for registering a new user
def register_user():

    global register_window

    #  for Checking if window is already open
    if register_window is not None and register_window.winfo_exists():
        register_window.lift()  # Bringing existing window to front
        return

    register_window = Toplevel()  # --> Creating new window
    register_window.configure(bg="black") # --> configure method is used to set the background color of the window
    register_window.title("User Registration")
    register_window.geometry("500x600")

    # to Handle window close event to reset the global variable
    def on_closing():
        global register_window
        register_window.destroy()
        register_window = None

    register_window.protocol("WM_DELETE_WINDOW", on_closing)

    # Main heading
    lbl_registration = Label(register_window, text="User Registration", font=("Arial", 18, "bold"), bg="blue", fg="white")
    lbl_registration.place(x=150, y=20)

    # Full Name
    lbl_full_name = Label(register_window, text="Full Name:", bg="black", font=("Arial", 12), fg="white")
    lbl_full_name.place(x=50, y=80)
    full_name_entry = Entry(register_window, width=35, font=("Arial", 11), bd=2, relief="raised")
    full_name_entry.place(x=180, y=80)

    # Email
    lbl_email = Label(register_window, text="Email:", bg="black", font=("Arial", 12), fg="white")
    lbl_email.place(x=50, y=130)
    email_entry = Entry(register_window, width=35, font=("Arial", 11), bd=2, relief="raised")
    email_entry.place(x=180, y=130)

    # Phone
    lbl_phone = Label(register_window, text="Phone:", bg="black", font=("Arial", 12), fg="white")
    lbl_phone.place(x=50, y=180)
    phone_entry = Entry(register_window, width=35, font=("Arial", 11), bd=2, relief="raised")
    phone_entry.place(x=180, y=180)

    # Password
    lbl_password = Label(register_window, text="Password:", bg="black", font=("Arial", 12), fg="white")
    lbl_password.place(x=50, y=230)
    password_entry = Entry(register_window, show="*", width=35, font=("Arial", 11), bd=2, relief="raised")
    password_entry.place(x=180, y=230)

    # Confirm Password
    lbl_confirm_password = Label(register_window, text="Confirm Password:", bg="black", font=("Arial", 12), fg="white")
    lbl_confirm_password.place(x=50, y=280)
    confirm_password_entry = Entry(register_window, show="*", width=35, font=("Arial", 11), bd=2, relief="raised")
    confirm_password_entry.place(x=180, y=280)

    # Function to handle registration
    def handle_registration():
        full_name = full_name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        
        # Basic validation
        if not all([full_name, email, phone, password, confirm_password]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        # Email validation (basic)
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Please enter a valid email address!")
            return
        
        # Phone validation (basic)
        if not phone.isdigit() or len(phone) < 10:
            messagebox.showerror("Error", "Please enter a valid phone number (at least 10 digits)!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return
        
        # If validation passes
        messagebox.showinfo("Success", f"Registration successful!\nWelcome, {full_name}!")
        
        # to Clear all fields after successful registration
        full_name_entry.delete(0, END)
        email_entry.delete(0, END)
        phone_entry.delete(0, END)
        password_entry.delete(0, END)
        confirm_password_entry.delete(0, END)
        
        # Close registration window
        on_closing()
        
    # Submit and Cancel buttons
    submit_button = Button(register_window, text="Register", width=15, font=("Arial", 12), bg="green", fg="white", bd=2, relief="raised", command=handle_registration)
    submit_button.place(x=120, y=350)
    
    cancel_button = Button(register_window, text="Cancel", width=15, font=("Arial", 12), bg="red", fg="white", bd=2, relief="raised", command=on_closing)
    cancel_button.place(x=270, y=350)

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
login_btn = Button(login_frame, text="Login", width=10, font=("Arial", 11), bg="lightblue", padx=5, pady=5, command=handle_login)
login_btn.grid(row=3, column=0, padx=10, pady=20, sticky="e")
# register button
register_btn = Button(login_frame, text="Register", width=12, font=("Arial", 11), bg="lightgreen", padx=5, pady=5, command=register_user)
register_btn.grid(row=3, column=1, padx=10, pady=20, sticky="w")

# text
Label(root, text="Lost & Found Desk App", font=("Arial", 25, "italic", "bold"), bg="black", fg="white").grid(row=0, column=3, columnspan=2, pady=1, sticky="e")

root.mainloop()