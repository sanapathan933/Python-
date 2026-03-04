import tkinter as tk
from tkinter import messagebox

# ---------------- FUNCTIONS ----------------

def show_status(msg):
    status_label.config(text=msg)


def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
    show_status("✅ Task Added Successfully")


def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task to delete!")
        return

    listbox.delete(selected[0])
    show_status("🗑️ Task Deleted")


def update_task():
    selected = listbox.curselection()
    new_task = entry.get().strip()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first!")
        return

    if new_task == "":
        messagebox.showwarning("Warning", "Enter new task text!")
        return

    index = selected[0]
    listbox.delete(index)
    listbox.insert(index, new_task)
    entry.delete(0, tk.END)

    show_status("✏️ Task Updated")


def mark_done():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    index = selected[0]
    task = listbox.get(index)

    if not task.startswith("✔ "):
        listbox.delete(index)
        listbox.insert(index, "✔ " + task)

    show_status("✔ Task Completed")


# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("420x520")
root.configure(bg="#f0f4ff")

# ---------- TITLE ----------
title = tk.Label(
    root,
    text="📝 My To-Do List",
    font=("Arial", 20, "bold"),
    bg="#4a7abc",
    fg="white",
    pady=12
)
title.pack(fill="x")

# ---------- ENTRY ----------
frame = tk.Frame(root, bg="#f0f4ff")
frame.pack(pady=15)

entry = tk.Entry(frame, font=("Arial", 14), width=24)
entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(
    frame,
    text="Add",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=8,
    command=add_task
)
add_btn.grid(row=0, column=1)

# ---------- LISTBOX ----------
listbox = tk.Listbox(
    root,
    font=("Arial", 13),
    width=35,
    height=12,
    bd=2,
    relief="groove"
)
listbox.pack(pady=10)

# ---------- BUTTONS ----------
btn_frame = tk.Frame(root, bg="#f0f4ff")
btn_frame.pack(pady=10)

update_btn = tk.Button(
    btn_frame,
    text="Update",
    width=14,
    bg="#2196F3",
    fg="white",
    command=update_task
)
update_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = tk.Button(
    btn_frame,
    text="Delete",
    width=14,
    bg="#f44336",
    fg="white",
    command=delete_task
)
delete_btn.grid(row=0, column=1, padx=5, pady=5)

done_btn = tk.Button(
    btn_frame,
    text="Mark Done",
    width=30,
    bg="#9C27B0",
    fg="white",
    command=mark_done
)
done_btn.grid(row=1, column=0, columnspan=2, pady=5)

# ---------- STATUS BAR ----------
status_label = tk.Label(
    root,
    text="Welcome! Add your tasks ✨",
    bd=1,
    relief="sunken",
    anchor="w",
    font=("Arial", 10),
    bg="white"
)
status_label.pack(side="bottom", fill="x")

# ---------- RUN ----------
root.mainloop()
