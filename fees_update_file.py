import tkinter.messagebox
import random
#import College_Std_info_BackEnd
import tkinter as tk
import fees
import pickle
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
#from babel.numbers import *
from tkcalendar import Calendar, DateEntry
from personal_info import Student, Fees
from staff_class import Staff
import main1
import sys

def callback(window, college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)

def searchStudent(college, Text_Entry_search, Text_Entry_total_fee, Text_Entry_semester,Text_Entry_paid ,  Text_Entry_paid_date , Text_Entry_mode_of_payment ,  Text_Entry_due_amount):
    selectedStudent = college.findStudent(Text_Entry_search.get())
    selectedFees = selectedStudent.findFees(Text_Entry_semester.get())
    if selectedFees:
       Text_Entry_total_fee.insert( END,str(selectedFees.get_total_fee()))
       #Text_Entry_semester.insert(END, str(selectedStudent.get_semester()))
       Text_Entry_paid.insert( END,str(selectedFees.get_paid()))
       Text_Entry_paid_date.delete(0, END)
       Text_Entry_paid_date.insert( END,str(selectedFees.get_paid_date()))
       Text_Entry_mode_of_payment.insert( END,str(selectedFees.get_mode_of_payment()))
       Text_Entry_due_amount.insert( END,str(selectedFees.get_due_amount()))
    else:
        messagebox.showinfo("info", 'Student doesnt exist')
def delete (college ,Text_Entry_search , Text_Entry_total_fee, Text_Entry_semester,Text_Entry_paid ,  Text_Entry_paid_date , Text_Entry_mode_of_payment ,  Text_Entry_due_amount):
    selectedStudent = college.findStudent((Text_Entry_search.get()))
    if selectedStudent:
        college.remove_student(selectedStudent)
        college.write_student_file()
        messagebox.showinfo("info", 'Student has been deleted')
        fees.clear(Text_Entry_total_fee, Text_Entry_semester,Text_Entry_paid ,  Text_Entry_paid_date , Text_Entry_mode_of_payment ,  Text_Entry_due_amount)
    else:
        messagebox.showinfo("info", 'Student doesnt exist')

def update(college ,Text_Entry_search , Text_Entry_total_fee, Text_Entry_semester,Text_Entry_paid ,  Text_Entry_paid_date , Text_Entry_mode_of_payment ,  Text_Entry_due_amount):
    selectedStudent = college.findStudent((Text_Entry_search.get()))
    selectedFees = selectedStudent.findFees(Text_Entry_semester.get())
    selectedFees.set_total_fee(Text_Entry_total_fee.get())
    selectedFees.set_semester( Text_Entry_semester.get())
    selectedFees.set_paid(Text_Entry_paid.get())
    selectedFees.set_paid_date(Text_Entry_paid_date.get())
    selectedFees.set_mode_of_payment(Text_Entry_mode_of_payment.get())
    selectedFees.set_due_amount(Text_Entry_due_amount.get())
    college.write_student_file()
    messagebox.showinfo("info", 'Information has been updated')
def gui(college):
    #loadStudentFile()
    window = tk.Tk()
    window.title('Student Fees')
    window.geometry('1350x750')
    window.config(bg='gray')
    college.read_student_file()


    lbl_search = tk.Label(window, text='Search by Name', font=('arial', 20))
    lbl_search.grid(row=0, column=0, sticky='W', padx=20, pady=10)
    lbl_total_fee = tk.Label(window, text='Total Fees', font=('arial', 20))
    lbl_total_fee.grid(row=1, column=0, sticky='W', padx=20)
    lbl_semester = tk.Label(window, text='Semester', font=('arial', 20))
    lbl_semester.grid(row=2, column=0, sticky='W', padx=20)
    lbl_paid = tk.Label(window, text='Paid', font=('arial', 20))
    lbl_paid.grid(row=3, column=0, sticky='W', padx=20)
    lbl_paid_date = tk.Label(window, text='Paid date', font=('arial', 20))
    lbl_paid_date.grid(row=4, column=0, sticky='W', padx=20)
    lbl_mode_of_payment = tk.Label(window, text='Mode of Payment', font=('arial', 20))
    lbl_mode_of_payment.grid(row=5, column=0, sticky='W', padx=20)
    lbl_due_amount = tk.Label(window, text='Due Amount', font=('arial', 20))
    lbl_due_amount.grid(row=6, column=0, sticky='W', padx=20)


    Text_Entry_search = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_search.grid(row=0, column=1, padx=10, pady=5)



    Text_Entry_total_fee = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_total_fee.grid(row=1, column=1, padx=10, pady=5)
    Text_Entry_semester = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_semester.grid(row=2, column=1, padx=10, pady=5)
    Text_Entry_paid = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_paid.grid(row=3, column=1, padx=10, pady=5)
    Text_Entry_paid_date =  DateEntry(window ,width=42,bg="darkblue",fg="white",year=2010)  # , textvariable=father_name)
    Text_Entry_paid_date.grid(row=4, column=1, padx=10, pady=5)
    Text_Entry_mode_of_payment = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_mode_of_payment.grid(row=5, column=1, padx=10, pady=5)
    Text_Entry_due_amount = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_due_amount.grid(row=6, column=1, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.grid(row=7, column=3, padx=10, pady=5)

    update_info = tk.Button(window, text="Update",command=lambda: update(college,Text_Entry_search, Text_Entry_total_fee, Text_Entry_semester,Text_Entry_paid ,  Text_Entry_paid_date , Text_Entry_mode_of_payment ,  Text_Entry_due_amount))
    update_info.grid(row=7, column=2, padx=10, pady=5)

    delete_info = tk.Button(window, text="Delete",command=lambda: delete(college, Text_Entry_total_fee, Text_Entry_semester,Text_Entry_paid ,  Text_Entry_paid_date , Text_Entry_mode_of_payment ,  Text_Entry_due_amount))
    delete_info.grid(row=7, column=1, padx=10, pady=5)

    search_button = tk.Button(window, text="Search",command=lambda: searchStudent(college ,Text_Entry_search , Text_Entry_total_fee, Text_Entry_semester ,Text_Entry_paid ,  Text_Entry_paid_date , Text_Entry_mode_of_payment ,  Text_Entry_due_amount ))
    search_button.grid(row=0, column=2, padx=10, pady=5)