'''IMporting'''
from tkinter import *
from tkinter import ttk
import  tkinter.messagebox
from Windows_Version import *
from tkinter import messagebox

class Authentication:
    user = 'admin'
    passw = 'admin'

    def __init__(self,root):

        self.root = root
        self.root.iconbitmap("its_icon.ico")
        self.root.geometry('1200x660+160+80')
        self.root.title('  Admin-Authetication ')
        self.root.resizable(0, 0)

        '''Make Window 10X10'''

        rows = 0
        while rows<10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows+=1

        '''Username and Password'''

        frame = LabelFrame(self.root, text='Login')
        frame.grid(row = 1,column = 1,columnspan=9,rowspan=9)

        Label(frame, text = ' Username ').grid(row = 2, column = 0, sticky = W, padx=10, pady = 5)
        Label(frame, text = '   ').grid(row = 2, column = 1, sticky = W)
        self.username = Entry(frame)
        self.username.grid(row = 2,column = 2 , padx=10)

        Label(frame, text = ' Password ').grid(row = 5, column = 0, sticky = W , padx=10)
        Label(frame, text = '    ').grid(row = 5, column = 1, sticky = W, pady = 5)
        self.password = Entry(frame, show='*')
        self.password.grid(row = 5, column = 2 , padx=10)

        ''''Login Button'''
        ttk.Button(frame, text = 'LOGIN',command = self.login_user).grid(row=7,column=2 , pady = 10)

        '''Message Display'''
        self.message = Label(text = '',fg = 'Red')
        self.message.grid(row=9,column=5)


    def login_user(self):

        '''Check username and password entered are correct'''
        if self.username.get() == self.user and self.password.get() == self.passw:

            # Do the work done by the main of Windows_Version.py

            #Destroy current window
            root.destroy()

            #Open new window
            create_database()
            newroot = Tk()
            newroot.title("Inventory Tracking System")
            newroot.iconbitmap("its_icon.ico")

            ob = Inventory(newroot)
            newroot.mainloop()

        else:

            '''Prompt user that either id or password is wrong'''
            self.message['text'] = 'Username or Password incorrect. Try again!'

if __name__ == '__main__':

    root = Tk()
    application = Authentication(root)
    root.mainloop()
