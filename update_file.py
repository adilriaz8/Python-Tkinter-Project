import tkinter.messagebox
import random
#import College_Std_info_BackEnd
import tkinter as tk
import tkinter as tk
from tkinter import simpledialog
import pickle
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
#from babel.numbers import *
from tkcalendar import Calendar, DateEntry
#from student2 import Student
import main1
import student_form2
#from student_form2 import clearInformation

import sys
from personal_info import Student

def delete (college , Text_Entry_name ,Text_Entry_adm_no,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion):
    selectedStudent = college.findStudent((Text_Entry_name.get()))
    if selectedStudent:
        college.remove_student(selectedStudent)
        college.write_student_file()
        messagebox.showinfo("info", 'Student has been deleted')
        student_form2.clearInformation(Text_Entry_name ,Text_Entry_adm_no,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion)
    else:
        messagebox.showinfo("info", 'Student doesnt exist')



def searchStudent(college, Text_Entry_name ,Text_Entry_adm_no,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion ):
    selectedStudent = college.findStudent((Text_Entry_name.get()))
    if selectedStudent:
       Text_Entry_adm_no.insert( END,str(selectedStudent.get_adm_no()))
       Text_Entry_Father_Name.insert(END,selectedStudent.get_father_name())
       Text_Entry_father_job.insert(END,selectedStudent.get_father_job())
       Text_Entry_date_of_birth.delete(0, END)
       Text_Entry_date_of_birth.insert(END,selectedStudent.get_date_of_birth())
       Text_Entry_course.insert(END,selectedStudent.get_course())
       Text_Entry_mobile_no.insert(END,selectedStudent.get_mobile_no())
       Text_Entry_landline_no.insert(END,selectedStudent.get_landline_no())
       Text_Entry_address.insert(END,selectedStudent.get_address())
       Text_Entry_admission.delete(0, END)
       Text_Entry_admission.insert(END,selectedStudent.get_admission())
       Text_Entry_last_name.insert(END,selectedStudent.get_last_name())
       Text_Entry_mother_name.insert(END,selectedStudent.get_mother_name())
       Text_Entry_mother_job.insert(END,selectedStudent.get_mother_job())
       Text_Entry_section.insert(END,selectedStudent.get_section())
       Text_Entry_blood_group.insert(END,selectedStudent.get_blood_group())
       Text_Entry_religion.insert(END,selectedStudent.get_religion())
    else:
        messagebox.showinfo("info", 'Student doesnt exist')


def update(college , Text_Entry_name ,Text_Entry_adm_no,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion):
    selectedStudent = college.findStudent((Text_Entry_name.get()))
    selectedStudent.set_first_name(Text_Entry_name.get())
    selectedStudent.set_adm_no(Text_Entry_adm_no.get())
    selectedStudent.set_father_Name(Text_Entry_Father_Name.get())
    selectedStudent.set_father_job(Text_Entry_father_job.get())
    selectedStudent.set_date_of_birth(Text_Entry_date_of_birth.get())
    selectedStudent.set_course(Text_Entry_course.get())
    selectedStudent.set_mobile_no(Text_Entry_mobile_no.get())
    selectedStudent.set_landline_no(Text_Entry_landline_no.get())
    selectedStudent.set_address(Text_Entry_address.get())
    selectedStudent.set_admission(Text_Entry_admission.get())
    selectedStudent.set_last_name(Text_Entry_last_name.get())
    selectedStudent.set_mother_name(Text_Entry_mother_name.get())
    selectedStudent.set_mother_job(Text_Entry_mother_job.get())
    selectedStudent.set_section(Text_Entry_section.get())
    selectedStudent.set_blood_group(Text_Entry_blood_group.get())
    selectedStudent.set_religion(Text_Entry_religion.get())
    college.write_student_file()
    messagebox.showinfo("info", 'Information has been updated')
def callback(window, college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)


