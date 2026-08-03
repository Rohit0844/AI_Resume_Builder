import customtkinter as ctk
from PIL import Image
from tkinter import Menu, messagebox
from datetime import datetime
import sqlite3
import subprocess

# =========================
# Appearance
# =========================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# =========================
# Main Window
# =========================

app = ctk.CTk()
app.title("Smart Resume Builder & Management System")
app.geometry("1300x750")
app.resizable(False, False)

# =========================
# Background Image
# =========================

bg = ctk.CTkImage(
    light_image=Image.open("assets/dash.png"),
    dark_image=Image.open("assets/dash.png"),
    size=(1300,750)
)

bg_label = ctk.CTkLabel(
    app,
    image=bg,
    text=""
)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# =========================
# Database Statistics
# =========================

try:
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM resumes")
    total_resume = cursor.fetchone()[0]

    conn.close()

except:
    total_resume = 0

# =========================
# Functions
# =========================

def create_resume():
    subprocess.Popen(["python", "resume_form.py"])

def view_resume():
    subprocess.Popen(["python", "view_resume.py"])

def edit_resume():
    subprocess.Popen(["python", "edit_resume.py"])

from pdf_generator import generate_pdf

import sys
import os

def open_settings():
    path = os.path.join(os.path.dirname(__file__), "settings.py")
    subprocess.Popen([sys.executable, path])
    
def exit_app():
    app.destroy()

def about():
    messagebox.showinfo(
        "About",
        "Smart Resume Builder & Management System\n\n"
        "Version : 1.0\n"
        "Developer : Rohit Joshi\n\n"
        "Python | CustomTkinter | SQLite | ReportLab"
    )

# =========================
# Live Clock
# =========================

def update_clock():

    current = datetime.now().strftime("%d-%m-%Y   %I:%M:%S %p")

    clock.configure(text=current)

    app.after(1000, update_clock)

# =========================
# Menu Bar
# =========================

menu_bar = Menu(app)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Create Resume", command=create_resume)
file_menu.add_command(label="View Resume", command=view_resume)
file_menu.add_command(label="Edit Resume", command=edit_resume)
file_menu.add_command(label="Generate PDF", command=generate_pdf)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)

help_menu.add_command(label="About", command=about)

menu_bar.add_cascade(label="Help", menu=help_menu)

app.config(menu=menu_bar)

# ==========================================
# SIDEBAR
# ==========================================

sidebar = ctk.CTkFrame(
    app,
    width=230,
    fg_color="#1E3A8A",
    corner_radius=0
)

sidebar.pack(side="left", fill="y")

# ==========================================
# LOGO
# ==========================================

logo = ctk.CTkImage(
    light_image=Image.open("assets/logo.png"),
    dark_image=Image.open("assets/logo.png"),
    size=(80,80)
)

logo_label = ctk.CTkLabel(
    sidebar,
    image=logo,
    text=""
)

logo_label.pack(pady=(25,10))

# ==========================================
# PROJECT TITLE
# ==========================================

title = ctk.CTkLabel(
    sidebar,
    text="Smart Resume\nBuilder",
    font=("Segoe UI",22,"bold"),
    text_color="white"
)

title.pack()

subtitle = ctk.CTkLabel(
    sidebar,
    text="Management System",
    font=("Segoe UI",12),
    text_color="white"
)

subtitle.pack(pady=(0,25))

# ==========================================
# SIDEBAR BUTTONS
# ==========================================

button_style = {
    "width":180,
    "height":45,
    "corner_radius":12,
    "font":("Segoe UI",14,"bold")
}

ctk.CTkButton(
    sidebar,
    text="🏠 Dashboard",
    **button_style
).pack(pady=6)

ctk.CTkButton(
    sidebar,
    text="📝 Create Resume",
    command=create_resume,
    **button_style
).pack(pady=6)

ctk.CTkButton(
    sidebar,
    text="📂 View Resume",
    command=view_resume,
    **button_style
).pack(pady=6)

ctk.CTkButton(
    sidebar,
    text="✏ Edit Resume",
    command=edit_resume,
    **button_style
).pack(pady=6)

