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
import sys
from personal_info import Student
import update_file

student_list = []

def loadStudentFile():
    global student_list
    try:
        f = open('student_information.pickle', 'rb')
        student_list = pickle.load(f)
        print("Student Information Loaded Successfully!")
        for each in student_list:
            print(each)
            print()
        f.close()
    except:
        print("File doesnt found")

    

def exit(college, window):
    window.destroy()
    college.write_student_file()
    '''
    f = open('student_information.pickle', 'wb')
    pickle.dump(student_list,f)
    f.close()
    '''

    
def callback(window, college):
    print("Opening Main window")
    window.destroy()
    main1.gui(college)
    #sys.exit()  # closes the existing script

#def grad_date():
    #date.config(text="Selected Date is: " + Text_Entry_admission.get_date())


def check(Text_Entry_adm_no , Text_Entry_name ,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  , v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion):
    for c in Text_Entry_adm_no.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in the Admission Number")
            return False
    if Text_Entry_adm_no.get() == '':
        messagebox.showinfo('Error', "Empty field in Admission Number")
        return False
    for c in Text_Entry_name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in the Name")
            return False
    if Text_Entry_name.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_Father_Name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Father Name")
            return False
    if Text_Entry_Father_Name.get() == '':
        messagebox.showinfo('Error', "Empty field in Father Name")
        return False
    for c in Text_Entry_father_job.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Father Job")
            return False
    if Text_Entry_father_job.get() == '':
        messagebox.showinfo('Error', "Empty field in Father Job")
        return False
    #for c in Text_Entry_date_of_birth.get():
        #if c.isdigit():
            #messagebox.showinfo('Error', "No digits in this field")
    for c in Text_Entry_course.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Course")
            return False
    if Text_Entry_course.get() == '':
        messagebox.showinfo('Error', "Empty field in Course")
        return False
    for c in Text_Entry_mobile_no.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in Mobile Number")
            return False
    if Text_Entry_mobile_no.get() == '':
        messagebox.showinfo('Error', "Empty field in Mobile Number")
        return False
    for c in Text_Entry_landline_no.get():
        if c.isdigit() != True:
            messagebox.showinfo('Error', "No letters in Landline Number")
            return False
    if Text_Entry_landline_no.get() == '':
        messagebox.showinfo('Error', "Empty field in Landline Number")
        return False
    '''
    for c in Text_Entry_admission.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Admission")
            return False
    '''
    if Text_Entry_admission.get() == '':
        messagebox.showinfo('Error', "Empty field in Admission")
        return False
    for c in Text_Entry_last_name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Last Name")
            return False
    if Text_Entry_last_name.get() == '':
        messagebox.showinfo('Error', "Empty field in Last Name")
        return False
    for c in Text_Entry_mother_name.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Mother Name")
            return False
    if Text_Entry_mother_name.get() == '':
        messagebox.showinfo('Error', "Empty field in Mother Name")
        return False
    for c in Text_Entry_mother_job.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Mother Job")
            return False
    if Text_Entry_mother_job.get() == '':
        messagebox.showinfo('Error', "Empty field in Name")
        return False
    for c in Text_Entry_section.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Section")
            return False
    if Text_Entry_section.get() == '':
        messagebox.showinfo('Error', "Empty field in Section")
        return False
    for c in Text_Entry_blood_group.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Blood Group")
            return False
    if Text_Entry_blood_group.get() == '':
        messagebox.showinfo('Error', "Empty field in Blood Group")
        return False
    for c in Text_Entry_religion.get():
        if c.isdigit():
            messagebox.showinfo('Error', "No digits in Religion")
            return False
    if Text_Entry_religion.get() == '':
        messagebox.showinfo('Error', "Empty field in Religion")
        return False
    return True



def saveInformation(college, Text_Entry_adm_no ,Text_Entry_name ,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion):
    # this function would be able to receive all inputs and store data into object of student
    # in the begining of the function you should validate all text entries , create object only if all data is valid
    global object_list
    gender = ''
    if v.get() == 1:
        gender = 'male'
    elif v.get() == 2:
        gender = 'female'
    print(gender)
    print( Text_Entry_date_of_birth.get())
    # do the validation of each textentry and create object if all data is valid
    # u might call a method for vlaidation here
    if check(Text_Entry_adm_no, Text_Entry_name ,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion):
        #we are creating the student object
        s = Student(Text_Entry_adm_no.get() , Text_Entry_name.get() , Text_Entry_Father_Name.get() , Text_Entry_father_job.get() , Text_Entry_date_of_birth.get() ,Text_Entry_course.get() , Text_Entry_mobile_no.get() , Text_Entry_landline_no.get() , Text_Entry_address.get() , Text_Entry_admission.get(),Text_Entry_last_name.get() ,Text_Entry_mother_name.get() , Text_Entry_mother_job.get(), gender ,Text_Entry_section.get(), Text_Entry_blood_group.get(), Text_Entry_religion.get())
        messagebox.showinfo("info", "Information is saved successfully!\n"+ s.__str__())
        #student_list.append(s)
        college.add_student(s)
        college.write_student_file()
    else:
        print('Error with entering information')


