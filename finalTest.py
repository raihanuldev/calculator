import tkinter as tk
import math

def btnOnClick(value):
    print(value)
    if value == "=":
        calculate_result()
    elif value =="C":
        entry_variable.set("")
    elif value =="√":
        try:
            num = float(entry_variable.get())
            if(num <0):
                entry_variable.set("Error")
            else:
                entry_variable.set(math.sqrt(num))
        except:
            entry_variable.set("error")
    elif value == "π":
        entry_variable.set(entry_variable.get()+ str(math.pi))
    else:
        current_text = entry_variable.get()
        entry_variable.set(current_text+value)

def calculate_result():
    try:
        expression = entry_variable.get().replace('^','**')
        result = eval(expression)
        entry_variable.set(result)
    except:
        entry_variable.set("Error")
    
# create window
root = tk.Tk()
root.title("BSPI Calculator")
root.geometry("400x600")

# create input filed and output filed
entry_variable = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_variable,bd=10,font=("Arial",25))
entry.grid(column=0,row=0,columnspan=4)

# create button object for disply dynamiclly
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['√', '%', '^', '!'],
    ['sin', 'cos', 'tan', 'log'],
    ['ln', 'e^x', 'π', 'e'],
    ['deg', 'rad', 'π','Quit']
]
# run loop for disply button
for r,row in enumerate(buttons):
    for c ,value in enumerate(row):
        if value=='Quite':
            btn = tk.Button(root,text=value,font="Arial",width=5,height=2,command=root.quit)
        else:
            btn = tk.Button(root,text=value,font="Arial",width=5,height=2,command=lambda t=value:btnOnClick(t)) 
        btn.grid(row=r+1,column=c)           
# run gui
root.mainloop()