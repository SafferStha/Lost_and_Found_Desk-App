from tkinter import *
root = Tk()
root.geometry("1200x700")
root.title("Lost and Found Desk - Admin Login Panel")
root.resizable(0, 0)
root.configure(bg="black")

# Global variables to track if windows are open
lost_window = None
found_window = None

# Function to handle lost item 
def lost():
    global lost_window
    
    # Check if window is already open
    if lost_window is not None and lost_window.winfo_exists():
        lost_window.lift()  # Bring existing window to front
        return
    
    lost_window = Toplevel()  # --> Create new window
    lost_window.title("Update records")
    lost_window.geometry("800x700")
    # Background color
    lost_window.configure(bg="black")
    
    # Handle window close event to reset the global variable
    def on_closing():
        global lost_window
        lost_window.destroy()
        lost_window = None
    
    lost_window.protocol("WM_DELETE_WINDOW", on_closing)


    lbl_registration = Label(lost_window, text="Lost Item Details", font=("aerial", 16, "bold"), bg="blue", fg="white")
    lbl_registration.place(x=120, y=20)

    lbl_item_name = Label(lost_window, text="Item Name", bg="black", font=("aerial", 12), fg="white")
    lbl_item_name.place(x=50, y=80)
    item_name = Entry(lost_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    item_name.place(x=180, y=80)

    lbl_item_category = Label(lost_window, text="Item Category", bg="black", font=("aerial", 12), fg="white")
    lbl_item_category.place(x=50, y=130)
    item_category = Entry(lost_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    item_category.place(x=180, y=130)

    lbl_date_lost = Label(lost_window, text="Date Lost", bg="black", font=("aerial", 12), fg="white")
    lbl_date_lost.place(x=50, y=180)
    date_lost = Entry(lost_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    date_lost.place(x=180, y=180)

    lbl_location_lost = Label(lost_window, text="Location Lost", bg="black", font=("aerial", 12), fg="white")
    lbl_location_lost.place(x=50, y=230)
    location_lost = Entry(lost_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    location_lost.place(x=180, y=230)

    # description
    lbl_description = Label(lost_window, text="Description", bg="black", font=("aerial", 12), fg="white")
    lbl_description.place(x=50, y=280)
    description = Text(lost_window, width=35, height=10, font=("aerial", 11), bd=2, relief="raised")
    description.place(x=180, y=280)

    # submit button
    submit_button = Button(lost_window, text="Submit", width=15, font=("aerial", 12), bg="green", fg="white", bd=2, relief="raised")
    submit_button.place(x=200, y=500)

def found():
    global found_window

    # Check if window is already open
    if found_window is not None and found_window.winfo_exists():
        found_window.lift()  # Bring existing window to front
        return

    found_window = Toplevel()  # --> Create new window
    found_window.configure(bg="black") # --> configure method is used to set the background color of the window
    found_window.title("Found Item Details")
    found_window.geometry("800x700")

    # Handle window close event to reset the global variable
    def on_closing():
        global found_window
        found_window.destroy()
        found_window = None

    found_window.protocol("WM_DELETE_WINDOW", on_closing)

    lbl_registration = Label(found_window, text="Found Item Details", font=("aerial", 16, "bold"), bg="blue", fg="white")
    lbl_registration.place(x=120, y=20)

    lbl_item_name = Label(found_window, text="Item Name", bg="black", font=("aerial", 12), fg="white")
    lbl_item_name.place(x=50, y=80)
    item_name = Entry(found_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    item_name.place(x=180, y=80)

    lbl_item_category = Label(found_window, text="Item Category", bg="black", font=("aerial", 12), fg="white")
    lbl_item_category.place(x=50, y=130)
    item_category = Entry(found_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    item_category.place(x=180, y=130)

    lbl_date_found = Label(found_window, text="Date Found", bg="black", font=("aerial", 12), fg="white")
    lbl_date_found.place(x=50, y=180)
    date_found = Entry(found_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    date_found.place(x=180, y=180)

    lbl_location_found = Label(found_window, text="Location Found", bg="black", font=("aerial", 12), fg="white")
    lbl_location_found.place(x=50, y=230)
    location_found = Entry(found_window, width=35, font=("aerial", 11), bd=2, relief="raised")
    location_found.place(x=180, y=230)

    # description
    lbl_description = Label(found_window, text="Description", bg="black", font=("aerial", 12), fg="white")
    lbl_description.place(x=50, y=280)
    description = Text(found_window, width=35, height=10, font=("aerial", 11), bd=2, relief="raised")
    description.place(x=180, y=280)

    # submit button
    submit_button = Button(found_window, text="Submit", width=15, font=("aerial", 12), bg="green", fg="white", bd=2, relief="raised")
    submit_button.place(x=200, y=500)


# Main window setup
lbl_registration = Label(root, text="Admin Control Panel", font=("aerial", 16, "bold"), bg="blue", fg="white")
lbl_registration.place(x=120, y=20)


# name
lbl_fullname = Label(root, text="Full Name", bg="black", font=("aerial", 12), fg="white")
lbl_fullname.place(x=50, y=80)
full_name = Entry(root, width=35, font=("aerial", 11))
full_name.place(x=180, y=80)

# email
lbl_email = Label(root, text="Email", bg="black", font=("aerial", 12), fg="white")
lbl_email.place(x=50, y=120)
email = Entry(root, width=35, font=("aerial", 11))
email.place(x=180, y=120)

# phone
lbl_phone = Label(root, text="Phone", bg="black", font=("aerial", 12), fg="white")
lbl_phone.place(x=50, y=160)
phone = Entry(root, width=35, font=("aerial", 11))
phone.place(x=180, y=160)

# item type radio buttons
lbl_item_type = Label(root, text="Item Type", bg="black", font=("aerial", 12), fg="white")
lbl_item_type.place(x=50, y=200)

#  buttons for item type
lost_btn = Button(root, text="Lost", width=10, font=("aerial", 11), bg="lightblue", padx=5, pady=5, command=lost)
lost_btn.place(x=180, y=200)
found_btn = Button(root, text="Found", width=10, font=("aerial", 11), bg="lightgreen", padx=5, pady=5, command=found)
found_btn.place(x=300, y=200)



root.mainloop()