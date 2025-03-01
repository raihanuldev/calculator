import tkinter as tk
import math
import speech_recognition as sr

# Handle button click
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
    else:
        entry_var.set(entry_var.get() + str(value))

# Calculate results
def calculate_result():
    try:
        expression = entry_var.get().replace("^", "**")
        result = eval(expression)
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Voice input function
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        entry_var.set("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            entry_var.set(command)
        except sr.UnknownValueError:
            entry_var.set("Could not understand")
        except sr.RequestError:
            entry_var.set("Error with recognition")

# Create Main Window
root = tk.Tk()
root.title("Scientific Calculator with Voice Input")
root.geometry("400x600")
root.configure(bg="#1e1e1e")

# Create Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, bg="#252526", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['√', '%', '^', '!'],
    ['π', 'e', 'Quit', 'Voice']
]

# Create buttons dynamically
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text == 'Quit':
            btn = tk.Button(root, text=text, font="Arial", width=5, height=2, command=root.quit, bg="#d9534f", fg="white")
        elif text == 'Voice':
            btn = tk.Button(root, text=text, font="Arial", width=5, height=2, command=voice_input, bg="#5bc0de", fg="white")
        else:
            btn = tk.Button(root, text=text, font="Arial", width=5, height=2, command=lambda t=text: on_button_click(t), bg="#2a2d2e", fg="white")
        btn.grid(row=r+1, column=c, padx=5, pady=5)

# Run the GUI
root.mainloop()
