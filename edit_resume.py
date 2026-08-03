import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import sqlite3
import subprocess

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Edit Resume")
app.geometry("1300x750")
app.resizable(False, False)
# Background Image
bg = ctk.CTkImage(
    light_image=Image.open("assets/edit_bg.webp"),
    dark_image=Image.open("assets/edit_bg.webp"),
    size=(1300,750)
)

bg_label = ctk.CTkLabel(app, image=bg, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
main = ctk.CTkFrame(
    app,
    width=1100,
    height=650,
    fg_color="white",
    corner_radius=25,
    border_width=2,
    border_color="#D1D5DB"
)

main.place(relx=0.5, rely=0.5, anchor="center")

heading = ctk.CTkLabel(
    main,
    text="✏ Edit Resume",
    font=("Segoe UI",30,"bold"),
    text_color="#1E3A8A"
)

heading.pack(pady=20)
id_entry = ctk.CTkEntry(
    main,
    width=250,
    placeholder_text="Enter Resume ID"
)

id_entry.pack(pady=10)

load_btn = ctk.CTkButton(
    main,
    text="🔍 Load Resume",
    width=180
)

load_btn.pack(pady=10)
name = ctk.CTkEntry(
    main,
    width=350,
    height=40,
    placeholder_text="Full Name"
)
name.pack(pady=8)

email = ctk.CTkEntry(
    main,
    width=350,
    height=40,
    placeholder_text="Email"
)
email.pack(pady=8)

phone = ctk.CTkEntry(
    main,
    width=350,
    height=40,
    placeholder_text="Phone"
)
phone.pack(pady=8)

address = ctk.CTkEntry(
    main,
    width=350,
    height=40,
    placeholder_text="Address"
)
address.pack(pady=8)

skills = ctk.CTkEntry(
    main,
    width=350,
    height=40,
    placeholder_text="Skills"
)
skills.pack(pady=8)

education = ctk.CTkEntry(
    main,
    width=350,
    height=40,
    placeholder_text="Education"
)
education.pack(pady=8)

projects = ctk.CTkEntry(
    main,
    width=350,
    height=40,
    placeholder_text="Projects"
)
projects.pack(pady=8)

def load_resume():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    print("Entered ID:", id_entry.get()) 

    cursor.execute(
    "SELECT name,email,phone,address,skills,education,projects FROM resumes WHERE id=?",
    (id_entry.get(),)
)
    row = cursor.fetchone()

    if row:

        name.delete(0, "end")
        email.delete(0, "end")
        phone.delete(0, "end")
        address.delete(0, "end")
        skills.delete(0, "end")
        education.delete(0, "end")
        projects.delete(0, "end")

        
        name.insert(0, row[0])
        email.insert(0, row[1])
        phone.insert(0, row[2])
        address.insert(0, row[3])
        skills.insert(0, row[4])
        education.insert(0, row[5])
        projects.insert(0, row[6])
    else:
        messagebox.showerror("Error", "Resume not found!")

    conn.close()

load_btn.configure(command=load_resume)

def update_resume():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
UPDATE resumes
SET
    name=?,
    email=?,
    phone=?,
    address=?,
    skills=?,
    education=?,
    projects=?
WHERE id=?
""", (
    name.get(),
    email.get(),
    phone.get(),
    address.get(),
    skills.get(),
    education.get(),
    projects.get(),
    id_entry.get()
))
    
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Resume Updated Successfully!")

# Create button frame HERE (outside the function)
button_frame = ctk.CTkFrame(main)
button_frame.pack(pady=20)

update_btn = ctk.CTkButton(
    button_frame,
    text="💾 Update Resume",
    width=180,
    command=update_resume
)

update_btn.grid(row=0, column=0, padx=10)

back_btn = ctk.CTkButton(
    button_frame,
    text="🏠 Dashboard",
    width=180,
    fg_color="#16A34A",
    command=lambda: [app.destroy(), subprocess.Popen(["python", "dashboard.py"])]
)

back_btn.grid(row=0, column=1, padx=10)

footer = ctk.CTkLabel(
    main,
    text="Smart Resume Builder v1.0 | Developed by Rohit Joshi",
    font=("Segoe UI",12),
    text_color="gray40"
)

footer.pack(side="bottom", pady=15)

app.mainloop()