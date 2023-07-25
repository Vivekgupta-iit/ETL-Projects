# scientific_calculator.py

import tkinter as tk
import math

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main application window
root = tk.Tk()
root.title("Scientific Calculator")

# Create the input field
entry = tk.Entry(root, width=30, borderwidth=2)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("^", 5, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, command=lambda t=text: entry.insert(tk.END, t))
    btn.grid(row=row, column=col)

# Calculate button
equal_btn = tk.Button(root, text="=", command=calculate)
equal_btn.grid(row=6, column=2, columnspan=2)

# Start the main event loop
root.mainloop()
