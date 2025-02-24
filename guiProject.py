import tkinter as tk
import math

def on_button_click(value):
    """ Handles button clicks """
    if value == "=":
        calculate_result()
    elif value == "C":
        entry_var.set("")
    elif value == "√":
        try:
            num = float(entry_var.get())
            if num < 0:
                entry_var.set("Error")
            else:
                entry_var.set(math.sqrt(num))
        except ValueError:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + str(value))

def calculate_result():
    """ Evaluates the mathematical expression """
    try:
        expression = entry_var.get().replace("^", "**")  # Convert ^ to power (**)
        result = eval(expression)
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="center", bd=10)
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
    ("√", "%", "^", "Quit"),
]

# Generate buttons dynamically
for r, row in enumerate(buttons, 1):
    for c, value in enumerate(row):
        btn = tk.Button(root, text=value, font=("Arial", 16), width=5, height=2,
                        command=lambda v=value: root.quit() if v == "Quit" else on_button_click(v))
        btn.grid(row=r, column=c, padx=5, pady=5)

# Run the GUI
root.mainloop()
