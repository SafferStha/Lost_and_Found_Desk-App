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

root.mainloop()