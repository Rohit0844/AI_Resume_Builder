import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import sqlite3
import subprocess

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Create Resume")
app.geometry("1300x750")
app.resizable(False, False)

# ---------------- Background ----------------

bg = ctk.CTkImage(
    light_image=Image.open("assets/create_bg.png"),
    dark_image=Image.open("assets/create_bg.png"),
    size=(1300,750)
)

bg_label = ctk.CTkLabel(app, image=bg, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------------- Main Frame ----------------

main = ctk.CTkFrame(
    app,
    width=1000,
    height=680,
    corner_radius=20,
    fg_color="white"
)

main.place(relx=0.5, rely=0.5, anchor="center")

heading = ctk.CTkLabel(
    main,
    text="📝 Create Resume",
    font=("Segoe UI",30,"bold"),
    text_color="#1E3A8A"
)

heading.pack(pady=20)

# ---------------- Form ----------------

name = ctk.CTkEntry(
    main,
    width=420,
    height=40,
    placeholder_text="Full Name"
)
name.pack(pady=8)

email = ctk.CTkEntry(
    main,
    width=420,
    height=40,
    placeholder_text="Email"
)
email.pack(pady=8)

phone = ctk.CTkEntry(
    main,
    width=420,
    height=40,
    placeholder_text="Phone"
)
phone.pack(pady=8)

address = ctk.CTkEntry(
    main,
    width=420,
    height=40,
    placeholder_text="Address"
)
address.pack(pady=8)

# ================= Skills =================

ctk.CTkLabel(main, text="Skills", font=("Segoe UI",14,"bold")).pack(anchor="w", padx=340)

skills_frame = ctk.CTkFrame(
    main,
    width=420,
    height=80,
    fg_color="white",
    border_width=2,
    border_color="#C5C5C5",
    corner_radius=8
)
skills_frame.pack(pady=8)
skills_frame.pack_propagate(False)

skills = ctk.CTkTextbox(
    skills_frame,
    width=400,
    height=60,
    border_width=0
)
skills.pack(padx=8, pady=8)


# ================= Education =================

ctk.CTkLabel(main, text="Education", font=("Segoe UI",14,"bold")).pack(anchor="w", padx=340)

education_frame = ctk.CTkFrame(
    main,
    width=420,
    height=80,
    fg_color="white",
    border_width=2,
    border_color="#C5C5C5",
    corner_radius=8
)
education_frame.pack(pady=8)
education_frame.pack_propagate(False)

education = ctk.CTkTextbox(
    education_frame,
    width=400,
    height=60,
    border_width=0
)
education.pack(padx=8, pady=8)


# ================= Projects =================

ctk.CTkLabel(main, text="Projects", font=("Segoe UI",14,"bold")).pack(anchor="w", padx=340)

projects_frame = ctk.CTkFrame(
    main,
    width=420,
    height=80,
    fg_color="white",
    border_width=2,
    border_color="#C5C5C5",
    corner_radius=8
)
projects_frame.pack(pady=8)
projects_frame.pack_propagate(False)

projects = ctk.CTkTextbox(
    projects_frame,
    width=400,
    height=60,
    border_width=0
)
projects.pack(padx=8, pady=8)

# ---------------- FUNCTIONS ----------------

def clear_fields():
    name.delete(0, "end")
    email.delete(0, "end")
    phone.delete(0, "end")
    address.delete(0, "end")

    skills.delete("1.0", "end")
    education.delete("1.0", "end")
    projects.delete("1.0", "end")


def save_resume():

    if name.get() == "":
        messagebox.showerror("Error", "Please enter your name.")
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO resumes
        (name,email,phone,address,skills,education,projects)
        VALUES (?,?,?,?,?,?,?)
    """, (
        name.get(),
        email.get(),
        phone.get(),
        address.get(),
        skills.get("1.0","end").strip(),
        education.get("1.0","end").strip(),
        projects.get("1.0","end").strip()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Resume Saved Successfully!")

    clear_fields()


def back_dashboard():
    app.destroy()
    subprocess.Popen(["python", "dashboard.py"])
    # ---------------- BUTTONS ----------------

button_frame = ctk.CTkFrame(
    main,
    fg_color="transparent"
)
button_frame.pack(pady=20)

save_btn = ctk.CTkButton(
    button_frame,
    text="💾 Save Resume",
    width=180,
    height=45,
    command=save_resume
)
save_btn.grid(row=0, column=0, padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=180,
    height=45,
    fg_color="#F59E0B",
    hover_color="#D97706",
    command=clear_fields
)
clear_btn.grid(row=0, column=1, padx=10)

dashboard_btn = ctk.CTkButton(
    button_frame,
    text="🏠 Dashboard",
    width=180,
    height=45,
    fg_color="#16A34A",
    hover_color="#15803D",
    command=back_dashboard
)
dashboard_btn.grid(row=0, column=2, padx=10)

footer = ctk.CTkLabel(
    main,
    text="Smart Resume Builder v1.0 | Developed by Rohit Joshi",
    font=("Segoe UI", 12),
    text_color="gray40"
)
footer.pack(side="bottom", pady=15)

app.mainloop()