def update(window , college):
    print("Opening Update Information")
    window.destroy()
    update_file.gui(college)

def delete(college , Text_Entry_Name):
    delete_info1 = simpledialog.askstring(title="Update", prompt='Which students information would you like to delete')
    delete_info2 = simpledialog.askstring(title="Update",prompt="What would you like to delete :")
    selectedStudent = college.findStudent(delete_info1)
    if delete_info2.lower() == 'Name':
        Text_Entry_Name = ''


def clearInformation(Text_Entry_adm_no , Text_Entry_name ,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  , v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion):
    Text_Entry_adm_no.delete(0, END)
    Text_Entry_name.delete(0, END)
    Text_Entry_Father_Name.delete(0 , END)
    Text_Entry_father_job.delete(0 , END)
    Text_Entry_date_of_birth.delete(0 , END)
    Text_Entry_course.delete(0 , END)
    Text_Entry_mobile_no.delete(0 , END)
    Text_Entry_landline_no.delete(0 , END)
    Text_Entry_address.delete(0 , END)
    Text_Entry_admission.delete(0 , END)
    Text_Entry_last_name.delete(0 , END)
    Text_Entry_mother_name.delete(0 , END)
    Text_Entry_mother_job.delete(0 , END)
    Text_Entry_section.delete(0 , END)
    Text_Entry_blood_group.delete(0 , END)
    Text_Entry_religion.delete(0 ,END)

