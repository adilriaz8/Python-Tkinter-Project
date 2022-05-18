class Staff:
    def __init__(self, first_name, qualification , subject ,date_of_birth , course , mobile_no , address ,last_name, email_address , salary , gender ):
        self.first_name = first_name
        self.last_name = last_name
        self.qualification = qualification
        self.subject = subject
        self.date_of_birth = date_of_birth
        self.course = course
        self.mobile_no = mobile_no
        self.address = address
        self.email_address = email_address
        self.salary = salary
        self.gender = gender
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

        return 'First Name : ' + self.first_name + '\nQualification:  ' + self.qualification + '\nSubject :  ' + self.subject + '\nDate of Birth :  ' + str(self.date_of_birth) + '\nCourse :  ' + self.course + '\nMobile Number:  ' + str(self.mobile_no) +  '\nAddress :  ' + str(self.address) + '\nLast Name:  ' + self.last_name + '\nEmail Address:  ' + str(self.email_address) + '\nSalary : ' + str(self.salary) + '\nGender : ' + self.gender