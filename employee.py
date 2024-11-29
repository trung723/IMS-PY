from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | N7")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        self.var_address = StringVar()  
        
        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Tìm kiếm", font=("goudy old style", 13, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # Options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Chọn", "Email", "Tên", "Số điện thoại"), state='readonly', justify=CENTER, font=("Arial", 13))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Arial", 13), bg="light yellow")
        txt_search.place(x=200, y=10)
        
        btn_search = Button(SearchFrame, text="Tìm kiếm", font=("Arial", 13), bg="#4caf50", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=410, y=9, width=150, height=30)

        # Title
        title = Label(self.root, text="Thông tin nhân viên", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1000)

        # Content
        # Row 1
        lbl_empid = Label(self.root, text="ID", font=("Arial", 15), bg="white")
        lbl_empid.place(x=50, y=150)
        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("gArial", 15), bg="light yellow")
        txt_empid.place(x=150, y=150, width=180)
        
        lbl_gender = Label(self.root, text="Giới tính", font=("Arial", 15), bg="white")
        lbl_gender.place(x=400, y=150)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Nam", "Nữ", "Khác"), state='readonly', justify=CENTER, font=("Arial", 15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        
        lbl_contact = Label(self.root, text="SĐT", font=("Arial", 15), bg="white")
        lbl_contact.place(x=750, y=150)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Arial", 15), bg="light yellow")
        txt_contact.place(x=850, y=150, width=180)

        # Row 2
        lbl_name = Label(self.root, text="Tên", font=("Arial", 15), bg="white")
        lbl_name.place(x=50, y=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("Arial", 15), bg="light yellow")
        txt_name.place(x=150, y=200, width=180)
        
        lbl_dob = Label(self.root, text="Ngày sinh", font=("Arial", 15), bg="white")
        lbl_dob.place(x=400, y=200)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Arial", 15), bg="light yellow")
        txt_dob.place(x=500, y=200, width=180)
        
        lbl_doj = Label(self.root, text="Ngày làm", font=("Arial", 15), bg="white")
        lbl_doj.place(x=750, y=200)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("Arial", 15), bg="light yellow")
        txt_doj.place(x=850, y=200, width=180)

        # Row 3
        lbl_email = Label(self.root, text="Email", font=("Arial", 15), bg="white")
        lbl_email.place(x=50, y=250)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("Arial", 15), bg="light yellow")
        txt_email.place(x=150, y=250, width=180)
        
        lbl_pass = Label(self.root, text="Mật khẩu", font=("Arial", 15), bg="white")
        lbl_pass.place(x=400, y=250)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("Arial", 15), bg="light yellow")
        txt_pass.place(x=500, y=250, width=180)
        
        lbl_utype = Label(self.root, text="Quyền hạn", font=("Arial", 15), bg="white")
        lbl_utype.place(x=750, y=250)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state='readonly', justify=CENTER, font=("Arial", 15))
        cmb_utype.place(x=850, y=250, width=180)
        cmb_utype.current(0)

        # Row 4
        lbl_address = Label(self.root, text="Địa chỉ", font=("Arial", 15), bg="white")
        lbl_address.place(x=50, y=300)
        self.txt_address = Text(self.root, font=("Arial", 15), bg="light yellow")
        self.txt_address.place(x=150, y=300, width=300, height=60)
        
        lbl_salary = Label(self.root, text="Lương", font=("Arial", 15), bg="white")
        lbl_salary.place(x=500, y=300)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("Arial", 15), bg="light yellow")
        txt_salary.place(x=600, y=300, width=180)

        # Buttons
        btn_add = Button(self.root, text="Add", command=self.add, font=("Arial", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_add.place(x=500, y=333, width=110, height=28)
        btn_update = Button(self.root, text="Update", command=self.update, font=("Arial", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=620, y=333, width=110, height=28)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("Arial", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=740, y=333, width=110, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("Arial", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=860, y=333, width=110, height=28)

        # Employee Details Table
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=370, relwidth=1, height=180)
        
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), 
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")
        
        self.EmployeeTable["show"] = "headings"
        
        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)
        
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()
        
    # Add employee to the database
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID already exists, try a different one", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END).strip(),
                        self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    # Show employees in the table
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Get data from table to entry fields
    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])
    
    # Update employee data
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("UPDATE employee SET name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? WHERE eid=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END).strip(),
                        self.var_salary.get(),
                        self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Delete employee from the database
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Employee deleted successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # Clear all entry fields
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
    
    # Search employee data
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select a search by option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute(f"SELECT * FROM employee WHERE {self.var_searchby.get().lower()} LIKE '%{self.var_searchtxt.get()}%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
