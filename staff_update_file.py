import tkinter.messagebox
import random
#import College_Std_info_BackEnd
import tkinter as tk
import staff_form
import pickle
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
#from babel.numbers import *
from tkcalendar import Calendar, DateEntry
from personal_info import Student
from personal_info import Staff
import main1
import sys

def searchStaff(college ,Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary):
    selectedStaff = college.findStaff((Text_Entry_first_name.get()))
    if selectedStaff:
       Text_Entry_qualification.insert(END, str(selectedStaff.get_qualification()))
       Text_Entry_subject.insert( END,str(selectedStaff.get_subject()))
       Text_Entry_date_of_birth.delete(0, END)
       Text_Entry_date_of_birth.insert( END,str(selectedStaff.get_date_of_birth()))
       Text_Entry_course.insert( END,str(selectedStaff.get_course()))
       Text_Entry_mobile_no.insert( END,str(selectedStaff.get_mobile_no()))
       Text_Entry_address.insert(END, str(selectedStaff.get_address()))
       Text_Entry_last_name.insert(END, str(selectedStaff.get_last_name()))
       Text_Entry_email_address.insert(END, str(selectedStaff.get_email_address()))
       Text_Entry_salary.insert(END, str(selectedStaff.get_salary()))
    else:
        messagebox.showinfo("info", 'Staff doesnt exist')


def delete (college ,Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary):
    selectedStaff = college.findStaff((Text_Entry_first_name.get()))
    if selectedStaff:
        college.remove_student(selectedStaff)
        college.write_staff_file()
        messagebox.showinfo("info", 'Staff has been deleted')
        staff_form.clear(Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary)
    else:
        messagebox.showinfo("info", 'Staff doesnt exist')



def update(college ,Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary):
    selectedStaff = college.findStaff((Text_Entry_first_name.get()))
    selectedStaff.set_qualification(Text_Entry_qualification.get())
    selectedStaff.set_subject(Text_Entry_subject.get())
    selectedStaff.set_date_of_birth(Text_Entry_date_of_birth.get())
    selectedStaff.set_course(Text_Entry_course.get())
    selectedStaff.set_mobile_no(Text_Entry_mobile_no.get())
    selectedStaff.set_address(Text_Entry_address.get())
    selectedStaff.set_last_name(Text_Entry_last_name.get())
    selectedStaff.set_email_address(Text_Entry_email_address.get())
    selectedStaff.set_salary(Text_Entry_salary.get())

def callback(window, college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)


def gui(college):
    #loadStudentFile()
    window = tk.Tk()
    window.title('Staff Info')
    window.geometry('1350x750')
    window.config(bg='gray')



    lbl_first_name = tk.Label(window, text='First Name', font=('arial', 20))
    lbl_first_name.grid(row=0, column=0, sticky='W', padx=20, pady=10)
    lbl_qualification = tk.Label(window, text='Qualifications', font=('arial', 20))
    lbl_qualification.grid(row=1, column=0, sticky='W', padx=20)
    lbl_subject = tk.Label(window, text='Subject', font=('arial', 20))
    lbl_subject.grid(row=2, column=0, sticky='W', padx=20)
    lbl_date_of_birth = tk.Label(window, text='Date of Birth', font=('arial', 20))
    lbl_date_of_birth.grid(row=3, column=0, sticky='W', padx=20)
    lbl_course = tk.Label(window, text='Course', font=('arial', 20))
    lbl_course.grid(row=4, column=0, sticky='W', padx=20)
    lbl_mobile_no = tk.Label(window, text='Phone Number', font=('arial', 20))
    lbl_mobile_no.grid(row=5, column=0, sticky='W', padx=20)
    lbl_address = tk.Label(window, text='Address', font=('arial', 20))
    lbl_address.grid(row=6, column=0, sticky='W', padx=20)

    lbl_last_name = tk.Label(window, text='Last Name', font=('arial', 20))
    lbl_last_name.grid(row=0, column=3, sticky='W', padx=20, pady=10)
    lbl_email_address = tk.Label(window, text='Email Address', font=('arial', 20))
    lbl_email_address.grid(row=1, column=3, sticky='W', padx=20)
    lbl_salary = tk.Label(window, text='Salary', font=('arial', 20))
    lbl_salary.grid(row=2, column=3, sticky='W', padx=20)
    lbl_gender = tk.Label(window, text='Gender', font=('arial', 20))
    lbl_gender.grid(row=3, column=3, sticky='W', padx=20)


    Text_Entry_first_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_first_name.grid(row=0, column=1, padx=10, pady=5)
    Text_Entry_qualification = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_qualification.grid(row=1, column=1, padx=10, pady=5)
    Text_Entry_subject = ttk.Combobox(window, values=('Select Your Subject ', 'Christianity', 'Islam', 'Judaism', 'Hinduism', 'Other'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_subject.grid(row=2, column=1, padx=10, pady=5)
    Text_Entry_date_of_birth = DateEntry(window, width=42, bg="darkblue",fg="white")  # tk.Entry(window, font=('arial', 17, 'bold'))
    Text_Entry_date_of_birth.grid(row=3, column=1, padx=10, pady=5)
    Text_Entry_course = ttk.Combobox(window, values=('Select Your Course ', 'Christianity', 'Islam', 'Judaism', 'Hinduism', 'Other'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_course.grid(row=4, column=1, padx=10, pady=5)
    Text_Entry_mobile_no = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_mobile_no.grid(row=5, column=1, padx=10, pady=5)
    Text_Entry_address = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_address.grid(row=6, column=1, padx=10, pady=5)

    v = tk.IntVar()

    Text_Entry_last_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_last_name.grid(row=0, column=4, padx=10, pady=5)
    Text_Entry_email_address = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_email_address.grid(row=1, column=4, padx=10, pady=5)
    Text_Entry_salary = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_salary.grid(row=2, column=4, padx=10, pady=5)
    Text_Entry_male_gender = tk.Radiobutton(window, text="Male", value=1, variable=v)
    Text_Entry_female_gender = tk.Radiobutton(window, text="Female", value=2, variable=v)
    Text_Entry_male_gender.grid(row=3, column=4, padx=10, pady=5)
    Text_Entry_female_gender.grid(row=3, column=5, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.grid(row=7, column=4, padx=10, pady=5)

    update_info = tk.Button(window, text="Update",command=lambda: update(college, Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary, v ))
    update_info.grid(row=7, column=2, padx=10, pady=5)

    delete_info = tk.Button(window, text="Delete",command=lambda: delete(college, Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary, v ))
    delete_info.grid(row=7, column=1, padx=10, pady=5)

    search_button = tk.Button(window, text="Search",command=lambda: searchStaff(college, Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary))
    search_button.grid(row=0, column=2, padx=10, pady=5)



    window.mainloop()

