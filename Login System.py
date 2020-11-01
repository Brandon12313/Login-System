from tkinter import *
import os
import time

root = Tk()


def session():
    screen4 = Toplevel(screen)
    screen4.after(1000, screen1.destroy())
def login_user():
    Label(screen1, text='').pack()
    Label(screen1, text='Logging in',height='2', width='750', bg='green', font=('Calibri', 15)).pack()
    session()


def attempt_login():
    username5 = username_verify.get()
    password5 = password_verify.get()

    username_verify.delete(0, END)
    password_verify.delete(0, END)

    list_of_files = os.listdir()
    if username5 in list_of_files:
        file1 = open(username5, 'r')
        verify = file1.read().splitlines()
        if password5 in verify:
            login_user()
        else:
            Label(screen1, text='').pack()
            Label(screen1, text='Password not recognized', height='2', width='750', bg='red', font=('Calibri', 15)).pack()
    else:
        Label(screen1, text='').pack()
        Label(screen1, text='User not found', height='2', width='750', bg='red', font=('Calibri', 15)).pack()


def login():

    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry('750x500')
    screen1.title('Login')

    global password_verify
    global username_verify

    password_verify = StringVar()
    username_verify = StringVar()

    Label(screen1, text='Login', height='2', width='750', bg='grey', font=('Calibri', 20)).pack()
    Label(screen1, text='Please enter Username and Password', height='2', width='750', bg='grey', font=('Calibri', 20)).pack()
    Label(screen1, text='').pack()
    Label(screen1, text='Username', font=('Calibri', 20)).pack()
    username_verify = Entry(screen1, textvariable='username_verify', font=('Calibri', 20))
    username_verify.pack()
    Label(screen1, text='').pack()
    Label(screen1, text='Password', font=('Calibri', 20)).pack()
    password_verify = Entry(screen1, textvariable='password_verify', font=('Calibri', 20))
    password_verify.pack()
    Label(screen1, text='').pack()
    Button(screen1, text='Login', height='1', width='28', font=('Calibri'), command=attempt_login).pack()


def register():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry('750x500')
    screen2.title('Register')

    global username_entry
    global password_entry
    global password_confirm

    username_entry = StringVar()
    password_entry = StringVar()
    password_confirm = StringVar()

    Label(screen2, text= 'Register', height='2', width='750', bg='grey', font=('Calibri', 15)).pack()
    Label(screen2, text='Please enter Username and Password', height='2', width='750', bg='grey', font=('Calibri', 15)).pack()
    Label(screen2, text='').pack()
    Label(screen2, text='Username', font=('Calibri', 15)).pack()
    username_entry = Entry(screen2, textvariable='username_entry', font=('Calibri', 15))
    username_entry.pack()
    Label(screen2, text='').pack()
    Label(screen2, text='Password', font=('Calibri', 15)).pack()
    password_entry = Entry(screen2, textvariable='password_entry', font=('Calibri', 15))
    password_entry.pack()
    Label(screen2, text='').pack()
    Label(screen2, text='Please confirm Password', font=('Calibri', 15)).pack()
    password_confirm = Entry(screen2, textvariable='password_confirm', font=('Calibri', 15))
    password_confirm.pack()
    Label(screen2, text='').pack()
    Button(screen2, text='Register', height='1', width='28', font='Calibri', command=attempt_register).pack()


def attempt_register():
    password = password_entry.get()
    pass_confirm = password_confirm.get()
    username = username_entry.get()

    if password != pass_confirm:
        Label(screen2, text='').pack()
        Label(screen2, text='Passwords do not match', bg='red', height='2', width='28', font='Calibri').pack()
    elif username == account_data_verify:
        Label(screen2, text='').pack()
        Label(screen2, text='Username taken', bg='red', height='2', width='28', font='Calibri').pack()
    elif password == pass_confirm and username != account_data_verify:
        Label(screen2, text='').pack()
        Label(screen2, text='Registration Successful', bg='green', height='2', width='28', font='Calibri').pack()
        register_user()


def register_user():
    password1 = password_entry.get()
    username1 = username_entry.get()
    pass_confirm1 = password_confirm.get()
    file = open(username1,'w')
    file.write(username1+'\n')
    file.write(password1+'\n')
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    password_confirm.delete(0, END)
    screen2.after(1500, screen2.destroy)


def account_data_verify():
    account_data_list = open('account_data.txt').readlines()
    account_data_check = list(account_data_list)


def screen():
    global screen
    screen = root
    screen.geometry('750x500')
    screen.title('Welcome')
    Label(text='Welcome', height='2', width='750', bg='grey', font=('Calibri',20)).pack()
    Label(text='').pack()
    Button(text='Login', height='1', width='28', font=('Calibri'), command=login).pack()
    Label(text='').pack()
    Button(text='Register', height='1', width='28', font=('Calibri'), command=register).pack()

    root.mainloop()

screen()