def gui(college):
    #loadStudentFile()
    college.read_student_file()
    window = tk.Tk()
    window.title('Update Information')
    window.geometry('1350x750')
    window.config(bg='gray')

    lbl_adm_no = tk.Label(window, text='Admission Number', font=('arial', 20))
    lbl_adm_no.grid(row=1, column=0, sticky='W', padx=20, pady=10)
    lbl_Name = tk.Label(window, text='Name', font=('arial', 20))
    lbl_Name.grid(row=0, column=0, sticky='W', padx=20, pady=10)
    lbl_father_name = tk.Label(window, text='Father Name', font=('arial', 20))
    lbl_father_name.grid(row=2, column=0, sticky='W', padx=20)
    lbl_father_job = tk.Label(window, text='Fathers Occupation', font=('arial', 20))
    lbl_father_job.grid(row=3, column=0, sticky='W', padx=20)
    lbl_date_of_birth = tk.Label(window, text='Date of Birth', font=('arial', 20))
    lbl_date_of_birth.grid(row=4, column=0, sticky='W', padx=20)
    lbl_course = tk.Label(window, text='Course', font=('arial', 20))
    lbl_course.grid(row=5, column=0, sticky='W', padx=20)
    lbl_mobile_no = tk.Label(window, text='Phone Number', font=('arial', 20))
    lbl_mobile_no.grid(row=6, column=0, sticky='W', padx=20)
    lbl_landline_no = tk.Label(window, text='Landline Number', font=('arial', 20))
    lbl_landline_no.grid(row=7, column=0, sticky='W', padx=20)
    lbl_address = tk.Label(window, text='Address', font=('arial', 20))
    lbl_address.grid(row=8, column=0, sticky='W', padx=20)

    lbl_admission = tk.Label(window, text='Admission Date', font=('arial', 20))
    lbl_admission.grid(row=1, column=2, sticky='W', padx=20, pady=10)
    lbl_last_name = tk.Label(window, text='Last Name', font=('arial', 20))
    lbl_last_name.grid(row=2, column=2, sticky='W', padx=20, pady=10)
    lbl_mother_name = tk.Label(window, text='Mother Name', font=('arial', 20))
    lbl_mother_name.grid(row=3, column=2, sticky='W', padx=20, pady=10)
    lbl_mother_job = tk.Label(window, text='Mothers Occupation', font=('arial', 20))
    lbl_mother_job.grid(row=4, column=2, sticky='W', padx=20, pady=10)
    lbl_gender = tk.Label(window, text='Gender', font=('arial', 20))
    lbl_gender.grid(row=5, column=2, sticky='W', padx=20, pady=10)
    lbl_section = tk.Label(window, text='Section', font=('arial', 20))
    lbl_section.grid(row=6, column=2, sticky='W', padx=20, pady=10)
    lbl_blood_group = tk.Label(window, text='Blood Group', font=('arial', 20))
    lbl_blood_group.grid(row=7, column=2, sticky='W', padx=20, pady=10)
    lbl_religion = tk.Label(window, text='Religion', font=('arial', 20))
    lbl_religion.grid(row=8, column=2, sticky='W', padx=20, pady=10)

    Text_Entry_adm_no = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_adm_no.grid(row=1, column=1, padx=10, pady=5)
    Text_Entry_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_name.grid(row=0, column=1, padx=10, pady=5)
    Text_Entry_Father_Name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_Father_Name.grid(row=2, column=1, padx=10, pady=5)
    Text_Entry_father_job = ttk.Combobox(window, values=('Select your Fathers Job', 'Doctor', 'Engineer', 'Lawyer'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_father_job.grid(row=3, column=1, padx=10, pady=5)
    Text_Entry_date_of_birth = DateEntry(window, width=42, bg="darkblue", fg="white", year=2010)
    Text_Entry_date_of_birth.grid(row=4, column=1, padx=20, pady=10)
    Text_Entry_course = ttk.Combobox(window, values=('Select a Course ', 'College Algebra', 'English', 'Introduction to American History'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_course.grid(row=5, column=1, padx=10, pady=5)
    Text_Entry_mobile_no = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=email_address)
    Text_Entry_mobile_no.grid(row=6, column=1, padx=10, pady=5)
    Text_Entry_landline_no = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=date_of_birth)
    Text_Entry_landline_no.grid(row=7, column=1, padx=10, pady=5)
    Text_Entry_address = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=date_of_birth)
    Text_Entry_address.grid(row=8, column=1, padx=10, pady=5)

    v = tk.IntVar()

    Text_Entry_admission = DateEntry(window, width=42, bg="darkblue", fg="white")  # tk.Entry(window, font=('arial', 17, 'bold'))
    Text_Entry_admission.grid(row=1, column=3, padx=10, pady=5)
    Text_Entry_last_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_last_name.grid(row=2, column=3, padx=10, pady=5)
    Text_Entry_mother_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_mother_name.grid(row=3, column=3, padx=10, pady=5)
    Text_Entry_mother_job = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_mother_job.grid(row=4, column=3, padx=10, pady=5)
    Text_Entry_male_gender = tk.Radiobutton(window, text="Male", value=1, variable=v)
    Text_Entry_female_gender = tk.Radiobutton(window, text="Female", value=2, variable=v)
    Text_Entry_male_gender.grid(row=5, column=3, padx=10, pady=5)
    Text_Entry_female_gender.grid(row=5, column=4, padx=10, pady=5)
    Text_Entry_section = ttk.Combobox(window, values=('Choose a Section', 'A', 'B', 'C'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_section.grid(row=6, column=3, padx=10, pady=5)
    Text_Entry_blood_group = ttk.Combobox(window, values=('Select a Blood Group', 'A', 'B', 'AB', 'O'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_blood_group.grid(row=7, column=3, padx=10, pady=5)
    Text_Entry_religion = ttk.Combobox(window, values=('Select Your Religion ', 'Christianity', 'Islam', 'Judaism', 'Hinduism', 'Other'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_religion.grid(row=8, column=3, padx=10, pady=5)

    search_button = tk.Button(window, text="Search",command=lambda: searchStudent(college, Text_Entry_name ,Text_Entry_adm_no,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion))
    search_button.grid(row=0, column=2, padx=10, pady=5)

    update_info = tk.Button(window, text="Update", command=lambda: update(college , Text_Entry_name ,Text_Entry_adm_no,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion))
    update_info.grid(row=9, column=2, padx=10, pady=5)

    delete_info = tk.Button(window, text="Delete",command=lambda: delete(college, Text_Entry_name, Text_Entry_adm_no,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion))
    delete_info.grid(row=9, column=1, padx=10, pady=5)


    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.grid(row=9, column=3, padx=10, pady=5)

    window.mainloop()

if __name__ == "__main__":
    print("Code executing from same file")


# update and delete method  for staff , fees , exam
#finish attendance