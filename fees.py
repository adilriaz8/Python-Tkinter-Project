import tkinter.messagebox
import random
#import College_Std_info_BackEnd
import tkinter as tk

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
import fees_update_file
fee_list = []

def update(window , college):
    print("Opening Update Information")
    window.destroy()
    fees_update_file.gui(college)




def check(Text_Entry_search , Text_Entry_total_fee , Text_Entry_semester , Text_Entry_paid , Text_Entry_paid_date , Text_Entry_mode_of_payment , Text_Entry_due_amount ):
    for c in Text_Entry_search.get():
        if c.isdigit() == True:
            messagebox.showinfo('Error', "No numbers in the search ")
            return False
    if Text_Entry_search.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_total_fee.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in total fee")
            return False
    if Text_Entry_total_fee.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_semester.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in the Semester")
            return False
    if Text_Entry_semester.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_paid.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in Paid")
            return False
    if Text_Entry_paid.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False

    if Text_Entry_paid_date .get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_mode_of_payment.get():
        if c.isdigit() == True:
            messagebox.showinfo('Error', "No digits in the Mode of Payment")
            return False
    if Text_Entry_mode_of_payment.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_due_amount.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in the Due Amount")
            return False
    if Text_Entry_due_amount.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")

    if Text_Entry_paid.get() > Text_Entry_total_fee.get():
        messagebox.showinfo('Error', 'Paid cannot be greater than Total Fee')

    if Text_Entry_due_amount.get() > Text_Entry_total_fee.get():
        messagebox.showinfo('Error', 'Due amount cannot be greater than Total Fee')

    if Text_Entry_paid.get() > Text_Entry_due_amount.get():
        messagebox.showinfo('Error', 'Paid cannot be greater than Due Amount')

        return False
    return True


def clear(Text_Entry_search , Text_Entry_total_fee , Text_Entry_semester , Text_Entry_paid , Text_Entry_paid_date , Text_Entry_mode_of_payment , Text_Entry_due_amount):
    Text_Entry_search.delete(0, END)
    Text_Entry_total_fee.delete(0, END)
    Text_Entry_semester.delete(0, END)
    Text_Entry_paid.delete(0,END)
    Text_Entry_paid_date.delete(0, END)
    Text_Entry_mode_of_payment.delete(0, END)
    Text_Entry_due_amount.delete(0, END)



def save(college ,Text_Entry_search , Text_Entry_total_fee , Text_Entry_semester , Text_Entry_paid , Text_Entry_paid_date , Text_Entry_mode_of_payment , Text_Entry_due_amount ):

    #global fee_list
    if check(Text_Entry_search , Text_Entry_total_fee , Text_Entry_semester , Text_Entry_paid , Text_Entry_paid_date , Text_Entry_mode_of_payment , Text_Entry_due_amount ):

        fees1 = Fees(Text_Entry_search.get() , Text_Entry_total_fee.get() , Text_Entry_semester.get() , Text_Entry_paid.get() , Text_Entry_paid_date.get() , Text_Entry_mode_of_payment.get() , Text_Entry_due_amount.get())
        studentName = Text_Entry_search.get()
        student1 = college.findStudent(studentName)
        #student1.add_fees(fees1)
        messagebox.showinfo("info", "Information is saved successfully!\n" + fees1.__str__())
        clear(Text_Entry_search , Text_Entry_total_fee , Text_Entry_semester , Text_Entry_paid , Text_Entry_paid_date , Text_Entry_mode_of_payment , Text_Entry_due_amount)


        if student1:
            student1.add_fees(fees1)
            college.write_student_file()
        else:
            print('Student not found')
    else:
        print('Error with entering information')

def callback(window, college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)

def searchStudent(college, Text_Entry_search , Text_student_info):

    print(college.get_student_list())
    selectedStudent = college.findStudent((Text_Entry_search.get()))
    if selectedStudent:
        Text_student_info.insert(INSERT, '\n' + str(selectedStudent.get_adm_no()) + '\t\t\t' + selectedStudent.get_first_name() + '\t\t\t' + selectedStudent.get_landline_no() + '\t\t' + selectedStudent.get_course())
    else:
        messagebox.showinfo("info",'Student doesnt exist')
def exit(college , window):
    window.destroy()
    college.write_staff_file()

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

    str1 = 'Sr No\t\t\tStudent Name\t\t\tPhone\t\t\tCourse'
    Text_student_info = Text(window, wrap=WORD)
    Text_student_info.grid(row = 2 , rowspan=5, column=3, padx=40, pady=40) # starts at row 2 then we rowspan it to row 7
    Text_student_info.insert(INSERT, str1)


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








    save_button = tk.Button(window, text="Save",command=lambda: save(college,Text_Entry_search , Text_Entry_total_fee , Text_Entry_semester , Text_Entry_paid , Text_Entry_paid_date , Text_Entry_mode_of_payment , Text_Entry_due_amount  ))
    save_button.grid(row=7, column=0, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.grid(row=7, column=3, padx=10, pady=5)

    exit_button = tk.Button(window, text="Exit", command=lambda: exit(college, window))
    exit_button.grid(row=7, column=1, padx=10, pady=5)

    search_button = tk.Button(window, text="Search", command=lambda: searchStudent(college, Text_Entry_search , Text_student_info))
    search_button.grid(row=0, column=2, padx=10, pady=5)

    update_button = tk.Button(window, text="Update / Delete", command=lambda: update(window, college))
    update_button.grid(row=8, column=0, padx=10, pady=5)

    window.mainloop()




if __name__ == "__main__":
    print("Code executing from same file")