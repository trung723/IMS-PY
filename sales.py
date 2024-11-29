from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | N7")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_invoice = StringVar()
        
        # Title
        lbl_title = Label(self.root, text="View Customer Bills", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        lbl_title.place(x=0, y=0, relwidth=1, height=50)
        
        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white")
        lbl_invoice.place(x=50, y=100)
        
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="light yellow")
        txt_invoice.place(x=160, y=100, width=180, height=28)
        
        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")
        btn_search.place(x=360, y=100, height=28, width=120)
        
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="light gray", cursor="hand2")
        btn_clear.place(x=490, y=100, height=28, width=120)
        
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)
        
        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.Sales_List = Listbox(sales_Frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.config(command=self.Sales_List.yview)
        scrolly.pack(side=RIGHT, fill=Y)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<Double-Button-1>", self.get_data)
        
        # Bill Area
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)
        
        lbl_title2 = Label(bill_Frame, text="Customer Bills Area", font=("goudy old style", 20), bg="orange")
        lbl_title2.pack(side=TOP, fill=X)
        
        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, bg="light yellow", yscrollcommand=scrolly2.set)
        scrolly2.config(command=self.bill_area.yview)
        scrolly2.pack(side=RIGHT, fill=Y)
        self.bill_area.pack(fill=BOTH, expand=1)
        
        # Image
        self.bill_photo = Image.open("images/InventoryManagement_Hero@3x.png")
        self.bill_photo = self.bill_photo.resize((450, 300))
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image = Label(self.root, image=self.bill_photo, bd=0)
        lbl_image.place(x=700, y=110)
        
        self.show()
        
    #===========================================
    def show(self):
        self.Sales_List.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.Sales_List.insert(END, i)  
                
    def get_data(self, ev):
        self.bill_area.delete('1.0', END)
        index_ = self.Sales_List.curselection()
        if index_:
            file_name = self.Sales_List.get(index_)
            with open(f'bill/{file_name}', 'r') as fp:
                for i in fp:
                    self.bill_area.insert(END, i)
                    
    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice No. should be required", parent=self.root)
        else:
            self.bill_area.delete('1.0', END)
            file_path = f'bill/{self.var_invoice.get()}.txt'
            if os.path.exists(file_path):
                with open(file_path, 'r') as fp:
                    for i in fp:
                        self.bill_area.insert(END, i)
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                
    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)
        self.var_invoice.set("")
                 
if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
