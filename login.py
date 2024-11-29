from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Developed By Group EAUT 7")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        
        #====image=====
        try:
            self.phone_image = ImageTk.PhotoImage(file="images/phone.png")  # Ensure the image path is correct
            self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=200, y=50)
        except Exception as e:
            messagebox.showerror("Error", f"Image not found: {str(e)}")
        
        #===Login_Frame====
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)
        
        title = Label(login_frame, text="Đăng nhập", font=("Elephant", 30, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        lbl_user = Label(login_frame, text="Mã nhân viên", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=100)
        self.txt_user = Entry(login_frame, font=("times new roman", 15), bg="#ECECEC")
        self.txt_user.place(x=50, y=140, width=250)

        lbl_pass = Label(login_frame, text="Mật khẩu", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=200)
        self.txt_pass = Entry(login_frame, font=("times new roman", 15), bg="#ECECEC", show="*")
        self.txt_pass.place(x=50, y=240, width=250)

        btn_login = Button(login_frame, text="Đăng nhập", command=self.login, font=("Arial Rounded MT Bold", 15), bg="#00B0F0", fg="white", cursor="hand2").place(x=50, y=300, width=250, height=35)

    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.txt_user.get() == "" or self.txt_pass.get() == "":
                messagebox.showerror('Error', "All fields are required", parent=self.root)
            else:
                print(f"Username: {self.txt_user.get()}, Password: {self.txt_pass.get()}")  # Debugging line
                cur.execute("SELECT * FROM employee WHERE eid=? AND pass=?", (self.txt_user.get(), self.txt_pass.get()))
                user = cur.fetchone()
                print(f"Database response: {user}")  # Debugging line
                if user is None:
                    messagebox.showerror('Error', 'Invalid Username/Password', parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to: {str(ex)}', parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
