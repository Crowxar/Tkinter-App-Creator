import tkinter as tk
from tkinter import ttk, filedialog
import conditions as con
import json
import re
import os

#region ===Functions===
def load_default_path():
    try:
        with open("tkinterapp.json", "r") as json_file:
            data = json.load(json_file)
            return data.get("default_path", "")
    except FileNotFoundError:
        return ""
    
def browse_folder():
    folder_path = path_var.get()
    if folder_path:
        selected_folder = filedialog.askdirectory(initialdir=folder_path)
        if selected_folder:
            path_var.set(selected_folder)

def validate_format(value):
    value_stripped = value.strip()
    pattern = r"^\d+\s*x\s*\d+$"
    return bool(re.match(pattern, value_stripped))

def is_valid_filename(filename):
    regex = r'^(?!^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$)[^<>:"/\\|?*\x00-\x1F]+[^<>:"/\\|?*\x00-\x1F\ .]$'
    return re.match(regex, filename) is not None

def final_check(formatted_title):
    if not is_valid_filename(formatted_title):
        updatelabel.config(text="Invalid Filename")
        return False
    updatelabel.config(text="Click Submit When Done")
    return True

def write_script():
    formatted_title = titlevar.get().strip().replace(" ", "_").lower()
    if not final_check(formatted_title):
        return
    
    script_content = con.base_template.format()
    path = os.path.join(path_var.get(), f"{formatted_title}.py")
    try:
        with open(path, "w") as file:
            file.write(script_content)
        updatelabel.config(text="Script created successfully!")
        app.destroy()
    except Exception as e:
        updatelabel.config(text=f"Error: {e}")
#endregion

#region ===App Setup===
app = tk.Tk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()

x = (screen_width - app_width) // 2
y = (screen_height - app_height) // 5

app.title("Tkinter File Creator")
app.geometry(f"+{x}+{y}")
app.resizable(False, False)
#endregion

#region ===Data/Variables===
default_path = load_default_path()
if default_path:
    path_var = tk.StringVar(value=default_path)
else:
    path_var = tk.StringVar(value=os.getcwd())

titlevar = tk.StringVar(value='')
#endregion

#region ===Widgets===
label = ttk.Label(app,text="Tkinter App Creator!",font=("Arial", 18))
label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

path_entry = ttk.Entry(app,width=20,textvariable=path_var)
path_entry.grid(row=1, column=1,padx=10)
path_button = tk.Button(app,text="Path Browse",command=browse_folder)
path_button.grid(row=1, column=0,padx=10, pady=(5, 2))

title_label = ttk.Label(app,text="Title",font=("Arial", 12))
title_label.grid(row=2,column=0,padx=10,pady=(5, 2))
title_entry = ttk.Entry(app,width=20,textvariable=titlevar)
title_entry.grid(row=2,column=1,padx=10)

updatelabel = ttk.Label(app,text="Click Submit When Done",font=("Arial", 12))
updatelabel.grid(row=5,column=0,columnspan=2,padx=10,pady=2)

complete_button = ttk.Button(app,text="Submit", command=write_script)
complete_button.grid(row=4, column=1, padx=10, pady=10)

#endregion

#region ===Bindings===
title_entry.bind("<Return>", lambda event: complete_button.invoke())

#endregion

#region ===Run===
app.focus_force()
app.wm_attributes('-topmost', 1)
app.mainloop()
#os.system('cls')
#endregion

"""
#region ===Functions===




def validate_format(value):
    value_stripped = value.strip()
    pattern = r"^\d+\s*x\s*\d+$"
    return bool(re.match(pattern, value_stripped))

def save_default_path(path):
    data = {"default_path": path}
    with open("default_path.json", "w") as json_file:
        json.dump(data, json_file)

def on_path_change():
    new_path = path_entry.get()
    save_default_path(new_path)



def Complete(path=None, title=None, center=True, size=None, updatelabel=None):
    if path is None or not os.path.exists(path):
        updatelabel.config(text="Invalid Path")
        return
    if title is None or title.strip() == "":
        updatelabel.config(text="Need Title")
        return
    if size_var.get():
        size_tuple = ("app.winfo_reqwidth()", "app.winfo_reqheight()")
    else:
        size_bool = validate_format(size)
        if not size_bool:
            updatelabel.config(text="Invalid Size: Width x Height")
            return

        width_str, height_str = size.split("x")
        size_tuple = (int(width_str), int(height_str))

    updatelabel.config(text="Submitted Successfully")
    title = "_".join(title.lower().strip().split())
    on_path_change()
    create_file(path, title, center, size_tuple)



#endregion
"""