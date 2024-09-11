from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk, Frame, Label, Entry, Button
import re
import sqlite3
import tkinter
import tkinter as tk
import time
from datetime import datetime, date
from PIL import Image, ImageTk, ImageWin

window = Tk()

window.title("Flight Management System")
window.geometry('550x450')
window.configure(bg='#cedef0')


# create new window

def new():  # new window definition
    newwin = Toplevel(window)
    newwin.geometry('650x300')
    newwin.configure(bg='#cedef0')

    def run_query3(query9):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            query_result3 = cursor.execute(query9, (txt15.get(),))
            conn.commit()
        return query_result3

    def viewing_records1():

        records1 = tree1.get_children()
        for element in records1:
            tree1.delete(element)
        query9 = 'SELECT * FROM passenger WHERE id = ?'
        db_rows = run_query3(query9)
        for row in db_rows:
            tree1.insert('', 0, text=row[0], values=(row[1], row[2], row[3],
                                                     row[4], row[5], row[6]))

    # treeview_pass
    tree1 = ttk.Treeview(newwin, height=10, column=6)
    tree1["column"] = ('#0', '#1', '#2', '#3', '#4', '#5')
    tree1.grid(row=0, column=0, columnspan=6, padx=14, pady=15)

    tree1.heading('#0', text='ID')
    tree1.column('#0', anchor='center', width=70)
    tree1.heading('#1', text='Name')
    tree1.column('#1', anchor='center', width=110)
    tree1.heading('#2', text='Age')
    tree1.column('#2', anchor='center', width=60)
    tree1.heading('#3', text='Gender')
    tree1.column('#3', anchor='center', width=80)
    tree1.heading('#4', text='Address')
    tree1.column('#4', anchor='center', width=80)
    tree1.heading('#5', text='Number')
    tree1.column('#5', anchor='center', width=80)
    tree1.heading('#6', text='Email')
    tree1.column('#6', anchor='center', width=130)

    viewing_records1()


tab_control = ttk.Notebook(window)

right = ttk.Frame(tab_control)
left = ttk.Frame(tab_control)
three = ttk.Frame(tab_control)
four = ttk.Frame(tab_control)

right1 = Frame(three, width=500, height=500, bg='#cedef0')
right1.pack(side=RIGHT)

left1 = Frame(three, width=500, height=500, bg='#cedef0')
left1.pack(side=LEFT)

right = Frame(tab_control, bg='#cedef0')
left = Frame(tab_control, bg='#cedef0')
three = Frame(tab_control, bg='#cedef0')
four = Frame(tab_control, bg='#cedef0')

tab_control.add(right, text='Passenger Info')
tab_control.add(left, text='Flight Info')
tab_control.add(three, text='Flight Booking ')
tab_control.add(four, text='Boarding Pass')

tab_control.pack(expand=1, fill="both")

# databse name
db_name = 'airline.db'


# Tab1
# database query
def run_query(query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        query_result = cursor.execute(query, parameters)
        conn.commit()
    return query_result


# ComboBox for Gender
gender_options = ["Male", "Female"]


def validate_id(id):
    return id.isdigit() and len(id) == 10


def validate_name(name):
    pattern = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
    return re.match(pattern, name)


def validate_age(age):
    return age.isdigit() and 1 <= int(age) <= 100


def validate_number(number):
    return number.isdigit() and len(number) >= 10


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)


def validation():
    if not validate_id(txt1.get()):
        messagebox.showerror("Invalid Input", "ID must be 10 digits!")
        return False
    if not validate_name(txt2.get()):
        messagebox.showerror("Invalid Input", "Name should be properly entered!")
        return False
    if not validate_age(txt3.get()):
        messagebox.showerror("Invalid Input", "Age must be between 1 and 100!")
        return False
    if combo_gender.get() not in gender_options:
        messagebox.showerror("Invalid Input", "Please select a valid gender!")
        return False
    if not txt5.get():
        messagebox.showerror("Invalid Input", "Address is required!")
        return False
    if not validate_number(txt6.get()):
        messagebox.showerror("Invalid Input", "Number must be at least 10 digits!")
        return False
    if not validate_email(txt7.get()):
        messagebox.showerror("Invalid Input", "Invalid email format!")
        return False
    return True


