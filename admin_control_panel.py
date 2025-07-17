from tkinter import *
root = Tk()
root.geometry("1000x700")
root.title("Lost & Found Desk - Admin Panel")
root.resizable(0, 0)

lbl_registration = Label(root, text="Admin Control Panel", font=("aerial", 16, "bold"), bg="blue", fg="white")
lbl_registration.place(x=120, y=20)

# name
lbl_fullname = Label(root, text="Full Name", bg="white", font=("aerial", 12))
lbl_fullname.place(x=50, y=80)
full_name = Entry(root, width=35, font=("aerial", 11))
full_name.place(x=180, y=80)

# email
lbl_email = Label(root, text="Email", bg="white", font=("aerial", 12))
lbl_email.place(x=50, y=120)
email = Entry(root, width=35, font=("aerial", 11))
email.place(x=180, y=120)

# phone
lbl_phone = Label(root, text="Phone", bg="white", font=("aerial", 12))
lbl_phone.place(x=50, y=160)
phone = Entry(root, width=35, font=("aerial", 11))
phone.place(x=180, y=160)

# item type 
lbl_item_type = Label(root, text="Item Type", bg="white", font=("aerial", 12))
lbl_item_type.place(x=50, y=200)

#  buttons for item type
lost_btn = Button(root, text="Lost", width=10, font=("aerial", 11), bg="lightblue", padx=5, pady=5)
lost_btn.place(x=180, y=200)
found_btn = Button(root, text="Found", width=10, font=("aerial", 11), bg="lightgreen", padx=5, pady=5)
found_btn.place(x=300, y=200)


root.mainloop()