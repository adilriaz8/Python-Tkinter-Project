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
import exam

def callback(window, college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)


def searchStudent(college, Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester ):
    selectedStudent = college.findStudent((Text_Entry_name.get()))
    selectedExam = selectedStudent.findExams(Text_Entry_subject.get(), Text_Entry_semester.get())
    if selectedExam:
       #Text_Entry_admission_no.insert( END,str(selectedExam.get_admission_no()))
       Text_Entry_marks.insert(END, str(selectedExam.get_marks()))
       Text_Entry_total_marks.insert(END, str(selectedExam.get_total_marks()))
       Text_Entry_percentage.insert(END, str(selectedExam.get_percentage()))
       Text_Entry_subject.insert(END, str(selectedExam.get_subject()))
       Text_Entry_semester.insert(END, str(selectedExam.get_semester()))
    else:
        messagebox.showinfo("info", 'Student doesnt exist')

def update(college , Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester):
    selectedStudent = college.findStudent((Text_Entry_name.get()))
    selectedExam = selectedStudent.findExams(Text_Entry_subject.get(), Text_Entry_semester.get())
    #selectedExam.set_admission_no(Text_Entry_admission_no.get())
    selectedExam.set_marks(Text_Entry_marks.get())
    selectedExam.set_total_marks(Text_Entry_total_marks.get())
    selectedExam.set_percentage(Text_Entry_percentage.get())
    selectedExam.set_subject(Text_Entry_subject.get())
    selectedExam.set_semester(Text_Entry_semester.get())
    college.write_student_file()
    messagebox.showinfo("info", 'Exam Information has been updated')
def delete (college ,Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester):
    selectedStudent = college.findStudent((Text_Entry_name.get()))
    if selectedStudent:
        college.remove_student(selectedStudent)
        college.write_student_file()
        messagebox.showinfo("info", 'Student has been deleted')
        exam.clearInformation(Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester)
    else:
        messagebox.showinfo("info", 'Student doesnt exist')


def gui(college):
    #loadStudentFile()
    window = tk.Tk()
    window.title('Exam Information')
    window.geometry('1350x750')
    window.config(bg='gray')
    college.read_student_file()

    lbl_Name = tk.Label(window, text='Name', font=('arial', 20))
    lbl_Name.grid(row=0, column=0, sticky='W', padx=20, pady=10)
    lbl_admission_no = tk.Label(window, text='Admission Number', font=('arial', 20))
    lbl_admission_no.grid(row=1, column=0, sticky='W', padx=20, pady=10)
    lbl_marks = tk.Label(window, text='Marks Obtained', font=('arial', 20))
    lbl_marks.grid(row=2, column=0, sticky='W', padx=20, pady=10)
    lbl_total_marks = tk.Label(window, text='Total Marks', font=('arial', 20))
    lbl_total_marks.grid(row=3, column=0, sticky='W', padx=20, pady=10)
    lbl_percentage = tk.Label(window, text='Percentage', font=('arial', 20))
    lbl_percentage.grid(row=4, column=0, sticky='W', padx=20, pady=10)
    lbl_subject = tk.Label(window, text='Subject', font=('arial', 20))
    lbl_subject.grid(row=5, column=0, sticky='W', padx=20, pady=10)
    lbl_semester = tk.Label(window, text='Semester', font=('arial', 20))
    lbl_semester.grid(row=6, column=0, sticky='W', padx=20, pady=10)


    Text_Entry_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_name.grid(row=0, column=1, padx=10, pady=5)
    Text_Entry_admission_no = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_admission_no.grid(row=1, column=1, padx=10, pady=5)
    Text_Entry_marks = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_marks.grid(row=2, column=1, padx=10, pady=5)
    Text_Entry_total_marks = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_total_marks.grid(row=3, column=1, padx=10, pady=5)
    Text_Entry_percentage = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_percentage.grid(row=4, column=1, padx=10, pady=5)
    Text_Entry_subject = ttk.Combobox(window, values=('Select a Subject ', 'College Algebra', 'English', 'Introduction to American History'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_subject.grid(row=5, column=1, padx=10, pady=5)
    Text_Entry_semester = ttk.Combobox(window, values=('Select a Semester ', 'Winter', 'Spring', 'Fall', 'Summer'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_semester.grid(row=6, column=1, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.grid(row=7, column=1, padx=10, pady=5)

    search_button = tk.Button(window, text="Search",command=lambda: searchStudent(college, Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester))
    search_button.grid(row=0, column=2, padx=10, pady=5)

    update_info = tk.Button(window, text="Update",command=lambda: update(college, Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester))
    update_info.grid(row=7, column=2, padx=10, pady=5)

    delete_info = tk.Button(window, text="Delete",command=lambda: delete(college, Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester))
    delete_info.grid(row=7, column=3, padx=10, pady=5)



