import customtkinter as ctk
from PIL import Image
import subprocess

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Settings")
app.geometry("900x600")
app.resizable(False, False)

# ================= Background =================

bg = ctk.CTkImage(
    light_image=Image.open("assets/sett_bg.webp"),
    dark_image=Image.open("assets/sett_bg.webp"),
    size=(900, 600)
)

bg_label = ctk.CTkLabel(
    app,
    image=bg,
    text=""
)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ================= Header =================

header = ctk.CTkFrame(
    app,
    height=70,
    corner_radius=0,
    fg_color="transparent"
)
header.pack(fill="x")

title = ctk.CTkLabel(
    header,
    text="⚙ Settings",
    font=("Segoe UI", 26, "bold"),
    fg_color="transparent"
)
title.pack(pady=18)

# ================= Main =================

main = ctk.CTkFrame(
    app,
    width=820,
    height=500,
    fg_color="#FFFFFF",
    corner_radius=20,
    border_width=2,
    border_color="#D1D5DB"
)

main.place(relx=0.5, rely=0.55, anchor="center")

# Appearance
ctk.CTkLabel(
    main,
    text="Appearance",
    font=("Segoe UI", 18, "bold")
).pack(anchor="w", pady=(10,5))

theme = ctk.CTkOptionMenu(
    main,
    values=["Light", "Dark", "System"],
    command=lambda mode: ctk.set_appearance_mode(mode.lower())
)
theme.pack(anchor="w", pady=5)

# Color Theme
ctk.CTkLabel(
    main,
    text="Theme Color",
    font=("Segoe UI", 18, "bold")
).pack(anchor="w", pady=(20,5))

color = ctk.CTkOptionMenu(
    main,
    values=["blue", "green", "dark-blue"],
    command=ctk.set_default_color_theme
)
color.pack(anchor="w", pady=5)

# Developer Info
ctk.CTkLabel(
    main,
    text="Developer",
    font=("Segoe UI", 18, "bold")
).pack(anchor="w", pady=(20,5))

ctk.CTkLabel(
    main,
    text="Rohit Joshi\nPython Developer",
    font=("Segoe UI", 14)
).pack(anchor="w")

# Back Button
def back():
    app.destroy()
    subprocess.Popen(["python", "dashboard.py"])

ctk.CTkButton(
    main,
    text="🏠 Back to Dashboard",
    width=220,
    command=back
).pack(pady=30)

app.mainloop()