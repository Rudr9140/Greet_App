
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime

def get_greeting():
    current_hour = datetime.now().hour
    if (current_hour < 12):
        return "Morning"
    elif (current_hour < 18):
        return "Afternoon"
    else:
        return "Evening"

def animate_text(text, label, root):
    def display_text(i=0):
        if i < len(text):
            label.config(text=text[:i+1])
            root.after(50, display_text, i+1)
        else:
            root.after(500, root.destroy)
    
    display_text()

# Create main window
root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.overrideredirect(0)

# Create a label to display the animation
label = ttk.Label(root, font=("Helvetica", 100), anchor="center")
label.configure(background="black", foreground="white")
label.pack(expand=True)

# Enable dark theme
root.configure(bg="black")

# User-specific variables
user_name = "USER"  # replace with actual user_name entered from external window
smiling_emoji = "\U0001F603"

# Create the message
greeting_according_to_time = get_greeting()
message = "Hello " + user_name + ",\nGood " + greeting_according_to_time + ",\nYou're Welcome " + smiling_emoji

# Start the animation
animate_text(message, label, root)

# Start the Tkinter event loop
root.mainloop()