#format str method
# show proper format like name : example , and on a new line father name : example
def gui(college):
    #loadStudentFile()
    college.read_student_file()
    window = tk.Tk()
    window.title('Student Information')
    window.geometry('1350x750')
    window.config(bg='gray')
    '''
    if (len(name.get()) != 0):
        College_Std_info_BackEnd.delete(selected_tuple[0])

    if (len(name.get()) != 0):
        College_Std_info_BackEnd.insert(name.get(), father_name.get(), mother_name.get(), address.get(), mobileno.get(), email_address.get(), date_of_birth.get(), gender.get())
        listbox.delete(0, END)
        listbox.insert(END, (
        name.get(), father_name.get(), mother_name.get(), address.get(), mobileno.get(),
        email_address.get(), date_of_birth.get(), \
        gender.get()))
    '''
    lbl_adm_no = tk.Label(window, text='Admission Number', font=('arial', 20))
    lbl_adm_no.grid(row=0, column=0, sticky='W', padx=20, pady=10)
    lbl_Name = tk.Label(window, text='Name', font=('arial', 20))
    lbl_Name.grid(row=1, column=0, sticky='W', padx=20, pady=10)
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
    lbl_admission.grid(row=0, column=2, sticky='W', padx=20, pady=10)
    lbl_last_name = tk.Label(window, text='Last Name', font=('arial', 20))
    lbl_last_name.grid(row=1, column=2, sticky='W', padx=20, pady=10)
    lbl_mother_name = tk.Label(window, text='Mother Name', font=('arial', 20))
    lbl_mother_name.grid(row=2, column=2, sticky='W', padx=20, pady=10)
    lbl_mother_job = tk.Label(window, text='Mothers Occupation', font=('arial', 20))
    lbl_mother_job.grid(row=3, column=2, sticky='W', padx=20, pady=10)
    lbl_gender = tk.Label(window, text='Gender', font=('arial', 20))
    lbl_gender.grid(row=4, column=2, sticky='W', padx=20, pady=10)
    lbl_section= tk.Label(window, text='Section', font=('arial', 20))
    lbl_section.grid(row=5, column=2, sticky='W', padx=20, pady=10)
    lbl_blood_group= tk.Label(window, text='Blood Group', font=('arial', 20))
    lbl_blood_group.grid(row=6, column=2, sticky='W', padx=20, pady=10)
    lbl_religion = tk.Label(window, text='Religion', font=('arial', 20))
    lbl_religion.grid(row=7, column=2, sticky='W', padx=20, pady=10)

    Text_Entry_adm_no = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=name)
    Text_Entry_adm_no.grid(row=0, column=1, padx=10, pady=5)
    Text_Entry_name = tk.Entry(window, font=('arial', 17, 'bold'))#, textvariable=name)
    Text_Entry_name.grid(row=1, column=1, padx=10, pady=5)
    Text_Entry_Father_Name = tk.Entry(window, font=('arial', 17, 'bold'))#, textvariable=father_name)
    Text_Entry_Father_Name.grid(row=2, column=1, padx=10, pady=5)
    Text_Entry_father_job = ttk.Combobox(window, values=('Select your Fathers Job', 'Doctor', 'Engineer', 'Lawyer'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_father_job.grid(row=3, column=1, padx=10, pady=5)
    Text_Entry_date_of_birth = DateEntry(window ,width=42,bg="darkblue",fg="white",year=2010)
    Text_Entry_date_of_birth.grid(row=4, column=1, padx=20, pady=10)
    Text_Entry_course = ttk.Combobox(window, values=('Select a Course ', 'College Algebra', 'English', 'Introduction to American History'), font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_course.grid(row=5, column=1, padx=10, pady=5)
    Text_Entry_mobile_no = tk.Entry(window, font=('arial', 17, 'bold'))#, textvariable=email_address)
    Text_Entry_mobile_no.grid(row=6, column=1, padx=10, pady=5)
    Text_Entry_landline_no = tk.Entry(window, font=('arial', 17, 'bold'))#, textvariable=date_of_birth)
    Text_Entry_landline_no.grid(row=7, column=1, padx=10, pady=5)
    Text_Entry_address = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=date_of_birth)
    Text_Entry_address.grid(row=8, column=1, padx=10, pady=5)

    v = tk.IntVar()

    Text_Entry_admission = DateEntry(window ,width=42,bg="darkblue",fg="white")#tk.Entry(window, font=('arial', 17, 'bold'))
    Text_Entry_admission.grid(row=0, column=3, padx=10, pady=5)
    Text_Entry_last_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_last_name.grid(row=1, column=3, padx=10, pady=5)
    Text_Entry_mother_name = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_mother_name.grid(row=2, column=3, padx=10, pady=5)
    Text_Entry_mother_job = tk.Entry(window, font=('arial', 17, 'bold'))  # , textvariable=father_name)
    Text_Entry_mother_job.grid(row=3, column=3, padx=10, pady=5)
    Text_Entry_male_gender = tk.Radiobutton(window, text="Male" , value =1 , variable = v )
    Text_Entry_female_gender = tk.Radiobutton(window, text="Female", value=2 , variable = v)
    Text_Entry_male_gender.grid(row=4, column=3, padx=10, pady=5)
    Text_Entry_female_gender.grid(row=4, column=4, padx=10, pady=5)
    Text_Entry_section = ttk.Combobox(window, values=('Choose a Section', 'A', 'B', 'C'), font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_section.grid(row=5, column=3, padx=10, pady=5)
    Text_Entry_blood_group = ttk.Combobox(window, values=('Select a Blood Group', 'A', 'B', 'AB', 'O'),font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_blood_group.grid(row=6, column=3, padx=10, pady=5)
    Text_Entry_religion = ttk.Combobox(window, values=('Select Your Religion ', 'Christianity', 'Islam', 'Judaism', 'Hinduism', 'Other'), font=('arial', 17, 'bold'))  # , textvariable=gender, width=19)
    Text_Entry_religion.grid(row=7, column=3, padx=10, pady=5)


    saveButton = tk.Button(window, text = "Save Information", command=lambda:saveInformation(college, Text_Entry_adm_no,Text_Entry_name ,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion  ))
    saveButton.grid(row=9, column =1, padx=10, pady=5)

    clearButton = tk.Button(window, text="Clear", command=lambda: clearInformation(Text_Entry_adm_no, Text_Entry_name ,Text_Entry_Father_Name , Text_Entry_father_job , Text_Entry_date_of_birth , Text_Entry_course ,Text_Entry_mobile_no, Text_Entry_landline_no , Text_Entry_address , Text_Entry_admission , Text_Entry_last_name ,Text_Entry_mother_name , Text_Entry_mother_job  ,  v , Text_Entry_section , Text_Entry_blood_group , Text_Entry_religion  ))
    clearButton.grid(row=9, column=2, padx=10, pady=5)

    back_button = tk.Button(window, text="Back", command=lambda:callback(window, college))
    back_button.grid(row=9, column=3, padx=10, pady=5)

    exit_button = tk.Button(window, text="Exit", command=lambda:exit(college, window))
    exit_button.grid(row=9, column=4, padx=10, pady=5)

    update_button = tk.Button(window, text="Update / Delete", command=lambda: update(window , college))
    update_button.grid(row=10, column=1, padx=10, pady=5)



    window.mainloop()


# code to be exectued when run from this script
if __name__ == "__main__":
    print("Code executing from same file")
    #college = College()
    #gui()

# new screen when you click update and it should have search student button and update info and
#then search the student and all their info should appear and then you change it with get and set method
# click update info to set it. then write file method

# create remove student where search student and delete student student form the list , show pop up that the student name and info is deleted