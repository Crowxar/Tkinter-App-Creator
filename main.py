import tkinter as tk
from tkinter import ttk, filedialog
import conditions as con
import json
import re
import os


# region ===Functions===
def load_default_path():
    try:
        with open("tkinterapp.json", "r") as json_file:
            data = json.load(json_file)
            path = data.get("default_path", "")
            if os.path.exists(path):
                return path
            else:
                return ""
    except FileNotFoundError:
        return ""


def save_default_path():
    current_path = path_entry.get()
    if os.path.exists("tkinterapp.json"):
        with open("tkinterapp.json", "r") as json_file:
            data = json.load(json_file)
            default_path = data.get("default_path")
    else:
        default_path = None

    if current_path != default_path:
        with open("tkinterapp.json", "w") as json_file:
            json.dump({"default_path": current_path}, json_file)


def browse_folder():
    folder_path = path_var.get()
    if folder_path:
        selected_folder = filedialog.askdirectory(initialdir=folder_path)
        if selected_folder:
            path_var.set(selected_folder)


def is_valid_size(value):
    # Compile the regex pattern to match the size format
    pattern = re.compile(r"^(\d+)\s*x\s*(\d+)$")
    match = pattern.match(value)

    if match:
        width, height = match.groups()
        return int(width), int(height)
    else:
        return False


def is_valid_filename(filename):
    regex = r'^(?!^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$)[^<>:"/\\|?*\x00-\x1F]+[^<>:"/\\|?*\x00-\x1F\ .]$'
    return re.match(regex, filename) is not None


def toggle_size():
    if size_var.get():
        size_entry.config(state="disabled")
    else:
        size_entry.config(state="normal")


def reset_to_default():
    path_var.set(os.getcwd())
    title_var.set("")
    size_var.set(True)
    size_val.set("")
    size_entry.config(state="disabled")
    updatelabel.config(text="Reset to defaults")


def write_script():
    # Check if file title is good
    formatted_title = title_var.get().strip().replace(" ", "_").lower()
    if not is_valid_filename(formatted_title):
        updatelabel.config(text="Invalid Filename")
        return
    else:
        valid_title = formatted_title

    # Check if file size is good
    if not size_var.get():
        # size_var is False
        size_tuple = is_valid_size(size_val.get().strip().lower())  # Validate size
        if not size_tuple:
            updatelabel.config(text="Invalid Size")
            return
        else:
            valid_size = size_tuple  # Set the updated_size to the tuple
    else:
        # size_var is True
        valid_size = "default"

    if valid_size == "default":
        app_size_specs = con.AppSetupAuto
    else:  # if its a tuple
        app_size_specs = con.AppSetupSized.format(
            app_width=valid_size[0],
            app_height=valid_size[1]
        )

    if regions_var.get(): # if regions is enabled
        base_template=con.base_template_with_regions
    else: # if they're not
        base_template=con.base_template_without_regions
    

    
    script_content = base_template.format(
            imports = con.imports,
            title = valid_title,
            AppSize = app_size_specs,
        )
        

    # Check if file path is good with file name, then write script to title
    path = os.path.join(path_var.get(), f"{valid_title}.py")
    if os.path.exists(path):
        updatelabel.config(text="File already exists!")
    else:
        try: 
            with open(path, "w") as file:
                file.write(script_content)
            updatelabel.config(text="Script created successfully!")
            save_default_path()
        #       app.destroy()
        except Exception as e:
            updatelabel.config(text=f"Invalid Path {e}")


# endregion

# region ===App Setup===
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
# endregion

# region ===Data/Variables===
default_path = load_default_path()
if default_path:
    path_var = tk.StringVar(value=default_path)
else:
    path_var = tk.StringVar(value=os.getcwd())

title_var = tk.StringVar(value="")
size_var = tk.BooleanVar(value=True)
size_val = tk.StringVar(value="")
center_var = tk.BooleanVar(value=True)
resizeable_var = tk.BooleanVar(value=True)
regions_var = tk.BooleanVar(value=True)
forcetop_var = tk.BooleanVar(value=True)
# endregion

# region ===Widgets===
label = ttk.Label(app, text="Tkinter App Creator!", font=("Arial", 18))
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

path_entry = ttk.Entry(app, width=20, textvariable=path_var)
path_entry.grid(row=1, column=1, sticky='w')
path_button = tk.Button(app, text="Path Browse", command=browse_folder)
path_button.grid(row=1, column=0, padx=(10,0), pady=(5, 2), sticky='w')

title_label = ttk.Label(app, text="Title", font=("Arial", 12))
title_label.grid(row=2, column=0, padx=(10,0), pady=(5, 2), sticky='w')
title_entry = ttk.Entry(app, width=20, textvariable=title_var)
title_entry.grid(row=2, column=1, sticky='w')

size_checkbox = ttk.Checkbutton(
    app, text="Auto Size", variable=size_var, command=toggle_size
)
size_checkbox.grid(row=3, column=0, padx=(10,0), pady=(5, 2), sticky='w')
size_entry = ttk.Entry(app, state="disabled", textvariable=size_val)
size_entry.grid(row=3, column=1, pady=(5, 2))

center_checkbox = ttk.Checkbutton(app, text="Center", variable=center_var)
center_checkbox.grid(row=6, column=0, padx=(10,0), pady=2, sticky='w')

resizeable_checkbox = ttk.Checkbutton(app, text="Resizeable", variable=resizeable_var)
resizeable_checkbox.grid(row=7, column=0, padx=(10,0), pady=2, sticky='w')

regions_checkbox = ttk.Checkbutton(app, text="Create Regions", variable=regions_var)
regions_checkbox.grid(row=7, column=0, padx=(10,0), pady=2, sticky='w')

forcetop_checkbox = ttk.Checkbutton(app, text="Resizeable", variable=forcetop_var)
forcetop_checkbox.grid(row=8, column=0, padx=(10,0), pady=2, sticky='w')

reset_button = ttk.Button(app, text="Reset", command=reset_to_default)
reset_button.grid(row=9, column=0, padx=(10,0), pady=10, sticky='w')

complete_button = ttk.Button(app, text="Submit", command=write_script)
complete_button.grid(row=9, column=1, pady=10, sticky='w')

updatelabel = ttk.Label(app, text="Click Submit When Done", font=("Arial", 12))
updatelabel.grid(row=10, column=0, columnspan=2, padx=10, pady=2)



# endregion

# region ===Bindings===
title_entry.bind("<Return>", lambda event: complete_button.invoke())

# endregion

# region ===Run===
app.focus_force()
app.wm_attributes("-topmost", 1)
app.mainloop()
# os.system('cls')
# endregion
