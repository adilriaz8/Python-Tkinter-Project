
import tkinter as tk
import os
import sys
import student_form2
import staff_form
import staff_details
import student_details
import fees
import exam
import exam_details
import fees_update_file
import update_file
from college_class import College

college = College() # creating the object of college class



def gui(college):

    window = tk.Tk()
    window.title('Main')
    window.geometry('1350x750')
    window.config(bg='gray')
    tk.Button(window, text="Student Form", command=lambda:callback(window)).pack()
    tk.Button(window, text="Staff Form", command=lambda: callback_2(window)).pack()
    tk.Button(window, text="Staff Details", command=lambda: staff_detail_form(window)).pack()
    tk.Button(window, text="Student Details", command=lambda: student_detail_form(window)).pack()
    tk.Button(window, text="Fee's", command=lambda: callback_3(window)).pack()
    tk.Button(window, text="Exam Information", command=lambda: callback_4(window)).pack()
    tk.Button(window, text="Student Attendance", command=lambda: callback_5(window)).pack()
    tk.Button(window, text="Exam Details", command=lambda: callback_6(window)).pack()

    window.mainloop()
def callback(window):
    print("Opening Student Form")
    window.destroy()
    student_form2.gui(college)
    #sys.exit() # closes the existing script
    
def callback_2(window):
    print("Opening Staff From")
    window.destroy()
    staff_form.gui(college)

def callback_3(window):
    print("Opening Fee's From")
    window.destroy()
    fees.gui(college)

def callback_4(window):
    print("Opening Exam Form")
    window.destroy()
    exam.gui(college)

def callback_5(window):
    print("Opening Student Attendance")
    window.destroy()
    student_attendance.gui(college)


def callback_6(window):
    print("Opening Exam Details")
    window.destroy()
    exam_details.gui(college)



def staff_detail_form(window):
    print("Opening Staff Details")
    window.destroy()
    staff_details.gui(college)
    # create open staff detail window passing college object as parameter
    # todo: print the staff list data into textarea of new window, new window should have back button
    # how to set any text into textarea
def student_detail_form(window):
    print("Opening Student details")
    window.destroy()
    student_details.gui(college)
    # open student detail window passing college object as parameter
    #todo: print the college.get_student list() data into textarea of new window, new window should have back button



if __name__ == "__main__":
    gui(college)




#return self.father_job
        # include fees informtation also in the returned str
        # call str of each fees from fees_list and merge into final str

        #write short story
        #added the college object in all paramaters and fixed the string outputting the students info and student details we added where it shows the students fees and also thier wholde details
        #update uml diagram
        #update exam and link with student