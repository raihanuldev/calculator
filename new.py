import tkinter as tk
import math
# calculate result
def calculate_result():
    try:
        expression = entry_var.get().replace("^","**")
        result = eval(expression)
        entry_var.set(result)
    except:
        entry_var.set("Error")
# Create Button
buttons = [
    ['7','8','9','C'],
    ['4','5','6','+'],
    ['1','2','3','-'],
    ['Quite','0','/','='],
]
# make window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

# make entry_filed
entry_var = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_var,bd=10,font=("Arial",20), bg="#333", fg="white")
entry.grid(row=0,column=0,columnspan=4)


def onclick(value):
    if value == "=":
        calculate_result()
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get()+ value)
        
    
    

# show button dynamiclly
for r,row in enumerate(buttons):
    for c,value in enumerate(row):
        if value=="Quite":
            btn = tk.Button(root,text=value,font="Arial",command=root.quit, height=5,width=5)
        else:
            btn = tk.Button(root,font="Arial",bg="blue", width=6,height=5,text=value,command=lambda t=value:onclick(t))
        btn.grid(row=r+1,column=c)
root.mainloop()