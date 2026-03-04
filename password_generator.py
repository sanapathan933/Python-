import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------- FUNCTION ----------

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showwarning("Warning", "Enter valid length!")
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(random.choice(characters) for _ in range(length))

        password_var.set(password)
        status_label.config(text="✅ Password Generated")

    except ValueError:
        messagebox.showerror("Error", "Enter numbers only!")


def copy_password():
    password = password_var.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate password first!")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    status_label.config(text="📋 Password Copied")


def clear_all():
    length_entry.delete(0, tk.END)
    password_var.set("")
    status_label.config(text="Cleared")


# ---------- WINDOW ----------

root = tk.Tk()
root.title("Password Generator")
root.geometry("380x350")
root.config(bg="#f2f6ff")

# ---------- TITLE ----------
tk.Label(root,
         text="🔐 Password Generator",
         font=("Arial",18,"bold"),
         bg="#4a7abc",
         fg="white",
         pady=10).pack(fill="x")

# ---------- LENGTH INPUT ----------
frame = tk.Frame(root, bg="#f2f6ff")
frame.pack(pady=20)

tk.Label(frame,
         text="Password Length:",
         font=("Arial",12),
         bg="#f2f6ff").grid(row=0, column=0, padx=5)

length_entry = tk.Entry(frame, font=("Arial",12), width=10)
length_entry.grid(row=0, column=1)

# ---------- GENERATE BUTTON ----------
tk.Button(root,
          text="Generate Password",
          font=("Arial",12,"bold"),
          bg="#4CAF50",
          fg="white",
          command=generate_password).pack(pady=10)

# ---------- PASSWORD DISPLAY ----------
password_var = tk.StringVar()

password_box = tk.Entry(root,
                        textvariable=password_var,
                        font=("Arial",14),
                        justify="center",
                        bd=3,
                        relief="sunken",
                        width=25)
password_box.pack(pady=10)

# ---------- BUTTONS ----------
btn_frame = tk.Frame(root, bg="#f2f6ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame,
          text="Copy",
          width=12,
          bg="#2196F3",
          fg="white",
          command=copy_password).grid(row=0, column=0, padx=5)

tk.Button(btn_frame,
          text="Clear",
          width=12,
          bg="#f44336",
          fg="white",
          command=clear_all).grid(row=0, column=1, padx=5)

# ---------- STATUS ----------
status_label = tk.Label(root,
                        text="Enter length and generate password",
                        bg="#f2f6ff",
                        font=("Arial",10))
status_label.pack(pady=15)

# ---------- RUN ----------
root.mainloop()
