 
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class CategoryClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("900x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        
        title = Label(self.root, text="Manage Product Category", font=("goudy old style", 20, "bold"),
                      bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X, pady=10)

         
        name_label = Label(self.root, text="Enter Category Name", font=("goudy old style", 15), bg="white")
        name_label.place(x=30, y=70)

        name_entry = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        name_entry.place(x=30, y=110, width=300)

        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 15),
                         bg="green", fg="white", cursor="hand2")
        btn_add.place(x=340, y=110, width=100, height=30)

        btn_delete = Button(self.root, text="DELETE", command=self.delete, font=("goudy old style", 15),
                            bg="red", fg="white", cursor="hand2")
        btn_delete.place(x=450, y=110, width=100, height=30)

         
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=600, y=70, width=280, height=400)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.category_table = ttk.Treeview(cat_frame, columns=("cid", "name"),
                                           yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("cid", text="C ID")
        self.category_table.heading("name", text="Name")
        self.category_table["show"] = "headings"
        self.category_table.column("cid", width=50)
        self.category_table.column("name", width=150)

        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)

         
        try:
            self.cat1_img = PhotoImage(file="images/img9.png")
            self.cat2_img = PhotoImage(file="images/img6.png")
            lbl_cat1 = Label(self.root, image=self.cat1_img, bg="white")
            lbl_cat2 = Label(self.root, image=self.cat2_img, bg="white")
            lbl_cat1.place(x=30, y=160)
            lbl_cat2.place(x=350, y=160)
        except Exception as e:
            print("Image load error:", e)

        self.create_table()
        self.show()

    def create_table(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS category (cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")
        con.commit()
        con.close()

    def add(self):
        if self.var_name.get() == "":
            messagebox.showerror("Error", "Category Name must be required", parent=self.root)
            return
        try:
            con = sqlite3.connect(database="ims.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
            row = cur.fetchone()
            if row:
                messagebox.showerror("Error", "This Category already exists, try another", parent=self.root)
            else:
                cur.execute("INSERT INTO category (name) VALUES (?)", (self.var_name.get(),))
                con.commit()
                messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        try:
            con = sqlite3.connect(database="ims.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        selected = self.category_table.focus()
        content = self.category_table.item(selected)
        row = content["values"]
        if row:
            self.var_cat_id.set(row[0])
            self.var_name.set(row[1])

    def delete(self):
        if self.var_cat_id.get() == "":
            messagebox.showerror("Error", "Please select a category from the list", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="ims.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if not row:
                    messagebox.showerror("Error", "Invalid Category ID", parent=self.root)
                else:
                    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this category?",
                                                  parent=self.root)
                    if confirm:
                        cur.execute("DELETE FROM category WHERE cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

 
if __name__ == "__main__":
    root = Tk()
    obj = CategoryClass(root)
    root.mainloop()
