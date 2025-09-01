import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("435x380")
root.configure(bg="#2c3e50")

entry = tk.Entry(root, width=18, font=("Arial", 22, "bold"),
                 borderwidth=8, relief="sunken", justify="right", bg="black" ,fg="white") 
entry.grid(row=0, column=0, columnspan=4, pady=15)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"),
                        bg="#27ae60", fg="black", activebackground="#2ecc71",
                        width=7, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"),
                        bg="#ecf0f1", fg="black", activebackground="#bdc3c7",
                        width=7, height=2, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(root, text="C", font=("Arial", 14, "bold"),
                      bg="red", fg="black", activebackground="darkred",
                      width=32, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()

