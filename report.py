from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import sqlite3
import pandas as pd

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1390x700+0+0")
        self.root.title("Inventory Management System | N7")
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="Generate Reports", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white").place(x=10, y=15, width=1370, height=50)

        # Buttons for report generation
        btn_inventory = Button(self.root, text="Inventory Report", command=self.export_inventory_report, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=50, y=100, width=300, height=50)
        btn_sales = Button(self.root, text="Sales Report", command=self.export_sales_report, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=50, y=200, width=300, height=50)
        btn_transactions = Button(self.root, text="Transaction Report", command=self.export_transaction_report, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=50, y=300, width=300, height=50)

    def connect_db(self):
        return sqlite3.connect(database=r'ims.db')

    def export_inventory_report(self):
        con = self.connect_db()
        df = pd.read_sql_query("SELECT * FROM product", con)
        con.close()
        self.save_report(df, "Inventory_Report")

    def export_sales_report(self):
        con = self.connect_db()
        query = """
        SELECT product.name, product.price, product_transaction.qty, product_transaction.date
        FROM product_transaction
        JOIN product ON product_transaction.product_id = product.pid
        WHERE product_transaction.type = 'outbound'
        """
        df = pd.read_sql_query(query, con)
        con.close()
        self.save_report(df, "Sales_Report")

    def export_transaction_report(self):
        con = self.connect_db()
        query = """
        SELECT product.name, product_transaction.type, product_transaction.qty, product_transaction.date
        FROM product_transaction
        JOIN product ON product_transaction.product_id = product.pid
        """
        df = pd.read_sql_query(query, con)
        con.close()
        self.save_report(df, "Transaction_Report")

    def save_report(self, df, report_name):
        filetypes = [('CSV files', '*.csv'), ('Excel files', '*.xlsx')]
        file = asksaveasfilename(defaultextension=".csv", filetypes=filetypes, title="Save Report As")
        if file:
            if file.endswith('.csv'):
                df.to_csv(file, index=False)
            elif file.endswith('.xlsx'):
                df.to_excel(file, index=False, engine='openpyxl')
            messagebox.showinfo("Success", f"{report_name} has been saved successfully!")

if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
