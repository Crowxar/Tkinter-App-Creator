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
{conditional_code_1}
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


cond_1A = """
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()
x = (screen_width - app_width) // 2
y = (screen_height - app_height) // 5
app.geometry(f"+{x}+{y}")
app.resizable(False, False)
"""

cond_1B = """
print("Condition 1B is true")
for i in range(3):
    print(f"Loop iteration {i}")
"""
default_code_block = """
print("No specific conditions met")
"""