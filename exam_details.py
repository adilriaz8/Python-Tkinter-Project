import tkinter as tk
#from college_class import College
import pickle
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from babel.numbers import *
from tkcalendar import Calendar, DateEntry
#from student import Student
import main1
import personal_info
from personal_info import Exam

def callback(window, college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)


def gui(college):
    window = tk.Tk()
    window.title('Main')
    window.geometry('1350x750')
    window.config(bg='gray')
    college.read_student_file()


    str = ''

    list = college.getAllStudent()
    for student in list:
        #print(student)
        list2 = student.getAllExams()
        #print(len(list2))
        adm_no = student.get_adm_no()
        name = student.get_first_name() + ' ' + student.get_last_name()
        str += 'Full Name : ' + name + '\nAdmission Number : ' + adm_no
        for exam in list2:
            str += '\n' + exam.__str__()

    print(str)
           #print(exam)# it access str method of exam object only if called in print statement


    #Text_Entry_student = tk.Entry(window, font=('arial', 10, 'bold'))
    #Text_Entry_student.place(x = 10, y = 10, width=1300, height=650)
    #Text_Entry_student.delete(1.0, "END")
    #Text_Entry_student.insert(0, str)


    text = Text(window, wrap=WORD)
    text.insert(INSERT,str)
    text.pack()
    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.pack()
    print(str)




    window.mainloop()


if __name__ == "__main__":
    print("Code executing from student detail file")










#put str on screen
# update adn delete record

