from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass
from report import reportClass
import time
import sqlite3
from tkinter import messagebox
import os

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1390x700+0+0")
        self.root.title("Inventory Management System | N7")
        self.root.config(bg="white")
        
        # Title
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        # Bind the click event to the title
        title.bind("<Button-1>", self.billing_command)
        
        # Logout Button
        btn_logout = Button(self.root, text="Đăng xuất", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2",
                            command=self.logout)
        btn_logout.place(x=1150, y=10, height=50, width=150)
        
        # Clock
        self.lbl_clock = Label(self.root, text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()
        
        # Left Menu
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)
        
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        
        self.icon_side = PhotoImage(file="images/side.png")
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)
        
        # Menu Buttons
        btn_employee = Button(LeftMenu, text="Nhân viên", image=self.icon_side, compound=LEFT, padx=20,
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",
                              command=self.employee_command)
        btn_employee.pack(side=TOP, fill=X)
        
        btn_supplier = Button(LeftMenu, text="Nhà cung cấp", image=self.icon_side, compound=LEFT, padx=20,
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",
                              command=self.supplier_command)
        btn_supplier.pack(side=TOP, fill=X)
        
        btn_category = Button(LeftMenu, text="Danh mục", image=self.icon_side, compound=LEFT, padx=20,
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",
                              command=self.category_command)
        btn_category.pack(side=TOP, fill=X)
        
        btn_product = Button(LeftMenu, text="Sản phẩm", image=self.icon_side, compound=LEFT, padx=20,
                             font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",
                             command=self.product_command)
        btn_product.pack(side=TOP, fill=X)
        
        btn_sales = Button(LeftMenu, text="Hoá đơn", image=self.icon_side, compound=LEFT, padx=20,
                           font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",
                           command=self.sales_command)
        btn_sales.pack(side=TOP, fill=X)
        
        btn_report = Button(LeftMenu, text="Báo cáo", image=self.icon_side, compound=LEFT, padx=20,
                          font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2",
                          command=self.report_command)
        btn_report.pack(side=TOP, fill=X)

        # Content
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#33bbf9", fg="white", font=("Arial", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)
        
        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#ff5722", fg="white", font=("Arial", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)
        
        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#009688", fg="white", font=("Arial", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Products\n[ 0 ]", bd=5, relief=RIDGE,
                                 bg="#607d8b", fg="white", font=("Arial", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)
        
        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE,
                               bg="#ffc107", fg="white", font=("Arial", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # Footer
        lbl_footer = Label(self.root, text="ISM-INVENTORY MANAGER SYSTEM | N7\n Contact: 0123456789",
                           font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        
        self.update_content()
        
    #====================================================       
    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        current_date = time.strftime('%d-%m-%Y')
        self.lbl_clock.config(text=f"Welcome To Inventory Management System\t\t Date: {current_date}\t\t Time: {current_time}")
        self.root.after(1000, self.update_clock)  # update every second

    def logout(self):
        self.root.destroy()  # Close the application

    def employee_command(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier_command(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category_command(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
        
    def product_command(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)
        
    def sales_command(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def billing_command(self, event):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillClass(self.new_win)

    def report_command(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')
        
            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[{str(len(employee))}]')
            
            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(bill)}]')
           
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