def adding():
    if validation():
        query = 'INSERT INTO passenger VALUES (?, ?, ?, ?, ?, ?, ?)'
        parameters = (txt1.get(), txt2.get(), txt3.get(),
                      combo_gender.get(), txt5.get(), txt6.get(), txt7.get())
        run_query(query, parameters)
        messagebox.showinfo('Success', 'Data Added Successfully!')
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        combo_gender.set("")
        txt5.delete(0, END)
        txt6.delete(0, END)
        txt7.delete(0, END)


# Layout
lbl1 = Label(right, text='ID', bg='#f0ced9')
lbl1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
txt1 = Entry(right, width=25)
txt1.grid(row=0, column=1, padx=10, pady=10, sticky=W)

lbl2 = Label(right, text='Name', bg='#f0ced9')
lbl2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
txt2 = Entry(right, width=25)
txt2.grid(row=1, column=1, padx=10, pady=10, sticky=W)

lbl3 = Label(right, text='Age', bg='#f0ced9')
lbl3.grid(row=2, column=0, padx=10, pady=10, sticky=W)
txt3 = Entry(right, width=11)
txt3.grid(row=2, column=1, padx=10, pady=10, sticky=W)

lbl4 = Label(right, text='Gender', bg='#f0ced9')
lbl4.grid(row=3, column=0, padx=10, pady=10, sticky=W)
combo_gender = ttk.Combobox(right, values=gender_options, width=10)
combo_gender.grid(row=3, column=1, padx=10, pady=10, sticky=W)

lbl5 = Label(right, text='Address', bg='#f0ced9')
lbl5.grid(row=4, column=0, padx=10, pady=10, sticky=W)
txt5 = Entry(right, width=25)
txt5.grid(row=4, column=1, padx=10, pady=10, sticky=W)

lbl6 = Label(right, text='Number', bg='#f0ced9')
lbl6.grid(row=5, column=0, padx=10, pady=10, sticky=W)
txt6 = Entry(right, width=25)
txt6.grid(row=5, column=1, padx=10, pady=10, sticky=W)

lbl7 = Label(right, text='Email', bg='#f0ced9')
lbl7.grid(row=6, column=0, padx=10, pady=10, sticky=W)
txt7 = Entry(right, width=25)
txt7.grid(row=6, column=1, padx=10, pady=10, sticky=W)

# Add Data Button
btn1 = Button(right, text="Add Data", command=adding)
btn1.grid(row=7, column=1, padx=10, pady=10, sticky=W)


# Tab2

# Validation functions
def flight_number_validator(flight):
    """Validates flight number (3 letters followed by 3 digits)"""
    pattern = r"^[A-Za-z]{3}[0-9]{3}$"
    return bool(re.match(pattern, flight))


def name_validator(name):
    """Validates name fields (only letters and spaces, length between 2 and 30)"""
    if isinstance(name, str) and bool(re.match(r"^[a-zA-Z\s]{2,30}$", name)):
        return True
    else:
        return False


