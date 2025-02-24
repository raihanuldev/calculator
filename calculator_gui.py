import tkinter as tk
import math

# handle btn click
def on_button_click(value):
    if value=="=":
        calculate_result()
    elif value =="C":
        entry_var.set("")
    elif value=="√":
        try:
            num = float(entry_var.get())
            if num<0:
                entry_var.set("Error")
            else:
                entry_var.set(math.sqrt(num))
        except ValueError:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get()+str(value))

# calculete results
def calculate_result():
    try:
        expression = entry_var.get().replace('^','**')
        result = eval(expression)
        entry_var.set(result)
    except:
        entry_var.set("Error")

# create Main Window
root = tk.Tk()
root.title("BSPI Calculator")
root.geometry("350x380")

# create Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_var,font=("Arial",20),justify="right",bd=10)
entry.grid(row=0,column=0,columnspan=4)

#buttonlayout
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['C','0','=','+'],
    ['√', '%', '^', 'Quit']
]

# create button dynamiclly
for r,row in enumerate(buttons):
    for c,text in enumerate(row):
        if text=='Quit':
            btn = tk.Button(root,text=text,font="Arial",width=5,height=2,command=root.quit)
        else:
            btn  = tk.Button(root,text=text,font="Arial",width=5,height=2,command=lambda t= text:on_button_click(t))
        btn.grid(row=r+1,column=c)

# Run the GUI
root.mainloop()