class PersonalInfo:
    def __init__(self, first_name,  date_of_birth, course, mobile_no,
                 address, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.course = course
        self.mobile_no = mobile_no
        self.address = address
        self.gender = gender

    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_date_of_birth(self):
        return self.date_of_birth
    def get_course(self):
        return self.course
    def get_mobile_no(self):
        return self.mobile_no
    def get_address(self):
        return self.address
    def get_gender(self):
        return self.gender

    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
    def set_course(self, course):
        self.course = course
    def set_mobile_no(self, mobile_no):
        self.mobile_no = mobile_no
    def set_address(self, address):
        self.address = address
    def set_gender(self, gender):
        self.gender = gender



    def __str__(self):
        return 'First Name : ' + self.first_name + '\nLast Name : ' + self.last_name + '\nDate of Birth : ' + self.date_of_birth + '\nCourse : ' + self.course + '\nMobile Number : ' + self.mobile_no + '\nAddress : ' + self.address + '\nGender : ' + self.gender
class Staff(PersonalInfo):
    def __init__(self, first_name, qualification , subject ,date_of_birth , course ,
                 mobile_no , address ,last_name, email_address , salary , gender):
        super().__init__(first_name, date_of_birth, course, mobile_no,
                              address, last_name, gender)
        self.qualification = qualification
        self.email_address = email_address
        self.subject = subject
        self.salary = salary

    def get_qualification(self):
        return self.qualification

    def get_email_address(self):
        return self.email_address

    def get_subject(self):
        return self.subject

    def get_salary(self):
        return self.salary

    def set_qualification(self, qualification):
        self.qualification = qualification

    def set_email_address(self, email_address):
        self.email_address = email_address
    def set_subject(self, subject):
        self.subject = subject
    def set_salary(self, salary):
        self.salary = salary



    def __str__(self):
        #print(self.first_name)
        #print(self.last_name)
        #print(self.qualification)
        #print(self.subject)
        #print(self.date_of_birth)
        #print(self.course)
        #print(self.mobile_no)
        #print(self.address)
        #print(self.email_address)
        #print(self.salary)
        #print(self.gender)


        return  super().__str__() + '\nQualification:  ' + self.qualification + '\nSubject :  ' + self.subject + '\nEmail Address:  ' + str(self.email_address) + '\nSalary : ' + str(self.salary)


class Student(PersonalInfo):
    # initialize class variable
    #count_student = 0
    def __init__(self,admission_number , first_name, father_name, father_job, date_of_birth, course, mobile_no, landline_no, address,
                 admission, last_name, mother_name, mother_job, gender, section, blood_group, religion):
        super().__init__(first_name,  date_of_birth, course, mobile_no, address, last_name, gender)
        self.adm_no = admission_number
        self.father_name = father_name
        self.father_job = father_job
        self.landline_no = landline_no
        self.admission = admission
        self.mother_name = mother_name
        self.mother_job = mother_job
        self.section = section
        self.blood_group = blood_group
        self.religion = religion
        self.fees_list = [] # composition every student has their own fees and differnt fees to pay for each semester
        #Student.count_student = Student.count_student + 1
        #print("Class variable: ",Student.count_student)
        #self.srno = Student.count_student # we created this variable  we can keep the serial number for each student and as soon as a nother student is added it goes up 1
        self.exam_list = [] # each student can have multiple exam results
    def add_fees(self ,fees): # this method is going to add all the sperate fees in the list we created holding all the fees for the student
        self.fees_list.append(fees)
        print("Fees added")

    def add_exams(self,exams):  # this method is going to add all the sperate fees in the list we created holding all the fees for the student
        self.exam_list.append(exams)
        print("exam added")



    def get_father_name(self):
        return self.father_name

    def get_father_job(self):
        return self.father_job

    def get_landline_no(self):
        return self.landline_no

    def get_admission(self):
        return self.admission

    def get_mother_name(self):
        return self.mother_name

    def get_mother_job(self):
        return self.mother_job

    def get_section(self):
        return self.section

    def get_blood_group(self):
        return self.blood_group

    def get_religion(self):
        return self.religion

    def get_fees_list(self):
        return self.fees_list


    def get_adm_no(self):
        return self.adm_no

    # returning str of all exams
    def get_exam_list(self):
        value1 = ''
        for each in self.exam_list:
            value1 = value1 + each.__str__()  # calling the str function from the staff class by calling object each and each is the staff object
        return value1

    # returning objects of all exams
    def getAllExams(self):
        return self.exam_list
    def set_father_Name(self, father_name):
        self.father_name = father_name
    def set_father_job(self, father_job):
        self.father_job = father_job
    def set_landline_no(self, landline_no):
        self.landline_no = landline_no
    def set_admission(self, admission):
        self.admission = admission
    def set_mother_name(self, mother_name):
        self.mother_name = mother_name
    def set_mother_job(self, mother_job):
        self.mother_job = mother_job
    def set_section(self, section):
        self.section = section
    def set_blood_group(self, blood_group):
        self.blood_group = blood_group
    def set_religion(self, religion):
        self.religion = religion
    def set_fees_list(self, fees_list):
        self.fees_list = fees_list
    def set_adm_no(self, adm_no):
        self.adm_no = adm_no
    def set_exam_list(self, exam_list):
        self.exam_list = exam_list
    def findFees(self, semester):
        for each in self.fees_list:
            if semester == each.get_semester():
                return each # returning particular fees object of selected semester
        return None
    def findExams(self , subject , semester):
        for each in self.exam_list:
            print(each.get_subject(), subject)
            print(each.get_semester(), semester)
            if subject == each.get_subject() and semester == each.get_semester():
                return each
        return None

#[fees1, fees2]
    def __str__(self):
        value = ''
        for each in self.fees_list:
            value = value + each.__str__()  # calling the str function from the staff class by calling object each and each is the staff object
        print("Fees: ",value)
        value1 = ''
        for each in self.exam_list:
            value1 = value1 + each.__str__()  # calling the str function from the staff class by calling object each and each is the staff object
        print("Exams: ", value1)
        return  '\nAdmission Number: ' + str(self.adm_no) + '\n' + super().__str__() + '\nFather Name:  ' + self.father_name + '\nFather Job :  ' + self.father_job + ' \nLandline Number :  ' + str(self.landline_no) +  '\nAdmission: ' + str(self.admission) + '\nMother Name : ' + self.mother_name + '\nMother Job : ' + self.mother_job  + '\nSection : ' + self.section + '\nBlood Group : ' + self.blood_group + '\nReligion : ' + self.religion + value + '\n\n' +  value1 +  '\n\n'


class Fees:
    def __init__(self , search ,total_fee , semester , paid , paid_date ,mode_of_payment ,due_amount):
        self.search = search
        self.total_fee = total_fee
        self.semester = semester
        self.paid = paid
        self.paid_date = paid_date
        self.mode_of_payment = mode_of_payment
        self.due_amount = due_amount

    def get_search(self):
            return self.search

    def get_total_fee(self):
            return self.total_fee

    def get_semester(self):
            return self.semester

    def get_paid(self):
            return self.paid

    def get_paid_date(self):
            return self.paid_date

    def get_mode_of_payment(self):
            return self.mode_of_payment

    def get_due_amount(self):
            return self.due_amount

    def set_search(self, search):
        self.search = search
    def set_total_fee(self, total_fee):
        self.total_fee = total_fee
    def set_semester(self, semester):
        self.semester = semester
    def set_paid(self, paid):
        self.paid = paid
    def set_paid_date(self, paid_date):
        self.paid_date = paid_date
    def set_mode_of_payment(self, mode_of_payment):
        self.mode_of_payment = mode_of_payment
    def set_due_amount(self, due_amount):
        self.due_amount = due_amount


    def __str__(self):
        return '\nFees Details : ' +  '\n\tTotal Fee : ' + self.total_fee + '\n\tSemester : ' + self.semester + '\n\tPaid : ' + self.paid + '\n\tPaid Date : ' + self.paid_date + '\n\tMode of Payment :' + self.mode_of_payment + '\n\tDue Amount : ' + self.due_amount
# what is the relationship between college and student and college and staff


class Exam:
    def __init__(self , marks , total_marks , percentage , semester, subject ):
        self.marks = marks
        self.total_marks = total_marks
        self.percentage = percentage
        self.subject = subject
        self.semester = semester

    def get_marks(self):
        return self.marks
    def get_total_marks(self):
        return self.total_marks
    def get_percentage(self):
        return self.percentage
    def get_subject(self):
        return self.subject
    def get_semester(self):
        return self.semester

    def set_marks(self , marks):
        self.marks = marks
    def set_total_marks(self , total_marks):
        self.total_marks = total_marks
    def set_percentage(self , percentage):
        self.percentage = percentage
    def set_subject(self , subject):
        self.subject  = subject
    def set_semester(self , semester):
        self.semester = semester


    def __str__(self):
        return '\nExam Information : ' +  '\n\tMarks : ' + self.marks + '\n\tTotal Marks : ' + self.total_marks + '\n\tPercentage : ' + self.percentage
class Attendance:
    def __init__(self , name , ttl_no_days , type , no_days_present , no_days_absent , adm_no , to):
        self.name = name
        self.ttle_no_days = ttl_no_days
        self.type = type
        self.no_days_present = no_days_present
        self.no_days_absent = no_days_absent
        self.adm_no = adm_no
        self.to = to

    def __str__(self):
        return  '\nStudent Attendance : ' + '\nName : ' + self.name + '\nTotal number of days : ' + self.ttle_no_days + '\Type : ' + self.type + '\nNumber of days present : ' + self.no_days_present + '\nNumber of days absent : ' + self.no_days_absent + '\nAdmission Number : ' + self.adm_no + '\nTo : ' + self.to




#update uml diagram

# check relationship between total , due amount , paid
# checks on these 3 after relationship
# make screen fro just attendace , fees , exam details : only student number , semester , subject , fees should only be semesterand details