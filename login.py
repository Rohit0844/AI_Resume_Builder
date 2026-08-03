import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart Resume Builder")
app.geometry("1200x700")
app.resizable(False, False)

# ================= Background =================

bg = ctk.CTkImage(
    Image.open("assets/login_bg.webp"),
    size=(1200,700)
)

bg_label = ctk.CTkLabel(app, image=bg, text="")
bg_label.place(x=0,y=0)

# ================= Login Card =================

card = ctk.CTkFrame(
    app,
    width=420,
    height=520,
    corner_radius=25,
    fg_color="white"
)

card.place(relx=0.72,rely=0.5,anchor="center")

# ================= Logo =================

logo = ctk.CTkImage(
    Image.open("assets/logo.png"),
    size=(90,90)
)

logo_label = ctk.CTkLabel(card,image=logo,text="")
logo_label.pack(pady=(25,10))

# ================= Title =================

title = ctk.CTkLabel(
    card,
    text="Smart Resume Builder",
    font=("Segoe UI",28,"bold"),
    text_color="#1E3A8A"
)

title.pack()

subtitle = ctk.CTkLabel(
    card,
    text="Welcome Back",
    font=("Segoe UI",16)
)

subtitle.pack(pady=(0,25))

# ================= Username =================

username = ctk.CTkEntry(
    card,
    width=300,
    height=45,
    placeholder_text="Username",
    corner_radius=12
)

username.pack(pady=10)

# ================= Password =================

password = ctk.CTkEntry(
    card,
    width=300,
    height=45,
    placeholder_text="Password",
    show="*",
    corner_radius=12
)

password.pack(pady=10)

# ================= Login =================

def login():

    if username.get()=="admin" and password.get()=="1234":

        app.destroy()

        import dashboard

    else:

        error.configure(text="Invalid Username or Password")

login_btn = ctk.CTkButton(
    card,
    text="Login",
    width=300,
    height=45,
    corner_radius=12,
    font=("Segoe UI",15,"bold"),
    command=login
)

login_btn.pack(pady=25)

error = ctk.CTkLabel(
    card,
    text="",
    text_color="red"
)

error.pack()

footer = ctk.CTkLabel(
    card,
    text="Version 1.0\nPython | SQLite | ReportLab",
    font=("Segoe UI",12)
)

footer.pack(side="bottom",pady=20)

app.mainloop()