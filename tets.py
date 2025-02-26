import tkinter as tk
import math;

# decalere on_button_click
def on_button_click(value):
    print(value)

# make window
root = tk.Tk()
root.title("SImple calculetor")
root.geometry("400x400")
# make enrty filed
entry_var = tk.StringVar();
entry = tk.Entry(root,textvariable=entry_var,font=("Arial", 20), justify="center", bd=10)
entry.grid(row=0, column=0, columnspan=4)
# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
    ("√", "%", "^", "Quit"),
]
for r, row in enumerate(buttons,1):
    for c, value in enumerate(row):
        btn = tk.Button(root, text=value, font=("Arial", 16), width=5, height=2,
                        command=lambda v=value: root.quit() if v == "Quit" else on_button_click(v))
        btn.grid(row=r, column=c, padx=5, pady=5)
root.mainloop()