ctk.CTkButton(
    sidebar,
    text="📄 Generate PDF",
    command=generate_pdf,
    **button_style
).pack(pady=6)

ctk.CTkButton(
    sidebar,
    text="⚙ Settings",
    command=open_settings,
    **button_style
).pack(pady=6)

ctk.CTkButton(
    sidebar,
    text="🚪 Exit",
    command=exit_app,
    fg_color="#DC2626",
    hover_color="#B91C1C",
    **button_style
).pack(pady=20)

# ==========================================
# MAIN GLASS PANEL
# ==========================================

main = ctk.CTkFrame(
    app,
    width=1020,
    height=690,
    fg_color="white",
    corner_radius=20,
    border_width=2,
    border_color="#D1D5DB"
)

main.place(x=260, y=30)

# ==========================================
# HEADER
# ==========================================

heading = ctk.CTkLabel(
    main,
    text="📊 Dashboard",
    font=("Segoe UI",30,"bold"),
    text_color="#1E3A8A"
)

heading.place(x=30,y=20)

welcome = ctk.CTkLabel(
    main,
    text="Welcome, Admin 👋",
    font=("Segoe UI",18)
)

welcome.place(x=30,y=65)

# ==========================================
# LIVE CLOCK
# ==========================================

clock = ctk.CTkLabel(
    main,
    text="",
    font=("Segoe UI",15,"bold"),
    text_color="#374151"
)

clock.place(x=720,y=25)

update_clock()

# ==========================================
# ADMIN PROFILE
# ==========================================

profile = ctk.CTkFrame(
    main,
    width=220,
    height=80,
    corner_radius=15,
    fg_color="#F8FAFC"
)

profile.place(x=760,y=70)

ctk.CTkLabel(
    profile,
    text="👤 Administrator",
    font=("Segoe UI",16,"bold")
).pack(pady=(10,2))

ctk.CTkLabel(
    profile,
    text="Resume Management",
    font=("Segoe UI",12),
    text_color="gray40"
).pack()

# ==========================================
# DASHBOARD CARDS
# ==========================================

cards = ctk.CTkFrame(
    main,
    fg_color="transparent"
)

cards.place(x=30, y=180)

# ---------- Card 1 ----------

card1 = ctk.CTkFrame(
    cards,
    width=220,
    height=130,
    corner_radius=18,
    fg_color="#FFFFFF",
    border_width=1,
    border_color="#E5E7EB"
)

card1.grid(row=0,column=0,padx=15)

ctk.CTkLabel(
    card1,
    text="📄 Total Resumes",
    font=("Segoe UI",18,"bold")
).pack(pady=(18,5))

ctk.CTkLabel(
    card1,
    text=str(total_resume),
    font=("Segoe UI",34,"bold"),
    text_color="#2563EB"
).pack()

# ---------- Card 2 ----------

card2 = ctk.CTkFrame(
    cards,
    width=220,
    height=130,
    corner_radius=18,
    fg_color="#FFFFFF",
    border_width=1,
    border_color="#E5E7EB"
)

card2.grid(row=0,column=1,padx=15)

ctk.CTkLabel(
    card2,
    text="📄 PDF Generator",
    font=("Segoe UI",18,"bold")
).pack(pady=(18,5))

ctk.CTkLabel(
    card2,
    text="Ready",
    font=("Segoe UI",30,"bold"),
    text_color="#16A34A"
).pack()

# ---------- Card 3 ----------

card3 = ctk.CTkFrame(
    cards,
    width=220,
    height=130,
    corner_radius=18,
    fg_color="#FFFFFF",
    border_width=1,
    border_color="#E5E7EB"
)

card3.grid(row=0,column=2,padx=15)

ctk.CTkLabel(
    card3,
    text="💾 Database",
    font=("Segoe UI",18,"bold")
).pack(pady=(18,5))

ctk.CTkLabel(
    card3,
    text="SQLite",
    font=("Segoe UI",28,"bold"),
    text_color="#F59E0B"
).pack()

# ---------- Card 4 ----------

