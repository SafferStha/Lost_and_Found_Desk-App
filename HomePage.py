import tkinter as tk
import tkinter.ttk as ttk

COLUMNS = ("ID", "Item Name", "Category", "Type", "Date", "Location", "Status")

root = tk.Tk()
root.geometry("1200x700")
root.title("Lost & Found App - Admin Control Panel")
root.resizable(1, 1)

# Header
header = tk.Frame(root, bg="#2996b8", height=60)
header.pack(fill=tk.X)
header_label = tk.Label(header, text="Lost & Found App - Admin Control Panel", bg="#2996b8", fg="white", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

# Top buttons
button_frame = tk.Frame(root, bg="black", height=80)
button_frame.pack(fill=tk.X)

def report_lost():
    print("Report Lost Item button clicked")

def report_found():
    print("Report Found Item button clicked")

def search_items():
    print("Search Items button clicked")

report_lost_btn = tk.Button(button_frame, text="Report Lost Item", bg="#ff2f00", fg="black", font=("Arial", 14), width=18, height=2, command=report_lost)
report_lost_btn.grid(row=0, column=0, padx=20, pady=20)

report_found_btn = tk.Button(button_frame, text="Report Found Item", bg="#2ecc40", fg="white", font=("Arial", 14), width=18, height=2, command=report_found)
report_found_btn.grid(row=0, column=1, padx=20, pady=20)

search_items_btn = tk.Button(button_frame, text="Search Items", bg="#19b5d8", fg="white", font=("Arial", 14), width=18, height=2, command=search_items)
search_items_btn.grid(row=0, column=2, padx=20, pady=20)

# Search bar
search_frame = tk.Frame(root, bg="black", height=50)
search_frame.pack(fill=tk.X)

search_label = tk.Label(search_frame, text="Search:", bg="black", fg="white", font=("Arial", 12))
search_label.place(x=20, y=10)
search_entry = tk.Entry(search_frame, width=40, font=("Arial", 12))
search_entry.place(x=90, y=12)

# Table area
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

columns = ("ID", "Item Name", "Category", "Type", "Date", "Location", "Status")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(fill=tk.BOTH, expand=True)

def search():
    print("Search button clicked")

def show_all():
    print("Show All button clicked")

search_btn = tk.Button(
    search_frame, text="Search", bg="#2996b8", fg="white",
    font=("Arial", 11), width=10, height=1, command=search
)
search_btn.place(x=420, y=10)

show_all_btn = tk.Button(
    search_frame, text="Show All", bg="#b85ca3", fg="white",
    font=("Arial", 11), width=10, height=1, command=show_all
)
show_all_btn.place(x=540, y=10)  # Increased x for more gap

# Define column widths
column_widths = {
    "ID": 60,
    "Item Name": 180,
    "Category": 120,
    "Type": 100,
    "Date": 100,
    "Location": 160,
    "Status": 100
}
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=column_widths.get(col, 120))
tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()