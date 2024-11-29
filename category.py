from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | N7")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # All Variables
        self.var_cid = StringVar()
        self.var_name = StringVar()
        
        # Title
        title = Label(self.root, text="Category Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        # Frame for form and buttons
        form_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        form_frame.place(x=10, y=60, width=500, height=180)

        # Category ID
        lbl_cid = Label(form_frame, text="Category ID", font=("goudy old style", 15), bg="white")
        lbl_cid.place(x=10, y=10)
        txt_cid = Entry(form_frame, textvariable=self.var_cid, font=("goudy old style", 15), bg="light yellow", state='readonly')
        txt_cid.place(x=150, y=10, width=200)

        # Category Name
        lbl_name = Label(form_frame, text="Name", font=("goudy old style", 15), bg="white")
        lbl_name.place(x=10, y=60)
        txt_name = Entry(form_frame, textvariable=self.var_name, font=("goudy old style", 15), bg="light yellow")
        txt_name.place(x=150, y=60, width=200)

        # Buttons Frame
        btn_frame = Frame(form_frame, bg="white")
        btn_frame.place(x=10, y=110, width=470, height=60)

        btn_add = Button(btn_frame, text="Add", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_add.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        btn_update = Button(btn_frame, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        btn_delete = Button(btn_frame, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        btn_clear = Button(btn_frame, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        # Category Details Table Frame
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=10, y=250, width=1080, height=230)
        
        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)
        
        self.CategoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)
        
        self.CategoryTable.heading("cid", text="Category ID")
        self.CategoryTable.heading("name", text="Name")
        
        self.CategoryTable["show"] = "headings"
        
        self.CategoryTable.column("cid", width=90)
        self.CategoryTable.column("name", width=100)
        
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()
        
    # Add category to the database
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Category already exists, try a different one", parent=self.root)
                else:
                    cur.execute("INSERT INTO category (name) VALUES (?)", (
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Show categories in the table
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Get data from table to entry fields
    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = self.CategoryTable.item(f)
        row = content['values']
        self.var_cid.set(row[0])
        self.var_name.set(row[1])
    
    # Update category data
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cid.get() == "":
                messagebox.showerror("Error", "Category ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Category ID", parent=self.root)
                else:
                    cur.execute("UPDATE category SET name=? WHERE cid=?", (
                        self.var_name.get(),
                        self.var_cid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Category updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Delete category from database
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cid.get() == "":
                messagebox.showerror("Error", "Category ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Category ID", parent=self.root)
                else:
                    if messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root):
                        cur.execute("DELETE FROM category WHERE cid=?", (self.var_cid.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Category deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Clear entry fields
    def clear(self):
        self.var_cid.set("")
        self.var_name.set("")
        self.show()

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
