# region ===Imports===
import tkinter as tk
from tkinter import ttk, filedialog
import conditions as con
import json
import re
import os


# endregion


# region ===Debug===
def Debug_Test():
    formatted_title = title_var.get().strip().replace(" ", "_").lower()
    filename = formatted_title + ".py"
    file_path = os.path.normpath(os.path.join(path_var.get(), filename))
    os.remove(file_path)


# endregion

# region ===Functions===


def browse_folder():
    folder_path = path_var.get()
    if folder_path:
        selected_folder = filedialog.askdirectory(initialdir=folder_path)
        if selected_folder:
            path_var.set(selected_folder)


def togglebox_entry(event=None):
    selected_option = dropdown.get()
    if selected_option == "Custom":
        size_entry.config(state=tk.NORMAL)
        size_entry.insert(0, "width x height")
    else:
        size_entry.delete(0, tk.END)
        size_entry.config(state=tk.DISABLED)


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


def is_valid_filename(filename):
    regex = r'^(?!^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$)[^<>:"/\\|?*\x00-\x1F]+[^<>:"/\\|?*\x00-\x1F\ .]$'
    return re.match(regex, filename) is not None


def validate_path(title):
    path = os.path.join(path_var.get(), f"{title}.py")
    # path = os.path.join(path_var.get(), f"{title}.py")

    if os.path.exists(path):
        updatelabel.config(text="File already exists!")
        return None  # Return None to indicate that no new path was created
    return path


def validate_size(value):
    # Compile the regex pattern to match the size format
    pattern = re.compile(r"^(\d+)\s*x\s*(\d+)$")
    match = pattern.match(value)

    if match:
        width, height = match.groups()
        return int(width), int(height)
    else:
        return False


def write_file(path, contents):
    try:
        # Create an empty file or write some initial content if needed
        with open(path, "w") as file:
            file.writelines(contents)
        updatelabel.config(text="Script created successfully!")
        save_default_path()
        app.destroy()
    except FileNotFoundError:
        updatelabel.config(text="Invalid Path: File not found")
        return None
    except PermissionError:
        updatelabel.config(text="Permission Denied: Cannot create file")
        return None
    except Exception as e:
        updatelabel.config(text=f"An error occurred: {e}")
        return None


def reset_app():
    title_var.set(value="")
    path_var.set(value=load_default_path())
    selected_size_option.set("1/2 Screen")
    center_var.set(value=True)
    resize_var.set(value=True)
    regions_var.set(value=False)
    forcetop_var.set(value=True)
    clear_var.set(value=False)
    size_entry.delete(0, tk.END)
    size_entry.config(state=tk.DISABLED)
    updatelabel.config(text="App Reset")


def create_file():
    # validate title
    formatted_title = title_var.get().strip().replace(" ", "_").lower()
    if not is_valid_filename(formatted_title):
        updatelabel.config(text="Invalid Filename")
        return
    else:
        valid_title = formatted_title

    # validate path
    validated_path = validate_path(valid_title)
    if not validated_path:
        return

    # validate size
    size_config = selected_size_option.get()
    if size_config == "Custom":
        size_tuple = validate_size(size_entry.get().strip().lower())
        if not size_tuple:
            updatelabel.config(text="Invalid Size")
            return
        else:
            validated_size = size_tuple

    # regions
    if regions_var.get():  # if regions are enabled
        base_temp = con.base_template_with_regions
    else:  # if they're not enabled
        base_temp = con.base_template_without_regions

    if center_var.get():
        if size_config == "Custom":
            configured_size = con.custom_size_cent.format(
                window_width=validated_size[0], window_height=validated_size[1]
            )
        elif size_config == "1/2 Screen":
            configured_size = con.half_size_cent
        else:
            configured_size = con.fit_sized_cent
    else:
        if size_config == "Custom":
            configured_size = con.custom_size_ncent.format(
                window_width=validated_size[0], window_height=validated_size[1]
            )
        elif size_config == "1/2":
            configured_size = con.half_size_ncent
        else:
            configured_size = con.fit_sized_cent

    # resize
    if resize_var.get():
        resize_con = """"""
    else:
        resize_con = """app.resizable(False, False)"""
    # forcetop
    if forcetop_var.get():
        force_con = """app.focus_force()\napp.wm_attributes("-topmost", 1)"""
    else:
        force_con = """"""
    # clear term
    if clear_var.get():
        clearterm_con = """os.system('cls')"""
        import_con = con.imports_1B
    else:
        clearterm_con = """"""
        import_con = con.imports_1A
    script_content = base_temp.format(
        Title=valid_title,
        Imports=import_con,
        SizeCon=configured_size,
        ResizeCon=resize_con,
        ForceTop=force_con,
        ClearTerm=clearterm_con,
    )
    write_file(validated_path, script_content)


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

