from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | N7")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_desc = StringVar()
        
        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Supplier", font=("goudy old style", 13, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # Options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Invoice", "Name", "Contact"), state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 13), bg="light yellow")
        txt_search.place(x=200, y=10)
        
        btn_search = Button(SearchFrame, text="Search", font=("goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=410, y=9, width=150, height=30)
        
        # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1000)

        # Content
        # Row 1
        lbl_invoice = Label(self.root, text="Invoice", font=("goudy old style", 15), bg="white")
        lbl_invoice.place(x=50, y=150)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style", 15), bg="light yellow")
        txt_invoice.place(x=150, y=150, width=180)
        
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=400, y=150)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="light yellow")
        txt_name.place(x=500, y=150, width=180)
        
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=750, y=150)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="light yellow")
        txt_contact.place(x=850, y=150, width=180)

        # Row 2
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white")
        lbl_desc.place(x=50, y=200)
        txt_desc = Entry(self.root, textvariable=self.var_desc, font=("goudy old style", 15), bg="light yellow")
        txt_desc.place(x=150, y=200, width=880)

        # Buttons
        btn_add = Button(self.root, text="Add", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_add.place(x=500, y=250, width=110, height=28)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=620, y=250, width=110, height=28)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=740, y=250, width=110, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=860, y=250, width=110, height=28)

        # Supplier Details Table
        sup_frame = Frame(self.root, bd=3, relief=RIDGE)
        sup_frame.place(x=0, y=300, relwidth=1, height=200)
        
        scrolly = Scrollbar(sup_frame, orient=VERTICAL)
        scrollx = Scrollbar(sup_frame, orient=HORIZONTAL)
        
        self.SupplierTable = ttk.Treeview(sup_frame, columns=("invoice", "name", "contact", "desc"), 
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading("invoice", text="Invoice")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Description")
        
        self.SupplierTable["show"] = "headings"
        
        self.SupplierTable.column("invoice", width=90)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("desc", width=100)
        
        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()
        
    # Add supplier to the database
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Invoice already exists, try a different one", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) VALUES (?, ?, ?, ?)", (
                        self.var_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_desc.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Show suppliers in the table
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Get data from table to entry fields
    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = self.SupplierTable.item(f)
        row = content['values']
        self.var_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_desc.set(row[3])
    
    # Update supplier data
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_desc.get(),
                        self.var_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Delete supplier from database
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice", parent=self.root)
                else:
                    if messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root):
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Clear entry fields
    def clear(self):
        self.var_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_desc.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
    
    # Search supplier by invoice, name, or contact
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute(f"SELECT * FROM supplier WHERE {self.var_searchby.get().lower()} LIKE ?", ('%' + self.var_searchtxt.get() + '%',))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
