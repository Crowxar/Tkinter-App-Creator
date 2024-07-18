import tkinter as tk
from tkinter import ttk
import os

#region ===Functions===


#endregion

#region ===App Setup===
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = screen_width // 2
y = screen_height // 2
window.title('Tkinter App Creator')
window.geometry(f'+{x}+{y}')
window.resizable(False, False)
#endregion

#region ===Widgets===
title_frame = ttk.Frame(window)
title_frame.pack()
app_label = ttk.Label(title_frame, text='Tkinter App Creator!', font=('Arial', 18))
app_label.pack(padx=10, pady=10)

path_frame = ttk.Frame(window)
path_frame.pack()
path_button = tk.Button(path_frame, text="Path Browse", command=lambda: print("Path Button"))
path_button.pack(padx=10, pady=(5, 2), side='left')
path_entry = ttk.Entry(path_frame, width=20)
path_entry.pack(padx=10, side='left')


apptitle_frame = ttk.Frame(window)
apptitle_frame.pack()
title_label = ttk.Label(apptitle_frame, text="Title", font=("Arial", 12))
title_label.pack(padx=10, pady=(5, 2), side='left', anchor='e')
title_entry = ttk.Entry(apptitle_frame, width=20)
title_entry.pack(padx=10, side='right', anchor='w')

# size_box = tk.Checkbutton(text="Auto Size")
# size_box.grid(row=3, column=0, padx=10, pady=(5, 2))
# size_entry = ttk.Entry(window, width=20, state=tk.DISABLED)
# size_entry.grid(row=3, column=1, padx=10)

# centerbox = tk.Checkbutton(text="Centered")
# centerbox.grid(row=4, column=0, padx=10, pady=2)
# complete_button = ttk.Button(window,text="Submit")
# complete_button.grid(row=4, column=1, padx=10, pady=10)

# updatelabel = ttk.Label(window, text="Click Submit When Done", font=("Arial", 12))
# updatelabel.grid(row=5, column=0, columnspan=2, padx=10, pady=2)
#endregion

#region ===Run===
window.focus_force()
window.wm_attributes('-topmost', 1)
window.mainloop()
os.system('cls')
#endregion
