import tkinter as tk
import math

# handle btn click
def on_button_click(value):
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
    elif value == "π":
        entry_var.set(entry_var.get() + str(math.pi))
    elif value == "e":
        entry_var.set(entry_var.get() + str(math.e))
    elif value == "sin":
        try:
            num = float(entry_var.get())
            entry_var.set(math.sin(math.radians(num)))  # Convert to radians before calculation
        except ValueError:
            entry_var.set("Error")
    elif value == "cos":
        try:
            num = float(entry_var.get())
            entry_var.set(math.cos(math.radians(num)))
        except ValueError:
            entry_var.set("Error")
    elif value == "tan":
        try:
            num = float(entry_var.get())
            entry_var.set(math.tan(math.radians(num)))
        except ValueError:
            entry_var.set("Error")
    elif value == "log":
        try:
            num = float(entry_var.get())
            if num <= 0:
                entry_var.set("Error")
            else:
                entry_var.set(math.log10(num))
        except ValueError:
            entry_var.set("Error")
    elif value == "ln":
        try:
            num = float(entry_var.get())
            if num <= 0:
                entry_var.set("Error")
            else:
                entry_var.set(math.log(num))
        except ValueError:
            entry_var.set("Error")
    elif value == "e^x":
        try:
            num = float(entry_var.get())
            entry_var.set(math.exp(num))
        except ValueError:
            entry_var.set("Error")
    elif value == "!":
        try:
            num = int(entry_var.get())
            if num < 0:
                entry_var.set("Error")
            else:
                entry_var.set(math.factorial(num))
        except ValueError:
            entry_var.set("Error")
    elif value == "deg":
        try:
            num = float(entry_var.get())
            entry_var.set(math.degrees(num))
        except ValueError:
            entry_var.set("Error")
    elif value == "rad":
        try:
            num = float(entry_var.get())
            entry_var.set(math.radians(num))
        except ValueError:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + str(value))

# calculate results
def calculate_result():
    try:
        expression = entry_var.get().replace("^", "**")
        result = eval(expression)
        entry_var.set(result)
    except:
        entry_var.set("Error")

# create Main Window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")  # Increased window size

# create Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4)

# button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['√', '%', '^', '!'],
    ['sin', 'cos', 'tan', 'log'],
    ['ln', 'e^x', 'π', 'e'],
    ['deg', 'rad', 'Quit']
]

# create buttons dynamically
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == 'Quit':
            btn = tk.Button(root, text=text, font="Arial", width=5, height=2, command=root.quit)
        else:
            btn = tk.Button(root, text=text, font="Arial", width=5, height=2, command=lambda t=text: on_button_click(t))
        btn.grid(row=r+1, column=c)

# Run the GUI
root.mainloop()