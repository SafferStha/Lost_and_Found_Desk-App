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

# Search Frame
search_frame = Frame(root, bg="black", height=60)
search_frame.pack(fill=X, pady=(0, 20))
search_frame.pack_propagate(False)

# Search Label and Entry
search_label = Label(search_frame, text="Search:", font=("Arial", 12), bg="black", fg="white")
search_label.pack(side=LEFT, padx=(50, 10), pady=15)

search_entry = Entry(search_frame, width=50, font=("Arial", 11), relief="solid", bd=1)
search_entry.pack(side=LEFT, pady=15)

search_btn = Button(search_frame, text="Search", width=10, font=("Arial", 10), bg="#2196F3", fg="white", relief="flat", cursor="hand2")
search_btn.pack(side=LEFT, padx=10, pady=15)

show_all_btn = Button(search_frame, text="Show All", width=10, font=("Arial", 10), bg="#E91E63", fg="white", relief="flat", cursor="hand2")
show_all_btn.pack(side=LEFT, padx=5, pady=15)

# Table Frame
table_frame = Frame(root, bg="white")
table_frame.pack(fill=BOTH, expand=True, padx=50, pady=(0, 50))

# Create Treeview for table
columns = ("ID", "Item Name", "Category", "Type", "Date", "Location", "Status")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

# Define column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(fill=BOTH, expand=True)

root.mainloop()