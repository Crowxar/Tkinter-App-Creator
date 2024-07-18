base_template = """# This is a generated script
#region ===Imports===
import tkinter as tk
from tkinter import ttk

#endregion

#region ===Functions===

#endregion

#region ===App Setup===

#endregion

#region ===Data/Variables===

#endregion

#region ===Widgets===

#endregion

#region ===Bindings===

#endregion

#region ===Run===

#endregion
"""



"""def main():
    print("Starting script...")

    # Conditional block 1 start
    {conditional_code_1}
    # Conditional block 1 end

    # Conditional block 2 start
    {conditional_code_2}
    # Conditional block 2 end

    print("Script ended.")"""

"""def create_file(path, title, center, size_tuple):
    path = os.path.join(path, f"{title}.py")
    with open(path, "w") as file:
        file.write(
            "import tkinter as tk\nfrom tkinter import ttk\nimport os\n\n#region ===Functions===\n\n\n#endregion\n\n#region ===Setup===\n"
        )
        file.write("window = tk.Tk()\n")
        if center is False:
            if size_tuple:
                file.write(f"window_width = {size_tuple[0]}\n")
                file.write(f"window_height = {size_tuple[1]}\n")
            else:
                file.write("window_width = window.winfo_reqwidth()\n")
                file.write("window_height = window.winfo_reqheight()\n")
        else:
            if size_tuple:
                file.write(f"window_width = {size_tuple[0]}\n")
                file.write(f"window_height = {size_tuple[1]}\n")
            else:
                file.write("window_width = window.winfo_reqwidth()\n")
                file.write("window_height = window.winfo_reqheight()\n")
            file.write("screen_width = window.winfo_screenwidth()\n")
            file.write("screen_height = window.winfo_screenheight()\n")
            file.write("x = (screen_width - window_width) // 2\n")
            file.write("y = (screen_height - window_height) // 5\n")
        file.write(f"window.title('{title}')\n")
        if center is False:
            file.write("window.geometry(f'{window_width}x{window_height}')\n")
        else:
            file.write("window.geometry(f'{window_width}x{window_height}+{x}+{y}')\n")
        file.write("window.resizable(False, False)\n\n#endregion\n\n#region ===Widgets===\n\n\n#endregion\n\n#region ===Run===\n")
        file.write(
            "window.focus_force()\nwindow.wm_attributes('-topmost', 1)\nwindow.mainloop()\nos.system('cls')\n#endregion\n"
        )
    window.destroy()"""