import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
def search_resume():
    name = search_entry.get()

    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM resumes WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()
# ---------------- DELETE FUNCTION ----------------
def delete_resume():
    selected = tree.focus()

    if selected == "":
        messagebox.showwarning("Warning", "Please select a record.")
        return

    values = tree.item(selected, "values")
    resume_id = values[0]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM resumes WHERE id=?", (resume_id,))

    conn.commit()
    conn.close()

    tree.delete(selected)

    messagebox.showinfo("Success", "Resume Deleted Successfully!")

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("View Resumes")
root.geometry("1000x500")

tree = ttk.Treeview(root)

tree["columns"] = (
    "ID",
    "Name",
    "Email",
    "Phone",
    "Address",
    "Skills",
    "Education",
    "Projects"
)

tree.column("#0", width=0, stretch=False)

for col in tree["columns"]:
    tree.column(col, width=120)
    tree.heading(col, text=col)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM resumes")
rows = cursor.fetchall()

for row in rows:
    tree.insert("", tk.END, values=row)

conn.close()

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search Name:").pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_resume,
    bg="blue",
    fg="white"
).pack(side=tk.LEFT)

tree.pack(fill="both", expand=True)

delete_btn = tk.Button(
    root,
    text="Delete Selected Resume",
    bg="red",
    fg="white",
    font=("Arial",12,"bold"),
    command=delete_resume
)

delete_btn.pack(pady=10)

root.mainloop()