# region ===Widgets===
# App title
label = ttk.Label(app, text="Tkinter File Creator!", font=("Arial Bold", 12))
label.grid(row=0, column=0, columnspan=2)

# Title label
title_label = ttk.Label(app, text="Title of App", font=("Arial", 12), anchor="center")
title_label.grid(row=1, column=0, sticky="EW", padx=5, pady=3)

# Title entry box
title_var = tk.StringVar(value="")
title_entry = ttk.Entry(app, textvariable=title_var, width=13)
title_entry.grid(row=1, column=1, sticky="EW", padx=(5, 10), pady=3)

# Path browser
path_button = tk.Button(app, text="Path Browse", command=browse_folder)
path_button.grid(row=2, column=0, sticky="EW", padx=5, pady=3)

# Path entry
default_path = load_default_path()
if default_path:
    path_var = tk.StringVar(value=default_path)
else:
    path_var = tk.StringVar(value=os.getcwd())

path_entry = ttk.Entry(app, textvariable=path_var, width=12)
path_entry.grid(row=2, column=1, sticky="EW", padx=(5, 10), pady=3)

# Size dropdown w/ textbox to enable/disable
selected_size_option = tk.StringVar()
dropdown = ttk.Combobox(
    app,
    values=("1/2 Screen", "Fit", "Custom"),
    justify="center",
    state="readonly",
    textvariable=selected_size_option,
    width=8,
)
dropdown.set("1/2 Screen")
dropdown.option_add("*TCombobox*Listbox.Justify", "center")
dropdown.grid(row=3, column=0, sticky="EW", padx=5, pady=3)

# Size Entry Box
size_enabled_var = tk.BooleanVar(value=False)
size_entry = ttk.Entry(app, state=tk.DISABLED, width=12)
size_entry.grid(row=3, column=1, sticky="EW", padx=(5, 10), pady=3)

# Center checkbox
center_var = tk.BooleanVar(value=True)
center_checkbox = ttk.Checkbutton(app, text="Center App", variable=center_var)
center_checkbox.grid(row=4, column=0, sticky="W", padx=5, pady=3)

# Resizeable checkbox
resize_var = tk.BooleanVar(value=True)
resize_checkbox = ttk.Checkbutton(app, text="Resizeable", variable=resize_var)
resize_checkbox.grid(row=4, column=1, sticky="W", padx=5, pady=3)

# Regions checkbox
regions_var = tk.BooleanVar(value=False)
regions_checkbox = ttk.Checkbutton(app, text="Set Regions", variable=regions_var)
regions_checkbox.grid(row=5, column=0, sticky="W", padx=5, pady=3)

# Force on top checkbox
forcetop_var = tk.BooleanVar(value=True)
forcetop_checkbox = ttk.Checkbutton(app, text="Force Top", variable=forcetop_var)
forcetop_checkbox.grid(row=5, column=1, sticky="W", padx=5, pady=3)

# Clear terminal checkbox
clear_var = tk.BooleanVar(value=False)
clearterm_checkbox = ttk.Checkbutton(app, text="Clear Terminal", variable=clear_var)
clearterm_checkbox.grid(row=6, column=0, sticky="W", padx=5, pady=3)

# Reset button 0/7
reset_button = ttk.Button(app, text="Reset", command=reset_app)
reset_button.grid(row=7, column=0, sticky="EW", padx=5, pady=3)

# Submit button 1/7
complete_button = ttk.Button(app, text="Submit", command=create_file)
complete_button.grid(row=7, column=1, sticky="EW", padx=5, pady=3)


# Update Label
updatelabel = ttk.Label(app, text="Click Submit When Done", font=("Arial", 12))
updatelabel.grid(row=8, column=0, columnspan=2)


# region ===Bindings===
dropdown.bind("<<ComboboxSelected>>", togglebox_entry)

# endregion

# region ===Run===
app.focus_force()
app.wm_attributes("-topmost", 1)
app.mainloop()

# endregion
