from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management")
        self.root.geometry("1050x500+220+220")
        self.root.config(bg="white")
        self.root.focus_force()

        
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        self.cat_list = []
        self.sup_list = []

         
        title = Label(self.root, text="Manage Product Details", font=("goudy old style", 20), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

         
        Label(self.root, text="Category", font=("goudy old style", 15), bg="white").place(x=30, y=60)
        Label(self.root, text="Supplier", font=("goudy old style", 15), bg="white").place(x=400, y=60)
        Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=30, y=110)
        Label(self.root, text="Price", font=("goudy old style", 15), bg="white").place(x=400, y=110)
        Label(self.root, text="Quantity", font=("goudy old style", 15), bg="white").place(x=30, y=160)
        Label(self.root, text="Status", font=("goudy old style", 15), bg="white").place(x=400, y=160)

        self.cmb_cat = ttk.Combobox(self.root, textvariable=self.var_cat, state="readonly", font=("goudy old style", 13), justify=CENTER)
        self.cmb_cat.place(x=150, y=60, width=200)

        self.cmb_sup = ttk.Combobox(self.root, textvariable=self.var_sup, state="readonly", font=("goudy old style", 13), justify=CENTER)
        self.cmb_sup.place(x=580, y=60, width=200)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 13), bg="lightyellow").place(x=150, y=110, width=200)
        Entry(self.root, textvariable=self.var_price, font=("goudy old style", 13), bg="lightyellow").place(x=580, y=110, width=200)
        Entry(self.root, textvariable=self.var_qty, font=("goudy old style", 13), bg="lightyellow").place(x=150, y=160, width=200)

        self.cmb_status = ttk.Combobox(self.root, textvariable=self.var_status, values=("Active", "Inactive"), state="readonly", font=("goudy old style", 13), justify=CENTER)
        self.cmb_status.place(x=580, y=160, width=200)
        self.cmb_status.current(0)

        
        Button(self.root, text="Save", command=self.add_product, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=150, y=220, width=110, height=35)
        Button(self.root, text="Update", command=self.update_product, font=("goudy old style", 15), bg="#4caf50", fg="white").place(x=270, y=220, width=110, height=35)
        Button(self.root, text="Delete", command=self.delete_product, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=390, y=220, width=110, height=35)
        Button(self.root, text="Clear", command=self.clear_fields, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=510, y=220, width=110, height=35)

        
        product_frame = Frame(self.root, bd=3, relief=RIDGE)
        product_frame.place(x=0, y=270, relwidth=1, height=230)

        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(product_frame, columns=("pid", "Category", "Supplier", "Name", "Price", "Quantity", "Status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        for col in ("pid", "Category", "Supplier", "Name", "Price", "Quantity", "Status"):
            self.product_table.heading(col, text=col)
            self.product_table.column(col, width=100)
        self.product_table["show"] = "headings"
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        
        self.create_product_table()
        self.fetch_cat_sup()
        self.show_products()

    def create_product_table(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS product (
                pid INTEGER PRIMARY KEY AUTOINCREMENT,
                Category TEXT,
                Supplier TEXT,
                Name TEXT,
                Price TEXT,
                Quantity TEXT,
                Status TEXT
            )
        """)
        con.commit()
        con.close()

    def fetch_cat_sup(self):
        try:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            cur.execute("SELECT name FROM category")
            self.cmb_cat['values'] = [row[0] for row in cur.fetchall()]
            cur.execute("SELECT name FROM supplier")
            self.cmb_sup['values'] = [row[0] for row in cur.fetchall()]
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching data: {str(ex)}", parent=self.root)

    def add_product(self):
        try:
            if self.var_cat.get() == "" or self.var_sup.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            cur.execute("INSERT INTO product (Category, Supplier, Name, Price, Quantity, Status) VALUES (?, ?, ?, ?, ?, ?)", (
                self.var_cat.get(), self.var_sup.get(), self.var_name.get(),
                self.var_price.get(), self.var_qty.get(), self.var_status.get()
            ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Product added successfully", parent=self.root)
            self.show_products()
            self.clear_fields()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def show_products(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM product")
        rows = cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
            self.product_table.insert("", END, values=row)
        con.close()

    def get_data(self, ev):
        selected = self.product_table.focus()
        data = self.product_table.item(selected)["values"]
        if data:
            self.var_pid.set(data[0])
            self.var_cat.set(data[1])
            self.var_sup.set(data[2])
            self.var_name.set(data[3])
            self.var_price.set(data[4])
            self.var_qty.set(data[5])
            self.var_status.set(data[6])

    def update_product(self):
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select a product to update", parent=self.root)
                return
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            cur.execute("UPDATE product SET Category=?, Supplier=?, Name=?, Price=?, Quantity=?, Status=? WHERE pid=?", (
                self.var_cat.get(), self.var_sup.get(), self.var_name.get(),
                self.var_price.get(), self.var_qty.get(), self.var_status.get(), self.var_pid.get()
            ))
            con.commit()
            con.close()
            messagebox.showinfo("Updated", "Product updated successfully", parent=self.root)
            self.show_products()
            self.clear_fields()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def delete_product(self):
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select a product to delete", parent=self.root)
                return
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            cur.execute("DELETE FROM product WHERE pid=?", (self.var_pid.get(),))
            con.commit()
            con.close()
            messagebox.showinfo("Deleted", "Product deleted successfully", parent=self.root)
            self.show_products()
            self.clear_fields()
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)

    def clear_fields(self):
        self.var_pid.set("")
        self.var_cat.set("")
        self.var_sup.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.cmb_status.current(0)

if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
