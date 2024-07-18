base_template = """# This is a generated script
#region ===Imports===
import tkinter as tk
from tkinter import ttk

#endregion

#region ===Functions===

#endregion

#region ===App Setup===
app = tk.Tk()
app.title("{title}")
{AppSetup}
# Conditional block 1 end

#endregion

#region ===Data/Variables===

#endregion

#region ===Widgets===

#endregion

#region ===Bindings===

#endregion

#region ===Run===
app.mainloop()
#endregion
"""


AppSetup_1A = """
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()
x = (screen_width - app_width) // 2
y = (screen_height - app_height) // 5
app.geometry(f"+{x}+{y}")
app.resizable(False, False)
"""

AppSetup_1B = """
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = {app_width}
app_height = {app_height}
x = (screen_width - app_width) // 2
y = (screen_height - app_height) // 5
app.geometry(f"{{app_width}}x{{app_height}}+{{x}}+{{y}}")
app.resizable(False, False)


label = tk.Label(app, text="Hello, tkinter!")
label.pack()
"""
