from tkinter import *
from tkinter import ttk, messagebox

# Main window setup
root = Tk()
root.geometry("1200x700")
root.title("Lost & Found - Admin Panel")
root.resizable(0, 0)
root.configure(bg="white")

# Global variables for window management
add_lost_window = None
add_found_window = None

# Header Frame
header_frame = Frame(root, bg="#2196F3", height=80)
header_frame.pack(fill=X)
header_frame.pack_propagate(False)

# Header Label
header_label = Label(header_frame, text="Admin Panel - Welcome Administrator", 
                    font=("Arial", 20, "bold"), bg="#2196F3", fg="white")
header_label.pack(pady=20)


# Create Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Items Management Tab
items_frame = Frame(notebook, bg="white")
notebook.add(items_frame, text="Items Management")

# Users Management Tab
users_frame = Frame(notebook, bg="white")
notebook.add(users_frame, text="Users Management")

# Reports Tab
reports_frame = Frame(notebook, bg="white")
notebook.add(reports_frame, text="Reports")

# Style the notebook tabs
style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook.Tab", font=("Arial", 12, "bold"), padding=[20, 10])

# Items Management Tab Content
# Functions for adding items
def add_lost_item():
    global add_lost_window
    if add_lost_window is not None and add_lost_window.winfo_exists():
        add_lost_window.lift()
        return
    
    add_lost_window = Toplevel()
    add_lost_window.title("Add Lost Item")
    add_lost_window.geometry("600x550")
    add_lost_window.resizable(0, 0)
    add_lost_window.configure(bg="black")
    add_lost_window.grab_set()
    add_lost_window.transient(root)
    
    def on_closing():
        global add_lost_window
        add_lost_window.destroy()
        add_lost_window = None
    
    add_lost_window.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Header
    header_frame = Frame(add_lost_window, bg="#5DADE2", height=60)
    header_frame.pack(fill=X)
    header_frame.pack_propagate(False)
    
    Label(header_frame, text="Lost Item Details", font=("Arial", 18, "bold"), 
          bg="#5DADE2", fg="white").pack(pady=15)
    
    # Form frame
    form_frame = Frame(add_lost_window, bg="black")
    form_frame.pack(fill=BOTH, expand=True, padx=40, pady=30)
    
    # Basic form fields
    y_pos = 50
    
    Label(form_frame, text="Item Name:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=y_pos)
    item_name = Entry(form_frame, width=30, font=("Arial", 11), bd=1, relief="solid")
    item_name.place(x=200, y=y_pos)
    
    y_pos += 40
    Label(form_frame, text="Category:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=y_pos)
    category = Entry(form_frame, width=30, font=("Arial", 11), bd=1, relief="solid")
    category.place(x=200, y=y_pos)
    
    def submit_lost_item():
        if not item_name.get().strip() or not category.get().strip():
            messagebox.showerror("Error", "Please fill required fields!")
            return
        messagebox.showinfo("Success", "Lost item added successfully!")
        on_closing()
    
    # Buttons
    y_pos += 100
    Button(form_frame, text="Submit", font=("Arial", 12, "bold"), bg="#28a745", fg="white", 
           width=12, command=submit_lost_item).place(x=200, y=y_pos)
    Button(form_frame, text="Cancel", font=("Arial", 12, "bold"), bg="#dc3545", fg="white", 
           width=12, command=on_closing).place(x=350, y=y_pos)
    
# Basic refresh function
def refresh_table():
    # Clear existing items
    for item in tree.get_children():
        tree.delete(item)
    # Table is now empty - ready for real data
    messagebox.showinfo("Refresh", "Table refreshed successfully!")

# Action buttons frame
action_frame = Frame(items_frame, bg="white", height=80)
action_frame.pack(fill=X, padx=20, pady=10)
action_frame.pack_propagate(False)

# Action buttons
Button(action_frame, text="Add Lost Item", font=("Arial", 12, "bold"), bg="#FF9800", 
       fg="white", width=15, height=2,command=add_lost_item).pack(side=LEFT, padx=10, pady=10)

Button(action_frame, text="Add Found Item", font=("Arial", 12, "bold"), bg="#4CAF50", 
       fg="white", width=15, height=2).pack(side=LEFT, padx=10, pady=10)

Button(action_frame, text="Refresh", font=("Arial", 12, "bold"), bg="#2196F3", 
       fg="white", width=15, height=2, command=refresh_table).pack(side=LEFT, padx=10, pady=10)

# Table frame
table_frame = Frame(items_frame, bg="white")
table_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Create Treeview for items table
columns = ("ID", "Item Name", "Category", "Type", "Date", "Status")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)

# Define column headings and widths
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor=CENTER if col in ["ID", "Type", "Status"] else W)

# Add scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Pack the treeview and scrollbar
tree.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Users Management Tab Content
def load_users():
    # Clear existing users
    for item in users_tree.get_children():
        users_tree.delete(item)
    
    # Users table is now empty - ready for real data

# Users table
users_columns = ("ID", "Full Name", "Email", "Phone", "Type")
users_tree = ttk.Treeview(users_frame, columns=users_columns, show="headings", height=20)

for col in users_columns:
    users_tree.heading(col, text=col)
    users_tree.column(col, width=200, anchor=W)

users_tree.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Reports Tab Content
# Create simple stats display
reports_content = Frame(reports_frame, bg="white")
reports_content.pack(fill=BOTH, expand=True, padx=50, pady=50)

# Stats display
stats_text = """
Total Items: 0
Lost Items: 0
Found Items: 0
Active Items: 0
Claimed Items: 0
"""

stats_label = Label(reports_content, text=stats_text, font=("Arial", 14), 
                   bg="white", fg="black", justify=LEFT)
stats_label.pack(pady=50)


# Load initial data
refresh_table()
load_users()

root.mainloop()