import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Contact Book")
root.geometry("800x520")
root.config(bg="#eef2f3")

contacts = []

# ---------------- VARIABLES ----------------
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()

# ---------------- FUNCTIONS ----------------

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")


def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name & Phone Required!")
        return

    contacts.append([name, phone, email, address])
    show_contacts()
    clear_fields()


def show_contacts():   # VIEW BUTTON FUNCTION
    table.delete(*table.get_children())
    for contact in contacts:
        table.insert("", tk.END, values=contact)


def select_contact(event):
    selected = table.focus()
    data = table.item(selected, "values")

    if data:
        name_var.set(data[0])
        phone_var.set(data[1])
        email_var.set(data[2])
        address_var.set(data[3])


def update_contact():
    selected = table.focus()
    if selected:
        index = table.index(selected)
        contacts[index] = [
            name_var.get(),
            phone_var.get(),
            email_var.get(),
            address_var.get()
        ]
        show_contacts()
        clear_fields()


def delete_contact():
    selected = table.focus()
    if selected:
        index = table.index(selected)
        contacts.pop(index)
        show_contacts()
        clear_fields()


def search_contact():
    keyword = name_var.get().lower()
    table.delete(*table.get_children())

    for contact in contacts:
        if keyword in contact[0].lower() or keyword in contact[1]:
            table.insert("", tk.END, values=contact)

# ---------------- TITLE ----------------
title = tk.Label(root, text="CONTACT BOOK",
                 font=("Arial", 20, "bold"),
                 bg="#2c3e50", fg="white", pady=10)
title.pack(fill="x")

# ---------------- INPUT FRAME ----------------
frame = tk.Frame(root, bg="#eef2f3")
frame.pack(pady=15)

tk.Label(frame, text="Name", bg="#eef2f3").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(frame, textvariable=name_var, width=25).grid(row=0, column=1)

tk.Label(frame, text="Phone", bg="#eef2f3").grid(row=0, column=2)
tk.Entry(frame, textvariable=phone_var, width=25).grid(row=0, column=3)

tk.Label(frame, text="Email", bg="#eef2f3").grid(row=1, column=0)
tk.Entry(frame, textvariable=email_var, width=25).grid(row=1, column=1)

tk.Label(frame, text="Address", bg="#eef2f3").grid(row=1, column=2)
tk.Entry(frame, textvariable=address_var, width=25).grid(row=1, column=3)

# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(root, bg="#eef2f3")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, bg="#27ae60",
          fg="white", command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="View", width=12, bg="#2980b9",
          fg="white", command=show_contacts).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Search", width=12, bg="#f39c12",
          fg="white", command=search_contact).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="Update", width=12, bg="#8e44ad",
          fg="white", command=update_contact).grid(row=0, column=3, padx=5)

tk.Button(btn_frame, text="Delete", width=12, bg="#c0392b",
          fg="white", command=delete_contact).grid(row=0, column=4, padx=5)

tk.Button(btn_frame, text="Clear", width=12,
          command=clear_fields).grid(row=0, column=5, padx=5)

# ---------------- TABLE ----------------
columns = ("Name", "Phone", "Email", "Address")

table = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=180)

table.pack(pady=10)

table.bind("<<TreeviewSelect>>", select_contact)

# ---------------- RUN ----------------
root.mainloop()
