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
