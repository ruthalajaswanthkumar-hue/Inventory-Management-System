from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def login():
    username = txt_user.get()
    password = txt_pass.get()
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Success", "Welcome!")
        root.destroy()
        os.system("python dashboard.py")
    else:
        messagebox.showerror("Error", "Invalid Username or Password try again")

root = Tk()
root.title("Login")
root.geometry("400x400")
root.config(bg="white")

 
try:
    img = Image.open("images/img0.png")  
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    lbl_img = Label(root, image=photo, bg="white")
    lbl_img.image = photo  
    lbl_img.place(x=125, y=10)
except Exception as e:
    print(f"Image load error: {e}")

 
Label(root, text="Username", font=("Arial", 14), bg="white").place(x=50, y=180)
txt_user = Entry(root, font=("Arial", 14), bg="lightyellow")
txt_user.place(x=170, y=180)

 
Label(root, text="Password", font=("Arial", 14), bg="white").place(x=50, y=230)
txt_pass = Entry(root, show="*", font=("Arial", 14), bg="lightyellow")
txt_pass.place(x=170, y=230)

 
btn_login = Button(root, text="Login", command=login, font=("Arial", 14), bg="blue", fg="white")
btn_login.place(x=150, y=280)

root.mainloop()
