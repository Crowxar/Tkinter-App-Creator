# This is a generated script made with Tkinter App Creator by Crowxar - https://crowxar.github.io/
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("write_test")



example_label_widget = ttk.Label(app, text="Thanks for using Tkinter App Creator!",
                                 font=("Arial", 18),
                                 anchor="center")
example_label_widget.pack(expand=True, fill="both")


app.update_idletasks()
app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
pos_x = (screen_width - app_width) // 2
pos_y = (screen_height - app_height) // 2
app.geometry(f"{app_width}x{app_height}+{pos_x}+{pos_y}")
app.mainloop()