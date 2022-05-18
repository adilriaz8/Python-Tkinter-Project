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
    #Text_Entry_student = tk.Entry(window, font=('arial', 10, 'bold'))
    #Text_Entry_student.place(x = 10, y = 10, width=1300, height=650)
    #Text_Entry_student.delete(1.0, "END")
    #Text_Entry_student.insert(0, str(college.get_staff_list()))
    str1 = college.get_student_list()
    print(str1)
    text = Text(window, wrap=WORD)
    text.insert(INSERT,str1)
    text.pack()
    back_button = tk.Button(window, text="Back", command=lambda: callback(window, college))
    back_button.place(x = 700, y = 670)
    print(str1)
    window.mainloop()


if __name__ == "__main__":
    print("Code executing from student detail file")