def date_validator(_date):
    """Validates date format and converts strings to date object"""
    if isinstance(_date, date):
        return True
    elif isinstance(_date, str):
        _date = _date.replace("/", "-").replace(".", "-").replace("_", "-")
        try:
            datetime.strptime(_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    return False


def time_validator(_time):
    """Validates time in HH:MM format (24-hour clock)"""
    pattern = r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
    return bool(re.match(pattern, _time))


# Database query function
def run_query1(query1, parameters1=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        query_result1 = cursor.execute(query1, parameters1)
        conn.commit()
    return query_result1


# Messagebox for success or error
def show_success():
    messagebox.showinfo('Success', 'Data Added Successfully!')


def show_error(message):
    messagebox.showerror('Error', message)


# Validation for the form fields
def validate_flight_info():
    if not flight_number_validator(txt8.get()):
        show_error('Flight number must be 3 letters followed by 3 digits (e.g., ABC123).')
        return False
    if not name_validator(txt9.get()):
        show_error('Invalid "From" location. Must contain only letters and spaces.')
        return False
    if not name_validator(txt10.get()):
        show_error('Invalid "To" location. Must contain only letters and spaces.')
        return False
    if not date_validator(txt11.get()):
        show_error('Invalid Departure Date. Format: YYYY-MM-DD.')
        return False
    if not time_validator(txt12.get()):
        show_error('Invalid Departure Time. Format: HH:MM.')
        return False
    if not date_validator(txt13.get()):
        show_error('Invalid Arrival Date. Format: YYYY-MM-DD.')
        return False
    if not time_validator(txt14.get()):
        show_error('Invalid Arrival Time. Format: HH:MM.')
        return False
    return True


# Database
def adding1():
    if validate_flight_info():
        query1 = 'INSERT INTO flight VALUES (?, ?, ?, ?, ?, ?, ?)'
        parameters1 = (txt8.get(), txt9.get(), txt10.get(),
                       txt11.get(), txt12.get(), txt13.get(), txt14.get())
        run_query1(query1, parameters1)
        show_success()
        # Clearing the form fields after successful addition
        txt8.delete(0, END)
        txt9.delete(0, END)
        txt10.delete(0, END)
        txt11.delete(0, END)
        txt12.delete(0, END)
        txt13.delete(0, END)
        txt14.delete(0, END)


# layout
lbl8 = Label(left, text='Flight Number', bg='#f0ced9')
lbl8.grid(row=0, column=0, padx=10, pady=10, sticky=W)
txt8 = Entry(left, width=25)
txt8.grid(row=0, column=1, padx=10, pady=10, sticky=W)

lbl9 = Label(left, text='From', bg='#f0ced9')
lbl9.grid(row=1, column=0, padx=10, pady=10, sticky=W)
txt9 = Entry(left, width=25)
txt9.grid(row=1, column=1, padx=10, pady=10, sticky=W)

lbl10 = Label(left, text='To', bg='#f0ced9')
lbl10.grid(row=2, column=0, padx=10, pady=10, sticky=W)
txt10 = Entry(left, width=25)
txt10.grid(row=2, column=1, padx=10, pady=10, sticky=W)

lbl11 = Label(left, text='Dep. Date ', bg='#f0ced9')
lbl11.grid(row=3, column=0, padx=10, pady=10, sticky=W)
txt11 = Entry(left, width=25)
txt11.grid(row=3, column=1, padx=10, pady=10, sticky=W)

lbl12 = Label(left, text='Dep. Time', bg='#f0ced9')
lbl12.grid(row=4, column=0, padx=10, pady=10, sticky=W)
txt12 = Entry(left, width=25)
txt12.grid(row=4, column=1, padx=10, pady=10, sticky=W)

lbl13 = Label(left, text='Arr. Date', bg='#f0ced9')
lbl13.grid(row=5, column=0, padx=10, pady=10, sticky=W)
txt13 = Entry(left, width=25)
txt13.grid(row=5, column=1, padx=10, pady=10, sticky=W)

lbl14 = Label(left, text='Arr. Time', bg='#f0ced9')
lbl14.grid(row=6, column=0, padx=10, pady=10, sticky=W)
txt14 = Entry(left, width=25)
txt14.grid(row=6, column=1, padx=10, pady=10, sticky=W)

# Add Data Button
btn2 = Button(left, text="Add Data", command=adding1, bg='#cceeff')
btn2.grid(row=7, column=1, padx=10, pady=10, sticky=W)


# Tab3

# viewing records from database
def viewing_records():
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    query = 'SELECT * FROM flight ORDER by flight_no DESC'
    db_rows = run_query(query)
    for row in db_rows:
        tree.insert('', 0, text=row[0], values=(row[1], row[2], row[3],
                                                row[4], row[5], row[6]))


# messagebox for booking
def clk_book():
    messagebox.showinfo('Success', 'Ticket Booked Successfully !')


# database query

def run_query2(query2, parameters2=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        query_result2 = cursor.execute(query2, parameters2)
        conn.commit()
        clk_book()
    return query_result2


# ticket booking
def adding2():
    data = tree.item(tree.selection())['text']
    print(data)

    query2 = 'INSERT INTO booking (pid, name, age, sex, addr, number, email, flight_no, frm, too, dep_date, dep_time, arr_date, arr_time) SELECT passenger.* , flight.* FROM passenger, flight WHERE pid = ? AND flight_no = ?'
    parameters2 = (txt15.get(), data)

    run_query2(query2, parameters2)

    txt15.delete(0, END)

    viewing_records()


# treeview_flight
tree = ttk.Treeview(right1, height=10, column=6)
tree["column"] = ('#0', '#1', '#2', '#3', '#4', '#5')
tree.grid(row=0, column=0, columnspan=6, padx=14, pady=15)

tree.heading('#0', text='Flight Number')
tree.column('#0', anchor='center', width=100)
tree.heading('#1', text='From')
tree.column('#1', anchor='center', width=80)
tree.heading('#2', text='To')
tree.column('#2', anchor='center', width=80)
tree.heading('#3', text='Dep. Date')
tree.column('#3', anchor='center', width=100)
tree.heading('#4', text='Dep. Time')
tree.column('#4', anchor='center', width=100)
tree.heading('#5', text='Arr. Date')
tree.column('#5', anchor='center', width=100)
tree.heading('#6', text='Arr. Time')
tree.column('#6', anchor='center', width=100)

# Labels
lbl15 = Label(three, text='Enter Passenger ID:', bg='#f0ced9')
lbl15.grid(row=0, column=0, padx=10, pady=10, sticky=W)
txt15 = Entry(three, width=20)
txt15.grid(row=0, column=1, padx=10, pady=10, sticky=W)

# Buttons
btn5 = Button(three, text="Get Info", command=new, bg='#cceeff')  # Get Info button placed above
btn5.grid(row=1, column=1, padx=10, pady=10, sticky=W)

btn4 = Button(three, text="Book Ticket", command=adding2, bg='#cceeff')  # Book Ticket button below
btn4.grid(row=2, column=1, padx=10, pady=10, sticky=W)

viewing_records()

# Tab4

# create new window
img = PhotoImage(file='/Users/nastaran/PycharmProjects/MFTProjectAirline/logo.png')
def new1():  # new window definition
    newwin1 = Toplevel(window)
    newwin1.geometry('570x230')

    one = Frame(newwin1, bg='#ED1B24', width=60, height=450)
    one.pack(side=LEFT)

    two = Frame(newwin1, bg='#1B1464', width=700, height=40)
    two.pack(side=TOP)

    def run_query4(query7, value):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            query_result7 = cursor.execute(query7, (value,))
            conn.commit()
            result = cursor.fetchall()
        return result

    # ticket viewing
    def ticket():
        query7 = 'SELECT name, flight_no, frm, too, dep_date, dep_time FROM booking WHERE pid = ?'
        value = (txt36.get())
        result = run_query4(query7, value)

        for row in result:
            lbl18.config(text=row[0])
            lbl20.config(text=row[2])
            lbl22.config(text=row[3])
            lbl24.config(text=row[1])
            lbl26.config(text=row[4])
            lbl28.config(text=row[5])

    # Labels

    lbl16 = Label(two, text='Boarding Pass', font=(' ', 13), fg='#fff', bg='#1B1464')
    lbl16.place(x=305, y=6, anchor=NE)

    lbl17 = Label(newwin1, text='Passenger Name', font=(' ', 9))
    lbl17.place(x=210, y=45, anchor=NE)
    lbl18 = Label(newwin1, font=(' ', 13))
    lbl18.place(x=230, y=70, width=140, anchor=NE)

    lbl19 = Label(newwin1, text='From', font=(' ', 9))
    lbl19.place(x=140, y=110, anchor=NE)
    lbl20 = Label(newwin1, font=(' ', 9))
    lbl20.place(x=145, y=130, width=50, anchor=NE)

    lbl21 = Label(newwin1, text='To', font=(' ', 9))
    lbl21.place(x=125, y=160, anchor=NE)
    lbl22 = Label(newwin1, font=(' ', 9))
    lbl22.place(x=145, y=180, width=50, anchor=NE)

    lbl23 = Label(newwin1, text='Flight', font=(' ', 9))
    lbl23.place(x=290, y=110, anchor=NE)
    lbl24 = Label(newwin1, font=(' ', 13))
    lbl24.place(x=305, y=130, width=50, anchor=NE)

    lbl25 = Label(newwin1, text='Date', font=(' ', 9))
    lbl25.place(x=370, y=110, anchor=NE)
    lbl26 = Label(newwin1, font=(' ', 13))
    lbl26.place(x=430, y=130, width=100, anchor=NE)

    lbl27 = Label(newwin1, text='Time', font=(' ', 9))
    lbl27.place(x=370, y=160, anchor=NE)
    lbl28 = Label(newwin1, font=(' ', 13))
    lbl28.place(x=417, y=180, width=100, anchor=NE)

   

    pil_img = Image.open('logo.png')
    img = ImageTk.PhotoImage(pil_img)
    lbl29 = Label(one, image=img, bg='#ED1B24')
    lbl29.place(x=20, y=15)
    lbl29.image = img

# lables

lbl36 = Label(four, text='Enter ID')
lbl36.place(x=250, y=150, anchor=NE)
txt36 = Entry(four, width=11)
txt36.place(x=350, y=150, anchor=NE)

# Buttons

btn6 = Button(four, text="Get The Boarding Pass", command=new1)
btn6.place(x=340, y=200, anchor=NE)

window.mainloop()
