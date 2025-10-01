import tkinter as tk 
from tkinter import ttk

from village import * 
# 

# Header
root = tk.Tk()
root.title("Village calculator")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=2)

top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, sticky="nsew")

top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=2)
top_frame.rowconfigure(1, weight=1)


choices = ["Income", "Modifiers", "Treasury"]
function_dropdown = ttk.Combobox(top_frame, values=choices)
function_dropdown.grid(row=0, column=0, sticky="ew")


input = tk.Entry(top_frame)
input.grid(row=0, column=1, sticky="ew")

input.bind("<Return>")

# Buttons 
d = {}
add_btn = tk.Button(top_frame, text="Add", command = add_modifier(d, input.get(), 10))
add_btn.grid(row=0, column=2)

remove_btn = tk.Button(top_frame, text="Remove")
remove_btn.grid(row=0, column=3)

view_btn = tk.Button(top_frame, text = "View")
view_btn.grid(row=0, column=4)

text_list = tk.Listbox(top_frame)
text_list.grid(row=1, column=0, columnspan=2, sticky= "ew")

middle_frame = tk.Frame(root)
middle_frame.grid(row=1, column=0, sticky="nsew")

middle_frame.rowconfigure(0, weight=1)



bottom_frame = tk.Frame(root)
bottom_frame.grid(row=1, column=0, sticky="ns", pady=10)

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(1, weight=1)


save_btn = tk.Button(bottom_frame, text="Save")
save_btn.grid(row=0, column=0)

clear_input_btn = tk.Button(bottom_frame, text="Clear all inputed data")
clear_input_btn.grid(row=0, column=1)

delete_btn = tk.Button(bottom_frame, text = "DELETE all data")
delete_btn.grid(row=0, column=2)

root.mainloop()
