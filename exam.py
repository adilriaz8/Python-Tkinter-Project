import tkinter.messagebox
import random
#import College_Std_info_BackEnd
import tkinter as tk
import exam_update_file
import pickle
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
#from babel.numbers import *
from tkcalendar import Calendar, DateEntry
#from student2 import Student
import main1
import sys
from personal_info import Student , Exam

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

def update(window , college):
    print("Opening Update Information")
    window.destroy()
    exam_update_file.gui(college)



def check(Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester):
    for c in Text_Entry_name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the Name")
            return False
    if Text_Entry_name.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_admission_no.get() :
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in Admission Number")
            return False
    if Text_Entry_admission_no.get()  == '':
        messagebox.showinfo('Error', "Empty field in Admission Number")
        return False
    for c in Text_Entry_marks.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in Marks")
            return False
    if Text_Entry_marks.get() == '':
        messagebox.showinfo('Error', "Empty field in Marks")
        return False
    for c in Text_Entry_total_marks.get() :
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in Total Marks")
            return False
    if Text_Entry_total_marks.get()  == '':
        messagebox.showinfo('Error', "Empty field in Total Marks")
        return False
    for c in Text_Entry_percentage.get() :
        if c.isdigit() != True:
            messagebox.showinfo('Error', "Only digits in Percentage")
            return False
    if Text_Entry_percentage.get() == '':
        messagebox.showinfo('Error', "Empty field in Percentage")
        return False

    return True


def saveInformation(college , Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester):
    if check(Text_Entry_name,Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester):
        e = Exam( Text_Entry_marks.get() ,  Text_Entry_total_marks.get() , Text_Entry_percentage.get() , Text_Entry_semester.get() , Text_Entry_subject.get())

        studentName = Text_Entry_name.get()
        student1 = college.findStudent(studentName)
        #print(student1)
        #print(e)
        #print('hi')
        # student_list.append(s)
        #college.add_student(s)
        #college.write_student_file()

        if student1:
            student1.add_exams(e)
            college.write_student_file()
            messagebox.showinfo("info", "Information is saved successfully!\n" + e.__str__())
            clearInformation(Text_Entry_name, Text_Entry_admission_no, Text_Entry_marks, Text_Entry_total_marks,
                             Text_Entry_percentage, Text_Entry_subject, Text_Entry_semester)

        else:
            messagebox.showinfo('info', 'Student not Found')

    else:
        print('Error with entering information')






def clearInformation(Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester):
    Text_Entry_name.delete(0, END)
    Text_Entry_admission_no.delete(0, END)
    Text_Entry_marks.delete(0, END)
    Text_Entry_total_marks.delete(0, END)
    Text_Entry_percentage.delete(0, END)
    Text_Entry_subject.delete(0, END)
    Text_Entry_semester.delete(0, END)

def calculate(Text_Entry_marks , Text_Entry_total_marks , Text_Entry_percentage):
    if int(Text_Entry_marks.get()) >= int(Text_Entry_total_marks.get()):
        messagebox.showinfo('Error', "Marks obtained cannot be greater than Total Marks")

    elif int(Text_Entry_marks.get()) < 0 or int(Text_Entry_total_marks.get()) < 0:
        messagebox.showinfo('Error', "Marks obtained and Total Marks have to be greater than 0")

    else:
        sum = (int(Text_Entry_marks.get()) / int(Text_Entry_total_marks.get())) * 100
        Text_Entry_percentage.insert(INSERT, round(sum))

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

    str1 = 'Sr No\t\t\tStudent Name\t\t\tPhone\t\t\tCourse'
    Text_student_info = Text(window, wrap=WORD)
    Text_student_info.grid(row=1, rowspan=4, column=3, padx=40, pady=40)  # starts at row 2 then we rowspan it to row 7
    Text_student_info.insert(INSERT, str1)

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




    saveButton = tk.Button(window, text="Save Information",command=lambda: saveInformation(college, Text_Entry_name , Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject , Text_Entry_semester))
    saveButton.grid(row=7, column=0, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda: callback(window , college))
    back_button.grid(row=7, column=1, padx=10, pady=5)

    update_button = tk.Button(window, text="Update", command=lambda: update(window , college))
    update_button.grid(row=7, column=2, padx=10, pady=5)

    clearButton = tk.Button(window, text="Clear",command=lambda: clearInformation(Text_Entry_name, Text_Entry_admission_no , Text_Entry_marks ,  Text_Entry_total_marks , Text_Entry_percentage , Text_Entry_subject, Text_Entry_semester ))
    clearButton.grid(row=7, column=3, padx=10, pady=5)

    calculate_percentage = tk.Button(window, text="Calculate",command=lambda: calculate(Text_Entry_marks , Text_Entry_total_marks , Text_Entry_percentage))
    calculate_percentage.grid(row=4, column=2, padx=10, pady=5)


    search_button = tk.Button(window, text="Search", command=lambda: searchStudent(college, Text_Entry_name , Text_student_info))
    search_button.grid(row=0, column=2, padx=10, pady=5)

    update_button = tk.Button(window, text="Update / Delete", command=lambda: update(window, college))
    update_button.grid(row=7, column=3, padx=10, pady=5)



if __name__ == "__main__":
    print("Code executing from same file")
    #college = College()
    #gui()
