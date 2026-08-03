import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("AI Resume Builder")
root.geometry("900x600")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

title = tk.Label(
    root,
    text="AI Resume Builder",
    font=("Arial", 26, "bold"),
    bg="#f0f4f8",
    fg="#1f4e79"
)
title.pack(pady=30)

subtitle = tk.Label(
    root,
    text="Create Professional ATS-Friendly Resumes",
    font=("Arial", 14),
    bg="#f0f4f8"
)
subtitle.pack()

def start():
    messagebox.showinfo("Next Step", "Login Page will open in the next step.")

btn = tk.Button(
    root,
    text="Get Started",
    font=("Arial", 14, "bold"),
    bg="#1f4e79",
    fg="white",
    width=20,
    command=start
)
btn.pack(pady=40)

root.mainloop()