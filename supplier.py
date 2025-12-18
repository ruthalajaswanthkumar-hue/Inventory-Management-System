 
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1000x500+200+150")
        self.root.config(bg="white")

         
        self.var_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.search_invoice = StringVar()

         
        title = Label(self.root, text="Manage Supplier Details", font=("goudy old style", 20), bg="#0f4d7d", fg="white").place(x=0, y=0, relwidth=1)

         
        lbl_search = Label(self.root, text="Invoice No", font=("goudy old style", 15), bg="white").place(x=700, y=60)
        txt_search = Entry(self.root, textvariable=self.search_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=800, y=60, width=180)
        btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=890, y=100, width=90)

         
        lbl_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=20, y=60)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 15), bg="lightgray").place(x=150, y=60, width=200)

        lbl_name = Label(self.root, text="Supplier Name", font=("goudy old style", 15), bg="white").place(x=20, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=100, width=200)

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=20, y=140)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=140, width=200)

        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=20, y=180)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=150, y=180, width=300, height=100)

         
        btn_save = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=20, y=300, width=110, height=30)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white").place(x=140, y=300, width=110, height=30)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=260, y=300, width=110, height=30)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=380, y=300, width=110, height=30)

        
        self.supplier_table = ttk.Treeview(self.root, columns=("sup_id", "invoice", "name", "contact"), show='headings')
        self.supplier_table.place(x=500, y=140, width=480, height=300)

        self.supplier_table.heading("sup_id", text="Sup ID")
        self.supplier_table.heading("invoice", text="Invoice No.")
        self.supplier_table.heading("name", text="Name")
        self.supplier_table.heading("contact", text="Contact")

        self.supplier_table.column("sup_id", width=50)
        self.supplier_table.column("invoice", width=100)
        self.supplier_table.column("name", width=100)
        self.supplier_table.column("contact", width=100)

        self.supplier_table.bind("<ButtonRelease-1>", self.get_data)

        self.create_table()
        self.show()

    def create_table(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS supplier (
                        sup_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        invoice TEXT UNIQUE,
                        name TEXT,
                        contact TEXT,
                        description TEXT)""")
        con.commit()

    def add(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Invoice No already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, description) VALUES (?, ?, ?, ?)", (
                        self.var_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0', END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT sup_id, invoice, name, contact FROM supplier")
            rows = cur.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())
            for row in rows:
                self.supplier_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplier_table.focus()
        content = self.supplier_table.item(f)
        row = content['values']
        if row:
            con = sqlite3.connect(database="ims.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM supplier WHERE sup_id=?", (row[0],))
            data = cur.fetchone()
            if data:
                self.clear()
                self.var_invoice.set(data[1])
                self.var_name.set(data[2])
                self.var_contact.set(data[3])
                self.txt_desc.delete("1.0", END)
                self.txt_desc.insert(END, data[4])

    def update(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Please select supplier from the list", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid invoice no", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, description=? WHERE invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get("1.0", END),
                        self.var_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Invoice no. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice no", parent=self.root)
                else:
                    cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete("1.0", END)

    def search(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.search_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. required to search", parent=self.root)
            else:
                cur.execute("SELECT sup_id, invoice, name, contact FROM supplier WHERE invoice=?", (self.search_invoice.get(),))
                rows = cur.fetchall()
                if rows:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    for row in rows:
                        self.supplier_table.insert('', END, values=row)
                else:
                    messagebox.showinfo("Info", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
