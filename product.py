from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+220+130")
        self.root.title("Inventory Management System | N7")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # All Variables
        self.var_pid = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.var_search = StringVar()
        self.var_search_by = StringVar()  # Thêm biến chọn tiêu chí tìm kiếm
        
        # Title
        title = Label(self.root, text="Thông tin sản phẩm", font=("Arial", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)
        
        # Frames
        form_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        form_frame.place(x=10, y=60, width=450, height=530)

        search_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        search_frame.place(x=470, y=60, width=620, height=70)

        table_frame = Frame(self.root, bd=3, relief=RIDGE)
        table_frame.place(x=470, y=140, width=620, height=450)
        
        # Search
        lbl_search_by = Label(search_frame, text="Search By", font=("Arial", 15), bg="white")
        lbl_search_by.place(x=10, y=10)
        
        self.cmb_search_by = ttk.Combobox(search_frame, textvariable=self.var_search_by, values=("Name", "Category", "Supplier"), state='readonly', justify=CENTER, font=("Arial", 15))
        self.cmb_search_by.place(x=120, y=10, width=150)
        self.cmb_search_by.current(0)
        
        lbl_search = Label(search_frame, text="Search", font=("Arial", 15), bg="white")
        lbl_search.place(x=280, y=10)
        
        txt_search = Entry(search_frame, textvariable=self.var_search, font=("Arial", 15), bg="light yellow")
        txt_search.place(x=350, y=10, width=150)
        
        btn_search = Button(search_frame, text="Search", command=self.search, font=("Arial", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=510, y=10, width=100, height=28)
        
        # Form
        # Row 1
        lbl_pid = Label(form_frame, text="Product ID", font=("Arial", 15), bg="white")
        lbl_pid.place(x=10, y=10)
        txt_pid = Entry(form_frame, textvariable=self.var_pid, font=("Arial", 15), bg="light yellow", state='readonly')
        txt_pid.place(x=150, y=10, width=180)
        
        lbl_category = Label(form_frame, text="Category", font=("Arial", 15), bg="white")
        lbl_category.place(x=10, y=60)
        self.cmb_category = ttk.Combobox(form_frame, textvariable=self.var_category, font=("Arial", 15), state='readonly', justify=CENTER)
        self.cmb_category.place(x=150, y=60, width=180)
        
        lbl_supplier = Label(form_frame, text="Supplier", font=("Arial", 15), bg="white")
        lbl_supplier.place(x=10, y=110)
        self.cmb_supplier = ttk.Combobox(form_frame, textvariable=self.var_supplier, font=("Arial", 15), state='readonly', justify=CENTER)
        self.cmb_supplier.place(x=150, y=110, width=180)
        
        lbl_name = Label(form_frame, text="Name", font=("Arial", 15), bg="white")
        lbl_name.place(x=10, y=160)
        txt_name = Entry(form_frame, textvariable=self.var_name, font=("Arial", 15), bg="light yellow")
        txt_name.place(x=150, y=160, width=180)

        lbl_price = Label(form_frame, text="Price", font=("Arial", 15), bg="white")
        lbl_price.place(x=10, y=210)
        txt_price = Entry(form_frame, textvariable=self.var_price, font=("Arial", 15), bg="light yellow")
        txt_price.place(x=150, y=210, width=180)

        lbl_qty = Label(form_frame, text="Quantity", font=("Arial", 15), bg="white")
        lbl_qty.place(x=10, y=260)
        txt_qty = Entry(form_frame, textvariable=self.var_qty, font=("Arial", 15), bg="light yellow")
        txt_qty.place(x=150, y=260, width=180)

        lbl_status = Label(form_frame, text="Status", font=("Arial", 15), bg="white")
        lbl_status.place(x=10, y=310)
        cmb_status = ttk.Combobox(form_frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("Arial", 15))
        cmb_status.place(x=150, y=310, width=180)
        cmb_status.current(0)

        # Buttons
        btn_add = Button(form_frame, text="Add", command=self.add, font=("Arial", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_add.place(x=10, y=360, width=100, height=28)
        btn_update = Button(form_frame, text="Update", command=self.update, font=("Arial", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=120, y=360, width=100, height=28)
        btn_delete = Button(form_frame, text="Delete", command=self.delete, font=("Arial", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=230, y=360, width=100, height=28)
        btn_clear = Button(form_frame, text="Clear", command=self.clear, font=("Arial", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=340, y=360, width=100, height=28)

        # Product Details Table
        scrolly = Scrollbar(table_frame, orient=VERTICAL)
        scrollx = Scrollbar(table_frame, orient=HORIZONTAL)
        
        self.ProductTable = ttk.Treeview(table_frame, columns=("pid", "category", "supplier", "name", "price", "qty", "status"), 
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading("pid", text="Product ID")
        self.ProductTable.heading("category", text="Category")
        self.ProductTable.heading("supplier", text="Supplier")
        self.ProductTable.heading("name", text="Name")
        self.ProductTable.heading("price", text="Price")
        self.ProductTable.heading("qty", text="Quantity")
        self.ProductTable.heading("status", text="Status")
        
        self.ProductTable["show"] = "headings"
        
        self.ProductTable.column("pid", width=90)
        self.ProductTable.column("category", width=100)
        self.ProductTable.column("supplier", width=100)
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=100)
        self.ProductTable.column("status", width=100)
        
        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()
        self.load_categories()
        self.load_suppliers()
        
    # Add product to the database
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_category.get() == "" or self.var_supplier.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("INSERT INTO product (category, supplier, name, price, qty, status) VALUES (?, ?, ?, ?, ?, ?)", (
                    self.var_category.get(),
                    self.var_supplier.get(),
                    self.var_name.get(),
                    self.var_price.get(),
                    self.var_qty.get(),
                    self.var_status.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Show all products in the table
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Get data from table to entry fields
    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = self.ProductTable.item(f)
        row = content['values']
        self.var_pid.set(row[0])
        self.var_category.set(row[1])
        self.var_supplier.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
    
    # Update product data
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Product ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    cur.execute("UPDATE product SET category=?, supplier=?, name=?, price=?, qty=?, status=? WHERE pid=?", (
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Delete product from database
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Product ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    if messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root):
                        cur.execute("DELETE FROM product WHERE pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Product deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Clear entry fields
    def clear(self):
        self.var_pid.set("")
        self.var_category.set("")
        self.var_supplier.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_search.set("")
        self.show()
        self.load_categories()
        self.load_suppliers()
    
    # Load categories into combobox
    def load_categories(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            rows = cur.fetchall()
            if rows:
                self.cmb_category['values'] = [row[0] for row in rows]
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Load suppliers into combobox
    def load_suppliers(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM supplier")
            rows = cur.fetchall()
            if rows:
                self.cmb_supplier['values'] = [row[0] for row in rows]
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Search products by selected criteria
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            search_by = self.var_search_by.get()
            search_text = self.var_search.get()
            query = ""
            if search_by == "Name":
                query = "SELECT * FROM product WHERE name LIKE ?"
            elif search_by == "Category":
                query = "SELECT * FROM product WHERE category LIKE ?"
            elif search_by == "Supplier":
                query = "SELECT * FROM product WHERE supplier LIKE ?"
            
            cur.execute(query, ('%' + search_text + '%',))
            rows = cur.fetchall()
            if rows:
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in rows:
                    self.ProductTable.insert('', END, values=row)
            else:
                self.ProductTable.delete(*self.ProductTable.get_children())
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
