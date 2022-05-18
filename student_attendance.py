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
#from student2 import Student
import main1
import sys
from personal_info import Student

def callback(window , college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)

def searchStudent(college, Text_Entry_name , Text_student_info):
    selectedStudent = college.findStudent((Text_Entry_name.get()))
    if selectedStudent:
        Text_student_info.insert(INSERT, '\n' + str(selectedStudent.get_adm_no()) + '\t\t\t' + selectedStudent.get_first_name() + '\t\t\t' + selectedStudent.get_landline_no() + '\t\t' + selectedStudent.get_course())
    else:
        messagebox.showinfo("info", 'Student doesnt exist')


def clearInformation(Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to):
    Text_Entry_name.delete(0, END)
    Text_Entry_from.delete(0, END)
    Text_Entry_ttl_no_days.delete(0, END)
    Text_Entry_type.delete(0, END)
    Text_Entry_no_days_present.delete(0, END)
    Text_Entry_no_days_absent.delete(0, END)
    Text_Entry_adm_no.delete(0, END)
    Text_Entry_to.delete(0, END)


def check(Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to):
    for c in Text_Entry_name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the Name")
            return False
    if Text_Entry_name.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")

    for c in Text_Entry_ttl_no_days.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in Total Number of Days")
            return False
    if Text_Entry_ttl_no_days.get() == '':
        messagebox.showinfo('Error', "Empty field in Total Number of Days")
    for c in Text_Entry_type.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in type")
            return False
    if Text_Entry_type.get() == '':
        messagebox.showinfo('Error', "Empty field in type")
    for c in Text_Entry_no_days_present.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in Number of days present")
            return False
    if Text_Entry_no_days_present.get() == '':
        messagebox.showinfo('Error', "Empty field in Number of days present")
    for c in Text_Entry_no_days_absent.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in Number of days absent")
            return False
    if Text_Entry_no_days_absent.get() == '':
        messagebox.showinfo('Error', "Empty field in Number of days absent")
    for c in Text_Entry_adm_no.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in admission number")
            return False
    if Text_Entry_adm_no.get() == '':
        messagebox.showinfo('Error', "Empty field in Admission Number")

    if Text_Entry_from.get() == '':
        messagebox.showinfo('Error', "Empty field in From")
    if Text_Entry_to.get() == '':
        messagebox.showinfo('Error', "Empty field in To")
def saveInformation(Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to):
    if check(Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to):
        s = Attendance(Text_Entry_name.get() , Text_Entry_from.get(), Text_Entry_ttl_no_days.get() ,  Text_Entry_type.get() , Text_Entry_no_days_present.get() , Text_Entry_no_days_absent.get() , Text_Entry_adm_no.get() , Text_Entry_to.get())
        college.write_student_file()
        messagebox.showinfo("info", "Information is saved successfully!\n" + s.__str__())
        clearInformation(Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to)





def gui(college):
    #loadStudentFile()
    window = tk.Tk()
    window.title('Student Attendance')
    window.geometry('1350x750')
    window.config(bg='gray')

    lbl_name = tk.Label(window, text='Name', font=('arial', 20))
    lbl_name.grid(row=0, column=0, sticky='W', padx=20, pady=10)
    lbl_from = tk.Label(window, text='From', font=('arial', 20))
    lbl_from.grid(row=1, column=0, sticky='W', padx=20, pady=10)
    lbl_ttl_days = tk.Label(window, text='Total number of days', font=('arial', 20))
    lbl_ttl_days.grid(row=2, column=0, sticky='W', padx=20, pady=10)
    lbl_type = tk.Label(window, text='Type', font=('arial', 20))
    lbl_type.grid(row=3, column=0, sticky='W', padx=20, pady=10)
    lbl_no_days_present = tk.Label(window, text='Number of days present', font=('arial', 20))
    lbl_no_days_present.grid(row=4, column=0, sticky='W', padx=20, pady=10)
    lbl_no_days_absent = tk.Label(window, text='Number of days absent', font=('arial', 20))
    lbl_no_days_absent.grid(row=5, column=0, sticky='W', padx=20, pady=10)

    lbl_adm_no = tk.Label(window, text='Admission Number', font=('arial', 20))
    lbl_adm_no.grid(row=0, column=3, sticky='W', padx=20, pady=10)
    lbl_to= tk.Label(window, text='Admission Number', font=('arial', 20))
    lbl_to.grid(row=1, column=2, sticky='W', padx=20, pady=10)

    str1 = 'Sr No\t\t\tStudent Name\t\t\tPhone\t\t\tCourse'
    Text_student_info = Text(window, wrap=WORD)
    Text_student_info.grid(row=2, rowspan=5, column=2, padx=40, pady=40)  # starts at row 2 then we rowspan it to row 7
    Text_student_info.insert(INSERT, str1)




    Text_Entry_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_name.grid(row=0, column=1, padx=10, pady=5)
    Text_Entry_from = DateEntry(window, width=42, bg="darkblue", fg="white", year=2010)
    Text_Entry_from.grid(row=1, column=1, padx=20, pady=10)
    Text_Entry_ttl_no_days = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_ttl_no_days.grid(row=2, column=1, padx=10, pady=5)
    Text_Entry_type = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_type.grid(row=3, column=1, padx=10, pady=5)
    Text_Entry_no_days_present = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_no_days_present.grid(row=4, column=1, padx=10, pady=5)
    Text_Entry_no_days_absent = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_no_days_absent.grid(row=5, column=1, padx=10, pady=5)

    Text_Entry_adm_no = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_adm_no.grid(row=0, column=4, padx=10, pady=5)
    Text_Entry_to =  DateEntry(window, width=42, bg="darkblue", fg="white", year=2010)
    Text_Entry_to.grid(row=1, column=3, sticky='W', padx=20, pady=10)






    saveButton = tk.Button(window, text="Save Information",command=lambda: saveInformation(college, Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to ))
    saveButton.grid(row=7, column=0, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.grid(row=7, column=1, padx=10, pady=5)

    update_button = tk.Button(window, text="Update",command=lambda: update(Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to))
    update_button.grid(row=7, column=2, padx=10, pady=5)

    clearButton = tk.Button(window, text="Clear",command=lambda: clearInformation(Text_Entry_name , Text_Entry_from , Text_Entry_ttl_no_days ,  Text_Entry_type , Text_Entry_no_days_present , Text_Entry_no_days_absent , Text_Entry_adm_no , Text_Entry_to))
    clearButton.grid(row=7, column=3, padx=10, pady=5)

    search_button = tk.Button(window, text="Search",command=lambda: searchStudent(college, Text_Entry_name, Text_student_info))
    search_button.grid(row=0, column=2, padx=10, pady=5)






    window.mainloop()

if __name__ == "__main__":
    print("Code executing from same file")
        # college = College()
        # gui()