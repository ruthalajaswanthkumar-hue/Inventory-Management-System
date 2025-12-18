
from tkinter import *
from PIL import Image, ImageTk
import time
import employee, supplier, category, product, billing
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

         
        icon_path = os.path.join(BASE_DIR, "images", "img1.png")
        icon_img = Image.open(icon_path)
        icon_img = icon_img.resize((50, 50))
        self.icon_title = ImageTk.PhotoImage(icon_img)

        

        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="orange", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

         
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2", command=self.root.destroy)
        btn_logout.place(x=1150, y=10, height=50, width=150)

         
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="yellow")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

         
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        menu_logo_path = os.path.join(BASE_DIR, "images", "img8.png")
        self.menu_logo = Image.open(menu_logo_path)
 
        self.menu_logo = self.menu_logo.resize((200, 200))
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        lbl_menu_logo = Label(LeftMenu, image=self.menu_logo)
        lbl_menu_logo.pack(side=TOP, fill=X)

        menu_label = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        menu_label.pack(side=TOP, fill=X)

         
        btn_employee = Button(LeftMenu, text=">> Employee", command=self.open_employee, font=("times new roman", 15), anchor="w", bg="orange", bd=3, relief=RIDGE)
        btn_employee.pack(fill=X)
        btn_supplier = Button(LeftMenu, text=">> Supplier", command=self.open_supplier, font=("times new roman", 15), anchor="w", bg="pink", bd=3, relief=RIDGE)
        btn_supplier.pack(fill=X)
        btn_category = Button(LeftMenu, text=">> Category", command=self.open_category, font=("times new roman", 15), anchor="w", bg="light blue", bd=3, relief=RIDGE)
        btn_category.pack(fill=X)
        btn_product = Button(LeftMenu, text=">> Products", command=self.open_product, font=("times new roman", 15), anchor="w", bg="yellow", bd=3, relief=RIDGE)
        btn_product.pack(fill=X)
         
        btn_billing = Button(LeftMenu, text=">> Billing", command=self.open_billing, font=("times new roman", 15), anchor="w", bg="grey", bd=3, relief=RIDGE)
        btn_billing.pack(fill=X)
        btn_exit = Button(LeftMenu, text=">> Exit", command=self.root.destroy, font=("times new roman", 15), anchor="w", bg="green", bd=3, relief=RIDGE)
        btn_exit.pack(fill=X)

         
        self.label_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE,
                                    bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.label_employee.place(x=300, y=120, height=150, width=300)

        self.label_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE,
                                    bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.label_supplier.place(x=650, y=120, height=150, width=300)

        self.label_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE,
                                    bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.label_category.place(x=1000, y=120, height=150, width=300)

        self.label_product = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE,
                                   bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.label_product.place(x=475, y=300, height=150, width=300)

         

         
        lbl_footer = Label(self.root, text="IMS - Inventory Management System | Developed by jaswanth\nFor any technical issues contact:",
                           font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

        self.update_content()

    
    def open_employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employee.EmployeeClass(self.new_win)

    def open_supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplier.SupplierClass(self.new_win)

    def open_category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = category.CategoryClass(self.new_win)

    def open_product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = product.ProductClass(self.new_win)

    

    def open_billing(self):
        
        self.new_obj = billing.BillClass(self.root)

    def update_content(self):
         
        self.label_employee.config(text="Total Employee\n[ 2 ]")
        self.label_supplier.config(text="Total Supplier\n[ 2 ]")
        self.label_category.config(text="Total Category\n[ 3 ]")
        self.label_product.config(text="Total Product\n[ 5 ]")
        

        time_str = time.strftime("%H:%M:%S")
        date_str = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {date_str}\t\t Time: {time_str}")
        self.root.after(1000, self.update_content)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
