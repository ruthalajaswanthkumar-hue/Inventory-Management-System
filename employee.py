
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class EmployeeClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System | Employee Management")
        self.root.geometry("1100x500+220+130")
        self.root.config(bg="white")
        self.root.focus_force()

         
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                eid TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                gender TEXT,
                contact TEXT,
                dob TEXT,
                doj TEXT,
                password TEXT,
                utype TEXT,
                address TEXT,
                salary TEXT
            )
        """)
        con.commit()
        con.close()

        
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        
        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style", 12, "bold"))
        SearchFrame.place(x=250, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER)
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 12), bg="lightyellow")
        txt_search.place(x=200, y=10)

        btn_search = Button(SearchFrame, text="Search", font=("goudy old style", 12), bg="#4caf50", fg="white")
        btn_search.place(x=410, y=9, width=150, height=30)

        
        lbl_empid = Label(self.root, text="Emp No.", bg="white", font=("goudy old style", 12))
        lbl_empid.place(x=10, y=100)
        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 12), bg="lightyellow")
        txt_empid.place(x=100, y=100, width=180)

        lbl_gender = Label(self.root, text="Gender", bg="white", font=("goudy old style", 12))
        lbl_gender.place(x=300, y=100)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Male", "Female", "Other"), state='readonly', justify=CENTER)
        cmb_gender.place(x=380, y=100, width=180)
        cmb_gender.current(0)

        lbl_contact = Label(self.root, text="Contact No.", bg="white", font=("goudy old style", 12))
        lbl_contact.place(x=580, y=100)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 12), bg="lightyellow")
        txt_contact.place(x=680, y=100, width=180)

        lbl_doj = Label(self.root, text="D.O.J", bg="white", font=("goudy old style", 12))
        lbl_doj.place(x=880, y=100)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 12), bg="lightyellow")
        txt_doj.place(x=940, y=100, width=150)

        lbl_name = Label(self.root, text="Name", bg="white", font=("goudy old style", 12))
        lbl_name.place(x=10, y=140)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 12), bg="lightyellow")
        txt_name.place(x=100, y=140, width=180)

        lbl_dob = Label(self.root, text="D.O.B", bg="white", font=("goudy old style", 12))
        lbl_dob.place(x=300, y=140)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 12), bg="lightyellow")
        txt_dob.place(x=380, y=140, width=180)

        lbl_email = Label(self.root, text="Email", bg="white", font=("goudy old style", 12))
        lbl_email.place(x=580, y=140)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 12), bg="lightyellow")
        txt_email.place(x=680, y=140, width=180)

        lbl_pass = Label(self.root, text="Password", bg="white", font=("goudy old style", 12))
        lbl_pass.place(x=880, y=140)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 12), bg="lightyellow")
        txt_pass.place(x=940, y=140, width=150)

        lbl_utype = Label(self.root, text="User Type", bg="white", font=("goudy old style", 12))
        lbl_utype.place(x=10, y=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state='readonly', justify=CENTER)
        cmb_utype.place(x=100, y=180, width=180)
        cmb_utype.current(0)

        lbl_address = Label(self.root, text="Address", bg="white", font=("goudy old style", 12))
        lbl_address.place(x=300, y=180)
        self.txt_address = Text(self.root, font=("goudy old style", 12), bg="lightyellow")
        self.txt_address.place(x=380, y=180, width=180, height=60)

        lbl_salary = Label(self.root, text="Salary", bg="white", font=("goudy old style", 12))
        lbl_salary.place(x=580, y=180)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 12), bg="lightyellow")
        txt_salary.place(x=680, y=180, width=180)

        btn_save = Button(self.root, text="Save", command=self.add, font=("goudy old style", 12), bg="#2196f3", fg="white")
        btn_save.place(x=880, y=180, width=110, height=28)

        btn_update = Button(self.root, text="Update", font=("goudy old style", 12), bg="#4caf50", fg="white")
        btn_update.place(x=880, y=210, width=110, height=28)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 12), bg="#f44336", fg="white")
        btn_delete.place(x=1000, y=180, width=90, height=28)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 12), bg="#607d8b", fg="white")
        btn_clear.place(x=1000, y=210, width=90, height=28)

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=250, relwidth=1, height=250)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        for col in self.EmployeeTable["columns"]:
            self.EmployeeTable.heading(col, text=col.title())
            self.EmployeeTable.column(col, width=100)

        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.show()

    def add(self):
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=self.root)
            else:
                con = sqlite3.connect("ims.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID already exists", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO employee (eid, name, email, gender, contact, dob, doj, password, utype, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get("1.0", END),
                            self.var_salary.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()
        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
        for row in rows:
            self.EmployeeTable.insert('', END, values=row)

if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()
