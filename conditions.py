base_template_with_regions = """# This is a generated script made with Tkinter App Creator by Crowxar - https://crowxar.github.io/
#region ===Imports===
{imports}

#endregion

#region ===Functions===
...

#endregion

#region ===App Setup===
app = tk.Tk()
app.title("{title}")
{AppSize}

#endregion

#region ===Data/Variables===
...

#endregion

#region ===Widgets===
example_label_widget = ttk.Label(app, text="Thanks for using Tkinter App Creator!", font=("Arial", 18))
example_label_widget.pack(expand=True, fill="both")

#endregion

#region ===Bindings===
...

#endregion

#region ===Run===
app.mainloop()

#endregion
"""

base_template_without_regions = """# This is a generated script made with Tkinter App Creator by Crowxar - https://crowxar.github.io/
{imports}

app = tk.Tk()
app.title("{title}")
{AppSize}


example_label_widget = ttk.Label(app, text="Thanks for using Tkinter App Creator!", font=("Arial", 18))
example_label_widget.pack(expand=True, fill="both")

app.mainloop()"""

AppSetupAuto = """app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
pos_x = (screen_width - app_width) // 2
pos_y = (screen_height - app_height) // 2
app.geometry(f"+{pos_x}+{pos_y}")"""

AppSetupSized = """app_width = {app_width}
app_height = {app_height}
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
pos_x = (screen_width - app_width) // 2
pos_y = (screen_height - app_height) // 2
app.geometry(f"{{app_width}}x{{app_height}}+{{pos_x}}+{{pos_y}}")"""





imports = """import tkinter as tk
from tkinter import ttk"""