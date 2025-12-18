 
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System | Billing")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
 
        title = Label(self.root, text="Welcome to Inventory Management System", font=("times new roman", 20), bg="gray20", fg="white")
        title.pack(side=TOP, fill=X)

         
        product_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_frame.place(x=10, y=50, width=300, height=500)

        title1 = Label(product_frame, text="All Products", font=("goudy old style", 20, "bold"), bg="black", fg="white")
        title1.pack(side=TOP, fill=X)

        lbl_search = Label(product_frame, text="Search Product | By Name", font=("times new roman", 12, "bold"), bg="white", fg="green")
        lbl_search.place(x=5, y=40)

        self.var_search = StringVar()
        txt_search = Entry(product_frame, textvariable=self.var_search, font=("times new roman", 12), bg="lightyellow")
        txt_search.place(x=5, y=70, width=180)

        btn_show_all = Button(product_frame, text="Show All", font=("times new roman", 12), bg="darkgreen", fg="white", command=self.show_products)
        btn_show_all.place(x=190, y=70, width=90)

        btn_search = Button(product_frame, text="Search", font=("times new roman", 12), bg="blue", fg="white", command=self.search_product)
        btn_search.place(x=5, y=100, width=275)

        
        self.product_table = ttk.Treeview(product_frame, columns=("pid", "name", "price", "qty", "status"), show="headings")
        self.product_table.heading("pid", text="P ID")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="QTY")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=30)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=60)
        self.product_table.column("qty", width=50)
        self.product_table.column("status", width=60)

        self.product_table.place(x=5, y=140, width=285, height=350)
        self.product_table.bind("<Double-1>", self.add_to_cart)

        lbl_note = Label(product_frame, text="Note: 'Enter 0 QTY to Remove the Product from Cart'", font=("times new roman", 9), bg="white", fg="red")
        lbl_note.place(x=5, y=495)

        
        self.products = [
            {"pid": "101", "name": "Laptop", "price": 999.99, "qty": 10, "status": "In Stock"},
            {"pid": "102", "name": "Mouse", "price": 19.99, "qty": 50, "status": "In Stock"},
            {"pid": "103", "name": "Keyboard", "price": 49.99, "qty": 30, "status": "In Stock"},
            {"pid": "104", "name": "Monitor", "price": 199.99, "qty": 15, "status": "In Stock"},
            {"pid": "105", "name": "Headphones", "price": 79.99, "qty": 25, "status": "In Stock"}
        ]
        self.show_products()

         
        customer_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        customer_frame.place(x=320, y=50, width=500, height=500)

        title2 = Label(customer_frame, text="Customer Details", font=("goudy old style", 15), bg="lightgray")
        title2.pack(side=TOP, fill=X)

        lbl_name = Label(customer_frame, text="Name", font=("times new roman", 12), bg="white")
        lbl_name.place(x=5, y=40)
        self.txt_name = Entry(customer_frame, font=("times new roman", 12), bg="lightyellow")
        self.txt_name.place(x=60, y=40, width=200)

        lbl_contact = Label(customer_frame, text="Contact No.", font=("times new roman", 12), bg="white")
        lbl_contact.place(x=270, y=40)
        self.txt_contact = Entry(customer_frame, font=("times new roman", 12), bg="lightyellow")
        self.txt_contact.place(x=360, y=40, width=130)

         
        calc_frame = Frame(customer_frame, bd=2, relief=RIDGE, bg="white")
        calc_frame.place(x=5, y=80, width=230, height=300)

        self.var_cal_input = StringVar()
        txt_cal_input = Entry(calc_frame, textvariable=self.var_cal_input, font=("arial", 15), width=21, bd=5, relief=GROOVE, justify=RIGHT)
        txt_cal_input.grid(row=0, column=0, columnspan=4)

        btn_texts = [
            ("7",1,0),("8",1,1),("9",1,2),("+",1,3),
            ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
            ("1",3,0),("2",3,1),("3",3,2),("*",3,3),
            ("0",4,0),("C",4,1),("=",4,2),("/",4,3),
        ]

        for (text, row, col) in btn_texts:
            Button(calc_frame, text=text, width=5, height=2, command=lambda t=text: self.get_input(t)).grid(row=row, column=col)

         
        cart_frame = Frame(customer_frame, bd=2, relief=RIDGE, bg="white")
        cart_frame.place(x=240, y=80, width=250, height=300)

        self.lbl_cart = Label(cart_frame, text="Cart \t Total Products: [0]", font=("times new roman", 12), bg="lightgray")
        self.lbl_cart.pack(side=TOP, fill=X)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "qty", "price"), show="headings")
        self.cart_table.heading("pid", text="PID")
        self.cart_table.heading("name", text="Product")
        self.cart_table.heading("qty", text="QTY")
        self.cart_table.heading("price", text="Price")

        self.cart_table.column("pid", width=30)
        self.cart_table.column("name", width=100)
        self.cart_table.column("qty", width=50)
        self.cart_table.column("price", width=60)

        self.cart_table.pack(fill=BOTH, expand=1)
        
         
        bottom_frame = Frame(customer_frame, bd=2, relief=RIDGE, bg="white")
        bottom_frame.place(x=5, y=390, width=485, height=100)

        lbl_pname = Label(bottom_frame, text="Product Name", font=("times new roman", 12), bg="white")
        lbl_pname.place(x=5, y=5)
        self.txt_pname = Entry(bottom_frame, font=("times new roman", 12), bg="lightyellow")
        self.txt_pname.place(x=5, y=30, width=130)

        lbl_price = Label(bottom_frame, text="Price Per Qty", font=("times new roman", 12), bg="white")
        lbl_price.place(x=145, y=5)
        self.txt_price = Entry(bottom_frame, font=("times new roman", 12), bg="lightyellow")
        self.txt_price.place(x=145, y=30, width=100)

        lbl_qty = Label(bottom_frame, text="Quantity", font=("times new roman", 12), bg="white")
        lbl_qty.place(x=255, y=5)
        self.txt_qty = Entry(bottom_frame, font=("times new roman", 12), bg="lightyellow")
        self.txt_qty.place(x=255, y=30, width=80)

        lbl_stock = Label(bottom_frame, text="In Stock", font=("times new roman", 12), bg="white")
        lbl_stock.place(x=340, y=5)
        self.lbl_stock_val = Label(bottom_frame, text="0", font=("times new roman", 12), bg="lightyellow")
        self.lbl_stock_val.place(x=340, y=30)

        btn_clear = Button(bottom_frame, text="Clear", font=("times new roman", 12), bg="gray", fg="white")
        btn_clear.place(x=400, y=5, width=70, height=25)

        btn_add = Button(bottom_frame, text="Add|Update Cart", font=("times new roman", 12), bg="orange", fg="white")
        btn_add.place(x=400, y=35, width=70, height=30)

         
        bill_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=830, y=50, width=500, height=500)

        title3 = Label(bill_frame, text="Customer Billing Area", font=("goudy old style", 15), bg="red", fg="white")
        title3.pack(side=TOP, fill=X)

        self.txt_bill_area = Text(bill_frame, font=("times new roman", 12), bg="lightyellow")
        self.txt_bill_area.pack(fill=BOTH, expand=1)

         
        summary_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        summary_frame.place(x=320, y=560, width=1010, height=130)

        self.lbl_amount = Label(summary_frame, text="Bill Amount\n[0]", font=("times new roman", 15), bg="blue", fg="white")
        self.lbl_amount.place(x=10, y=10, width=150, height=50)

        lbl_discount = Label(summary_frame, text="Discount\n5%", font=("times new roman", 15), bg="green", fg="white")
        lbl_discount.place(x=170, y=10, width=150, height=50)

        self.lbl_netpay = Label(summary_frame, text="Net Pay\n[0]", font=("times new roman", 15), bg="purple", fg="white")
        self.lbl_netpay.place(x=330, y=10, width=150, height=50)

        btn_print = Button(summary_frame, text="Print", font=("times new roman", 15), bg="lightblue", command=self.print_bill)
        btn_print.place(x=500, y=10, width=100, height=50)

        btn_clear_all = Button(summary_frame, text="Clear All", font=("times new roman", 15), bg="gray", fg="white")
        btn_clear_all.place(x=620, y=10, width=120, height=50)

        btn_generate = Button(summary_frame, text="Generate\nSave Bill", font=("times new roman", 15), bg="orange", fg="white")
        btn_generate.place(x=760, y=10, width=200, height=50)

    def print_bill(self):
         
        bill_content = f"""
        INVENTORY MANAGEMENT SYSTEM
        {'='*40}
        Customer Name: {self.txt_name.get()}
        Contact No.: {self.txt_contact.get()}
        {'-'*40}
        Products Purchased:
        {'-'*40}
        """
        
         
        for child in self.cart_table.get_children():
            product = self.cart_table.item(child, 'values')
            bill_content += f"{product[1]} (Qty: {product[2]}) - ${float(product[3]):.2f}\n"
        
         
        total = float(self.lbl_amount.cget('text').split('[')[1].split(']')[0])
        discount = total * 0.05
        net_pay = total - discount
        
        
        bill_content += f"""
        {'-'*40}
        Subtotal: ${total:.2f}
        Discount (5%): ${discount:.2f}
        Total Payable: ${net_pay:.2f}
        {'='*40}
        Thank you for your purchase!
        """
        
        
        self.txt_bill_area.delete(1.0, END)
        self.txt_bill_area.insert(END, bill_content)
        
         
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save Bill As"
        )
        
        if file_path:
            try:
                 
                with open(file_path, 'w') as f:
                    f.write(bill_content)
                
                 
                if os.name == 'nt':
                    os.startfile(file_path, 'print')
                    messagebox.showinfo("Success", "Bill sent to printer!")
                else:
                    messagebox.showinfo("Success", f"Bill saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save/print bill:\n{str(e)}")

    def add_to_cart(self, event):
        selected = self.product_table.focus()
        product_data = self.product_table.item(selected, 'values')
        
        if product_data:
            pid, name, price, qty, status = product_data
            self.cart_table.insert("", "end", values=(pid, name, 1, price))
            
             
            total_items = len(self.cart_table.get_children())
            self.lbl_cart.config(text=f"Cart \t Total Products: [{total_items}]")
            
             
            self.update_bill()

    def update_bill(self):
        total = 0
        for child in self.cart_table.get_children():
            product = self.cart_table.item(child, 'values')
            total += float(product[3]) * int(product[2])   
        
        discount = total * 0.05
        net_pay = total - discount
        
        self.lbl_amount.config(text=f"Bill Amount\n[{total:.2f}]")
        self.lbl_netpay.config(text=f"Net Pay\n[{net_pay:.2f}]")

    def show_products(self):
        self.product_table.delete(*self.product_table.get_children())
        for product in self.products:
            self.product_table.insert("", "end", values=(
                product["pid"],
                product["name"],
                product["price"],
                product["qty"],
                product["status"]
            ))

    def search_product(self):
        search_term = self.var_search.get().lower()
        self.product_table.delete(*self.product_table.get_children())
        
        for product in self.products:
            if search_term in product["name"].lower():
                self.product_table.insert("", "end", values=(
                    product["pid"],
                    product["name"],
                    product["price"],
                    product["qty"],
                    product["status"]
                ))
        
        if not self.product_table.get_children():
            messagebox.showinfo("Not Found", "No products matching your search")

    def get_input(self, char):
        if char == "C":
            self.var_cal_input.set("")
        elif char == "=":
            try:
                result = str(eval(self.var_cal_input.get()))
                self.var_cal_input.set(result)
            except:
                self.var_cal_input.set("Error")
        else:
            self.var_cal_input.set(self.var_cal_input.get() + str(char))

if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()