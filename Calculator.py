import tkinter as tk
from tkinter import messagebox

# ---------- FUNCTIONS ----------

def click(value):
    current = display_var.get()
    display_var.set(current + str(value))


def clear():
    display_var.set("")


def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
        answer_label.config(text=f"Answer = {result}")
    except:
        messagebox.showerror("Error", "Invalid Calculation")
        display_var.set("")


# ---------- WINDOW ----------

root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")
root.config(bg="#f2f6ff")

# ---------- TITLE ----------
tk.Label(root,
         text="🧮 Calculator",
         font=("Arial", 18, "bold"),
         bg="#4a7abc",
         fg="white",
         pady=10).pack(fill="x")

# ---------- DISPLAY ----------
display_var = tk.StringVar()

display = tk.Entry(root,
                   textvariable=display_var,
                   font=("Arial", 18),
                   justify="right",
                   bd=5,
                   relief="sunken")
display.pack(fill="x", padx=10, pady=15)

# ---------- BUTTON FRAME ----------
frame = tk.Frame(root, bg="#f2f6ff")
frame.pack()

buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):

        if char == "=":
            btn = tk.Button(frame, text=char, width=5, height=2,
                            font=("Arial",14,"bold"),
                            bg="#4CAF50", fg="white",
                            command=calculate)
        else:
            btn = tk.Button(frame, text=char, width=5, height=2,
                            font=("Arial",14),
                            command=lambda ch=char: click(ch))

        btn.grid(row=r, column=c, padx=5, pady=5)

# ---------- CLEAR BUTTON ----------
tk.Button(root,
          text="Clear",
          font=("Arial",12,"bold"),
          bg="#f44336",
          fg="white",
          command=clear).pack(fill="x", padx=20, pady=10)

# ---------- ANSWER LABEL ----------
answer_label = tk.Label(root,
                        text="Answer = ",
                        font=("Arial",14,"bold"),
                        bg="#f2f6ff")
answer_label.pack(pady=10)

# ---------- RUN ----------
root.mainloop()  
