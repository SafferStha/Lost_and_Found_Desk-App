from tkinter import *
from tkinter import ttk

# Main window setup
root = Tk()
root.geometry("1200x700")
root.title("Lost & Found - Admin Panel")
root.resizable(0, 0)
root.configure(bg="white")

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

root.mainloop()