card4 = ctk.CTkFrame(
    cards,
    width=220,
    height=130,
    corner_radius=18,
    fg_color="#FFFFFF",
    border_width=1,
    border_color="#E5E7EB"
)

card4.grid(row=0,column=3,padx=15)

ctk.CTkLabel(
    card4,
    text="👤 User",
    font=("Segoe UI",18,"bold")
).pack(pady=(18,5))

ctk.CTkLabel(
    card4,
    text="Admin",
    font=("Segoe UI",28,"bold"),
    text_color="#7C3AED"
).pack()

# ==========================================
# QUICK ACTIONS
# ==========================================

ctk.CTkLabel(
    main,
    text="Quick Actions",
    font=("Segoe UI",24,"bold"),
    text_color="#1F2937"
).place(x=30,y=360)

button_style = {
    "width":220,
    "height":50,
    "corner_radius":15,
    "font":("Segoe UI",15,"bold")
}

create_btn = ctk.CTkButton(
    main,
    text="📝 Create Resume",
    command=create_resume,
    **button_style
)
create_btn.place(x=30,y=420)

view_btn = ctk.CTkButton(
    main,
    text="📂 View Resume",
    fg_color="#16A34A",
    hover_color="#15803D",
    command=view_resume,
    **button_style
)
view_btn.place(x=290,y=420)

edit_btn = ctk.CTkButton(
    main,
    text="✏ Edit Resume",
    fg_color="#F59E0B",
    hover_color="#D97706",
    text_color="black",
    command=edit_resume,
    **button_style
)
edit_btn.place(x=550,y=420)

pdf_btn = ctk.CTkButton(
    main,
    text="📄 Generate PDF",
    fg_color="#7C3AED",
    hover_color="#6D28D9",
    command=generate_pdf,
    **button_style
)
pdf_btn.place(x=810,y=420)

settings_btn = ctk.CTkButton(
    main,
    text="⚙ Settings",
    fg_color="#0EA5E9",
    hover_color="#0284C7",
    command=open_settings,
    **button_style
)
settings_btn.place(x=160,y=500)

about_btn = ctk.CTkButton(
    main,
    text="ℹ About",
    fg_color="#6B7280",
    hover_color="#4B5563",
    command=about,
    **button_style
)
about_btn.place(x=420,y=500)

exit_btn = ctk.CTkButton(
    main,
    text="🚪 Exit",
    fg_color="#DC2626",
    hover_color="#B91C1C",
    command=exit_app,
    **button_style
)
exit_btn.place(x=680,y=500)

# ==========================================
# FOOTER
# ==========================================

footer = ctk.CTkFrame(
    app,
    height=35,
    fg_color="#1F2937",
    corner_radius=0
)

footer.pack(side="bottom", fill="x")

footer_text = ctk.CTkLabel(
    footer,
    text="Smart Resume Builder & Management System  |  Version 1.0  |  Developed by Rohit Joshi",
    font=("Segoe UI",12),
    text_color="white"
)

footer_text.pack(pady=6)

# ==========================================
# STATUS BAR
# ==========================================

status = ctk.CTkFrame(
    main,
    width=960,
    height=45,
    corner_radius=15,
    fg_color="#EFF6FF"
)

status.place(x=30, y=610)

status_label = ctk.CTkLabel(
    status,
    text="🟢 System Status : Ready | Database Connected | Dashboard Loaded Successfully",
    font=("Segoe UI",13,"bold"),
    text_color="#2563EB"
)

status_label.pack(pady=10)

# ==========================================
# COPYRIGHT
# ==========================================

copyright_label = ctk.CTkLabel(
    main,
    text="© 2026 Rohit Joshi | Python • CustomTkinter • SQLite • ReportLab",
    font=("Segoe UI",11),
    text_color="gray50"
)

copyright_label.place(x=280, y=660)

# ==========================================
# WELCOME MESSAGE
# ==========================================

messagebox.showinfo(
    "Welcome",
    "Welcome to Smart Resume Builder & Management System!"
)

# ==========================================
# RUN APPLICATION
# ==========================================

app.mainloop()