from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import os

root = Tk()
root.title("Lost & Found Desktop - Login")
root.geometry("1000x600")
root.resizable(0, 0)

# Setting the background color
canvas = Canvas(root, width=900, height=600, highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Drawing a gradient from darkblue to skyblue/lightblue
def get_gradient_color(i):
    # Gradient from dark blue (#001848) to light blue (#87ceeb)
    start_rgb = (0, 24, 72)      # dark blue
    end_rgb = (135, 206, 235)    # light blue (skyblue)
    ratio = i / 599
    r = 30 + int(i * 0.2)
    g = 30 + int(i * 0.1)
    b = 100 + int(i * 0.2)
    r, g, b = min(r, 255), min(g, 255), min(b, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

root.update_idletasks()  # Ensure geometry is updated
window_width = root.winfo_width()
for i in range(600):  # window height
    color = get_gradient_color(i)
    canvas.create_line(0, i, window_width, i, fill=color)
    canvas.create_line(0, i+1, window_width, i+1, fill=color)  # fill the gap for smoother gradient

for i in range(600):  # window height
    color = get_gradient_color(i)
    canvas.create_line(0, i, 1000, i, fill=color)
    canvas.create_line(0, i+1, 1000, i+1, fill=color)  # fill the gap for smoother gradient

# Global variable for register window
register_window = None

# Function to open admin control panel
def open_admin_panel():
    try:
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        admin_panel_path = os.path.join(current_dir, "admin_control_panel.py")
        
        # Clear login fields for security
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
        # Hide the login window
        root.withdraw()
        
        # Open admin control panel
        subprocess.run([sys.executable, admin_panel_path])
        
        # Show login window again when admin panel closes
        root.deiconify()
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not open admin panel: {str(e)}")
        root.deiconify()  # Show login window if error occurs

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
        open_admin_panel()  # Open admin control panel
    else:
        messagebox.showerror("Error", "Invalid username or password!")
        password_entry.delete(0, END)  # Clearing password field for security

# function for registering a new user
def register_user():
    global register_window
    if register_window is not None and register_window.winfo_exists():
        register_window.lift()
        return
    register_window = Toplevel()
    register_window.title("User Registration")
    register_window.geometry("500x600")
    register_window.resizable(0, 0)
    register_window.grab_set()  # Make window modal
    register_window.transient(root)  # Keep on top of parent

    # Create canvas for gradient background
    reg_canvas = Canvas(register_window, width=500, height=600, highlightthickness=0,)
    reg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
    def get_gradient_color_1(i):
        # Gradient from dark blue (#001848) to light blue (#87ceeb)
        start_rgb = (0, 24, 72)      # dark blue
        end_rgb = (135, 206, 235)    # light blue (skyblue)
        ratio = i / 599
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
        return f'#{r:02x}{g:02x}{b:02x}'
    get_gradient_color_1
    for i in range(600):  # window height
        color = get_gradient_color_1(i)
        reg_canvas.create_line(0, i, 500, i, fill=color)
        reg_canvas.create_line(0, i+1, 500, i+1, fill=color)  # fill the gap for smoother gradient

    def on_closing():
        global register_window
        register_window.destroy()
        register_window = None

    register_window.protocol("WM_DELETE_WINDOW", on_closing)

    lbl_registration = Label(register_window, text="User Registration", font=("Impact", 22), fg="white", bg=get_gradient_color_1(40))
    reg_canvas.create_window(250, 40, window=lbl_registration, anchor="center")

    # Full Name
    lbl_full_name = Label(register_window, text="Full Name:", font=("Arial", 12, "bold"), fg="white", bg=get_gradient_color_1(120))
    reg_canvas.create_window(150, 120, window=lbl_full_name, anchor="center")
    full_name_entry = Entry(register_window, width=25, font=("Arial", 11), relief="sunken")
    reg_canvas.create_window(350, 120, window=full_name_entry, anchor="center")

    # Email
    lbl_email = Label(register_window, text="Email:", font=("Arial", 12, "bold"), fg="white", bg=get_gradient_color_1(170))
    reg_canvas.create_window(150, 170, window=lbl_email, anchor="center")
    email_entry = Entry(register_window, width=25, font=("Arial", 11),  relief="sunken")
    reg_canvas.create_window(350, 170, window=email_entry, anchor="center")

    # Phone
    lbl_phone = Label(register_window, text="Phone:", font=("Arial", 12, "bold"), fg="white", bg=get_gradient_color_1(220))
    reg_canvas.create_window(150, 220, window=lbl_phone, anchor="center")
    phone_entry = Entry(register_window, width=25, font=("Arial", 11), relief="sunken")
    reg_canvas.create_window(350, 220, window=phone_entry, anchor="center")

    # Password
    lbl_password = Label(register_window, text="Password:", font=("Arial", 12, "bold"), fg="white", bg=get_gradient_color_1(270))
    reg_canvas.create_window(150, 270, window=lbl_password, anchor="center")
    password_entry_reg = Entry(register_window, show="*", width=25, font=("Arial", 11),  relief="sunken")
    reg_canvas.create_window(350, 270, window=password_entry_reg, anchor="center")

    # Confirm Password
    lbl_confirm_password = Label(register_window, text="Confirm Password:", font=("Arial", 12, "bold"), fg="white", bg=get_gradient_color_1(320))
    reg_canvas.create_window(150, 320, window=lbl_confirm_password, anchor="center")
    confirm_password_entry = Entry(register_window, show="*", width=25, font=("Arial", 11), relief="sunken")
    reg_canvas.create_window(350, 320, window=confirm_password_entry, anchor="center")

    def handle_registration():
        full_name = full_name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        password = password_entry_reg.get()
        confirm_password = confirm_password_entry.get()
        if not all([full_name, email, phone, password, confirm_password]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Please enter a valid email address!")
            return
        if not phone.isdigit() or len(phone) < 10:
            messagebox.showerror("Error", "Please enter a valid phone number (at least 10 digits)!")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return
        messagebox.showinfo("Success", f"Registration successful!\nWelcome, {full_name}!")
        full_name_entry.delete(0, END)
        email_entry.delete(0, END)
        phone_entry.delete(0, END)
        password_entry_reg.delete(0, END)
        confirm_password_entry.delete(0, END)
        on_closing()

    # Center the buttons
    submit_button = Button(register_window, text="Register", width=15, font=("Arial", 12, "bold"), bg="lightgreen", fg="black", command=handle_registration)
    reg_canvas.create_window(150, 410, window=submit_button, anchor="center")
    cancel_button = Button(register_window, text="Cancel", width=15, font=("Arial", 12, "bold"), bg="lightcoral", fg="black", command=on_closing)
    reg_canvas.create_window(350, 410, window=cancel_button, anchor="center")

    # Add footer similar to login page
    footer_reg = Label(register_window, text="Join the Lost & Found community!", font=("Arial", 12, "bold"), fg="#111111", bg=get_gradient_color_1(500))
    reg_canvas.create_window(250, 500, window=footer_reg, anchor="center")

# --- Login fields directly on canvas ---
# Username field - properly centered
username_label = Label(root, text="Username", font=("Calibri", 14), bg=get_gradient_color(250), fg="white")
canvas.create_window(400, 265, window=username_label, anchor="center")

username_entry = Entry(root, width=27, font=("Calibri", 14), relief="sunken", )
canvas.create_window(498, 290, window=username_entry, anchor="center")

# Password field - properly centered
password_label = Label(root, text="Password", font=("Calibri", 15), bg=get_gradient_color(300), fg="white")
canvas.create_window(400, 325, window=password_label, anchor="center")

password_entry = Entry(root, show="*", width=27, font=("Calibri", 14), relief="sunken", )
canvas.create_window(498, 350, window=password_entry, anchor="center")

# Buttons - centered horizontally
login_btn = Button(root, text="Login", width=10, fg="black", font=("Arial", 13), bg="skyblue", command=handle_login)
canvas.create_window(500, 430, window=login_btn, anchor="center")

register_btn = Button(root, text="Register", width=12, fg="black", font=("Arial", 13), bg="lightgreen", command=register_user)
canvas.create_window(500, 480, window=register_btn, anchor="center")

# --- App name typewriter effect ---
def blink_text_effect(current_text, next_text, canvas, item_id, delay=3000, fade_steps=10, on_complete=None):
    # Set the canvas item's text to the current text
    canvas.itemconfig(item_id, text=current_text)
    # Fade colors from white to transparent and back
    def fade_out(step):
        # Fade from white to background color (#3f2e85)
        def blend_color(c1, c2, t):
            return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        white_rgb = (255, 255, 255)
        # Convert #3f2e85 to RGB
        bg_rgb = (63, 46, 133)  # #3f2e85 in RGB
        t = step / fade_steps
        r, g, b = blend_color(white_rgb, bg_rgb, t)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.itemconfig(item_id, fill=color)
        if step < fade_steps:
            root.after(delay // (fade_steps * 2), fade_out, step + 1)
        else:
            # Text is now fully faded out, change to next text and fade in
            canvas.itemconfig(item_id, text=next_text)
            fade_in(0)

    def fade_in(step):
        # Fade from background color (#3f2e85) to white
        def blend_color(c1, c2, t):
            return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        # Convert #3f2e85 to RGB
        bg_rgb = (63, 46, 133)  # #3f2e85 in RGB
        white_rgb = (255, 255, 255)
        t = step / fade_steps
        r, g, b = blend_color(bg_rgb, white_rgb, t)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.itemconfig(item_id, fill=color)
        if step < fade_steps:
            root.after(delay // (fade_steps * 2), fade_in, step + 1)
        else:
            # Text is now fully white, wait 2.5 seconds before completing the cycle
            root.after(2500, lambda: on_complete() if on_complete else None)
    
    # Start the fade out effect
    fade_out(0)

def typewriter_effect(text, canvas, item_id, delay=100, on_complete=None):
    """
    Displays the given text on a Tkinter canvas item with a typewriter animation effect.

    Args:
        text (str): The text to display.
        canvas (tkinter.Canvas): The canvas where the text will be shown.
        item_id (int): The canvas text item ID to update.
        delay (int, optional): Delay in milliseconds between each character. Defaults to 100.
        on_complete (callable, optional): Function to call when animation completes. Defaults to None.
    """
    displayed_text = ""
    def update_text(i=0):
        nonlocal displayed_text
        if i < len(text):
            displayed_text += text[i]
            canvas.itemconfig(item_id, text=displayed_text)
            root.after(delay, update_text, i+1)
        else:
            if on_complete:
                on_complete()
    update_text()

# Center the text horizontally (500 is center of 1000px window)
app_name_text = canvas.create_text(500, 90, text="", font=("Impact", 35, "bold"), fill="white", anchor="center")
app_name_text2 = canvas.create_text(500, 135, text="", font=("Lato", 20), fill="white", anchor="center")
typewriter_effect_canvas(
    "Lost & Found Desktop App", canvas, app_name_text,
    delay=100,
    on_complete=lambda: typewriter_effect(
        "Connecting what's lost with those who are looking!", canvas, app_name_text2, delay=100,
        on_complete=lambda: run_blink_sequence(0, is_first=True)
    )
)
# --- Footer ---
footer_text = canvas.create_text(
    500, 520,  # x, y position (centered at bottom; 500 is center for 1000px width)
    text="Powered by TEAM DOBERMANs",
    font=("Courier New", 12, "bold"),
    fill="#222222",
    anchor="center"
)


root.mainloop()