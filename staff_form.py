import tkinter.messagebox
import random
#import College_Std_info_BackEnd
import tkinter as tk
import staff_update_file
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


staff_list = []

def callback(window):
    print("Opening Main window")
    window.destroy()
    main1.gui()

def update(window , college):
    print("Opening Update Information")
    window.destroy()
    staff_update_file.gui(college)

def loadStudentFile():
    global staff_list
    try:
        f = open('staff.pickle', 'rb')
        staff_list = pickle.load(f)
        print("Staff Information Loaded Successfully!")
        for each in staff_list:
            print(each)
            print()
        f.close()
    except:
        print("File doesnt found")


def check(Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary, v):
    for c in Text_Entry_first_name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the First Name")
            return False
    if Text_Entry_first_name.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_qualification.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the Qualification")
            return False
    if Text_Entry_qualification.get() == '':
        messagebox.showinfo('Error', "Empty field in Qualification")
        return False
    for c in Text_Entry_subject.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the Subject")
            return False
    if Text_Entry_subject.get() == '':
        messagebox.showinfo('Error', "Empty field in Subject")
        return False

    if Text_Entry_date_of_birth.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")

    for c in Text_Entry_course.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the Course")
            return False
    if Text_Entry_course.get() == '':
        messagebox.showinfo('Error', "Empty field in Course")
        return False

    for c in Text_Entry_mobile_no.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in Phone Number")
            return False
    if Text_Entry_mobile_no.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")


    if Text_Entry_address.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")

    for c in Text_Entry_last_name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the Last Name")
            return False
    if Text_Entry_last_name.get() == '':
        messagebox.showinfo('Error', "Empty field in Last Name")


    if Text_Entry_email_address.get() == '':
        messagebox.showinfo('Error', "Empty field in email address")

    for c in Text_Entry_salary.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in the Salary")
            return False
    if Text_Entry_salary.get() == '':
        messagebox.showinfo('Error', "Empty field in Salary")

    return True
def save(college , Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary, v):
    gender = ''
    if v.get() == 1:
        gender = 'male'
    elif v.get() == 2:
        gender = 'female'
    print(gender)
    global staff_list
    if check(Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary, v.get()):
        s1 = Staff(Text_Entry_first_name.get() ,Text_Entry_qualification.get(), Text_Entry_subject.get(), Text_Entry_date_of_birth.get(),  Text_Entry_course.get(), Text_Entry_mobile_no.get(), Text_Entry_address.get(), Text_Entry_last_name.get(), Text_Entry_email_address.get(), Text_Entry_salary.get(), gender)
        messagebox.showinfo("info", "Information is saved successfully!\n" + s1.__str__())
        college.add_staff(s1)
        college.write_staff_file()
    else:
        print('Error with entering information')

def exit(college , window):
    window.destroy()
    college.write_staff_file()
    '''
    f = open('staff.pickle', 'wb')
    pickle.dump(staff_list,f)
    f.close()
    '''
def callback(window):
    print("Opening Main window")
    window.destroy()
    main1.gui()


def clear(Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary, v):
    Text_Entry_first_name.delete(0, END)
    Text_Entry_qualification.delete(0, END)
    Text_Entry_subject.delete(0, END)
    Text_Entry_date_of_birth.delete(0, END)
    Text_Entry_course.delete(0, END)
    Text_Entry_mobile_no.delete(0, END)
    Text_Entry_address.delete(0, END)
    Text_Entry_last_name.delete(0, END)
    Text_Entry_email_address.delete(0, END)
    Text_Entry_salary.delete(0, END)



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
    lbl_last_name.grid(row=0, column=2, sticky='W', padx=20, pady=10)
    lbl_email_address = tk.Label(window, text='Email Address', font=('arial', 20))
    lbl_email_address.grid(row=1, column=2, sticky='W', padx=20)
    lbl_salary = tk.Label(window, text='Salary', font=('arial', 20))
    lbl_salary.grid(row=2, column=2, sticky='W', padx=20)
    lbl_gender = tk.Label(window, text='Gender', font=('arial', 20))
    lbl_gender.grid(row=3, column=2, sticky='W', padx=20)


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
    Text_Entry_last_name.grid(row=0, column=3, padx=10, pady=5)
    Text_Entry_email_address = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_email_address.grid(row=1, column=3, padx=10, pady=5)
    Text_Entry_salary = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_salary.grid(row=2, column=3, padx=10, pady=5)
    Text_Entry_male_gender = tk.Radiobutton(window, text="Male", value=1, variable=v)
    Text_Entry_female_gender = tk.Radiobutton(window, text="Female", value=2, variable=v)
    Text_Entry_male_gender.grid(row=3, column=3, padx=10, pady=5)
    Text_Entry_female_gender.grid(row=3, column=4, padx=10, pady=5)



    save_button = tk.Button(window, text="Save", command=lambda: save(college , Text_Entry_first_name ,Text_Entry_qualification, Text_Entry_subject, Text_Entry_date_of_birth ,  Text_Entry_course, Text_Entry_mobile_no, Text_Entry_address, Text_Entry_last_name, Text_Entry_email_address, Text_Entry_salary, v))
    save_button.grid(row=7, column=2, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda: callback(window))
    back_button.grid(row=7, column=4, padx=10, pady=5)

    exit_button = tk.Button(window, text="Exit", command=lambda: exit(college , window))
    exit_button.grid(row=7, column=3, padx=10, pady=5)

    update_button = tk.Button(window, text="Update / Delete", command=lambda: update(window, college))
    update_button.grid(row=7, column=1, padx=10, pady=5)


    window.mainloop()

#gui()



if __name__ == "__main__":
    print("Code executing from same file")
    #gui()


#write date into pickle on exit , create an exit button , data should be loaded into staff list when gui is loaded first time on every restrart
#put link of staff gui on  main , start creating new screen