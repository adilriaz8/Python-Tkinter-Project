import pickle
import mysql.connector



class College:
    def __init__(self):
        # concept of composition is implemented here as college class has other object/objects as its
        # instance variable
        self.__staff_list = [] # staff_list is the collection of Staff class objects
        self.__student_list = [] # student_list is the collection of student class objects
        try:
            f = open('student_information.pickle', 'rb')
            self.__student_list = pickle.load(f)
            print("Student Information Loaded Successfully!")
            for each in self.__student_list:
                print(each)
                print()
            f.close()
        except:
            print("File doesnt found")

        try:
            f = open('staff.pickle', 'rb')
            self.__staff_list = pickle.load(f)
            print("Staff Information Loaded Successfully!")
            for each in self.__staff_list:
                print(each)
                print()
            f.close()
        except:
            print("File doesnt found")
    def getAllStudent(self):
        return self.__student_list
    def getAllStaff(self):
        return self.__staff_list
    def add_student(self , student): #student is the object of the class
        self.__student_list.append(student)

    def remove_student(self , student):
        self.__student_list.remove(student)
    def add_staff(self , staff):# staff is the object of the class
        self.__staff_list.append(staff)

    def get_student_list(self):
        #print("getting staff list")
        value = ''
        for each in self.__student_list:
            value = value + each.__str__() + "----------------"  # calling the str function from the staff class by calling object each and each is the staff object
            #print("----------------", value, "-------------")
        return value

    def get_staff_list(self):
        value = ''
        for each in self.__staff_list:
            value = value + each.__str__()     # calling the str function from the staff class by calling object each and each is the staff object
        return value
    def read_student_file(self):
        try:
            f = open('student_information.pickle', 'rb')
            self.__student_list = pickle.load(f)
            print("Student Information Loaded Successfully!")
            for each in self.__student_list:
                print(each)
                print()
            f.close()
        except:
            print("File doesnt found")

        try:
            f = open('staff.pickle', 'rb')
            self.__staff_list = pickle.load(f)
            print("Staff Information Loaded Successfully!")
            for each in self.__staff_list:
                print(each)
                print()
            f.close()
        except:
            print("File doesnt found")

    def write_student_file(self):
        f = open('student_information.pickle', 'wb')
        pickle.dump(self.__student_list, f)
        f.close()

    def write_staff_file(self):
        f = open('staff.pickle', 'wb')
        pickle.dump(self.__staff_list, f)
        f.close()

    def findStudent(self, studentName):
        for student in self.__student_list:
            if student.get_first_name() == studentName:
                return student
        return None

    def findStaff(self, staffName):
        for staff in self.__staff_list:
            if staff.get_first_name() == staffName:
                return staff
        return None



# fix this method for printing a line after each students info
#line must contain dots or dash (get_student_list)
#make getters and setters in each class
# update UML diagram with all new methods
# search code for implementing student search button in exam_gui and fees_gui
# also put a button for search in exam_gui and fees_gui

# 1/1/2022
# fix the errors (no duplicate values in fields during search or update)
# implement delete for exam
# copy this folder files into StudentManagementSystem2 to save this work
# then perform following tasks in StudentManagementSystemMongoDB files:
# connect to mongodb atlas
# read any collection and print records on console
'''
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM table_name')

for i in cursor:
    print(i)
'''