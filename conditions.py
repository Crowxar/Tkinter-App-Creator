base_template_without_regions = """# This is a generated script made with Tkinter App Creator by Crowxar - https://crowxar.github.io/
{Imports}

app = tk.Tk()
app.title("{Title}")

# Widgets
example_label_widget = ttk.Label(app, text="Thanks for using Tkinter App Creator!",
                                 font=("Arial", 18),
                                 anchor="center")
example_label_widget.pack(expand=True, fill="both")

# App Configure
{SizeCon}
{ResizeCon}
{ForceTop}
app.mainloop()
{ClearTerm}"""


base_template_with_regions = """# This is a generated script made with Tkinter App Creator by Crowxar - https://crowxar.github.io/
#region ===Imports===
{Imports}

#endregion

#region ===Debug===
...

#endregion

#region ===Functions===
...

#endregion

#region ===App Init===
app = tk.Tk()
app.title("{Title}")



#endregion

#region ===Widgets===
example_label_widget = ttk.Label(app, text="Thanks for using Tkinter App Creator!",
                                 font=("Arial", 18),
                                 anchor="center")
example_label_widget.pack(expand=True, fill="both")

#endregion

#region ===Bindings===
...

#endregion


#region ===App Settings Configure===
{SizeCon}
{ResizeCon}
{ForceTop}
#endregion

#region ===Run===

app.mainloop()
{ClearTerm}

#endregion"""


fit_sized_cent = """app.update_idletasks()
app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
pos_x = (screen_width - app_width) // 2
pos_y = (screen_height - app_height) // 2
app.geometry(f"{app_width}x{app_height}+{pos_x}+{pos_y}")"""

fit_sized_ncent = """app.update_idletasks()
app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{app_width}x{app_height}")"""

half_size_cent = """screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = screen_width //2
app_height = screen_height // 2
pos_x = (screen_width - app_width) // 2
pos_y = (screen_height - app_height) // 2
app.geometry(f"{app_width}x{app_height}+{pos_x}+{pos_y}")"""

half_size_ncent = """screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = screen_width //2
app_height = screen_height // 2
app.geometry(f"{app_width}x{app_height}")"""

custom_size_cent = """app_width = {window_width}
app_height = {window_height}
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
pos_x = (screen_width - app_width) // 2
pos_y = (screen_height - app_height) // 2
app.geometry(f"{{app_width}}x{{app_height}}+{{pos_x}}+{{pos_y}}")"""

custom_size_ncent = """app_width = {window_width}
app_height = {window_height}
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
pos_x = (screen_width - app_width) // 2
pos_y = (screen_height - app_height) // 2
app.geometry(f"{{app_width}}x{{app_height}}")"""

imports_1A = """import tkinter as tk
from tkinter import ttk
"""

imports_1B = """import tkinter as tk
from tkinter import ttk
import os
"""