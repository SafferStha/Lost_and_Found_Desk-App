from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1200x800")
root.title("Lost & Found - Welcome User")
root.resizable(0, 0)
root.configure(bg="black")

# Header Frame
header_frame = Frame(root, bg="#4A9EFF", height=80)
header_frame.pack(fill=X)
header_frame.pack_propagate(False)

# Header Label
header_label = Label(header_frame, text="Lost & Found Desk - Welcome User", font=("Arial", 20, "bold"), bg="#4A9EFF", fg="white")
header_label.pack(pady=20)

root.mainloop()

# Button Frame
button_frame = Frame(root, bg="black", height=80)
button_frame.pack(fill=X, pady=20)
button_frame.pack_propagate(False)

# Action Buttons with connected functions
report_lost_btn = Button(button_frame, text="Report Lost Item", width=18, height=2, font=("Arial", 12, "bold"), bg="#FFB84D", fg="black", relief="flat", cursor="hand2")
report_lost_btn.pack(side=LEFT, padx=30, pady=10)

report_found_btn = Button(button_frame, text="Report Found Item", width=18, height=2, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", cursor="hand2")
report_found_btn.pack(side=LEFT, padx=30, pady=10)

search_items_btn = Button(button_frame, text="Search Items", width=18, height=2, font=("Arial", 12, "bold"), bg="#00BCD4", fg="white", relief="flat", cursor="hand2")
search_items_btn.pack(side=LEFT, padx=30, pady=10)