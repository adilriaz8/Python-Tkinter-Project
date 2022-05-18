class Student():
    def __init__(self, first_name, father_name, father_job ,date_of_birth , course , mobile_no , landline_no ,address , admission , last_name , mother_name , mother_job , gender , section , blood_group , religion ):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.father_job = father_job
        self.date_of_birth = date_of_birth
        self.course = course
        self.mobile_no = mobile_no
        self.landline_no = landline_no
        self.address = address
        self.admission = admission
        self.mother_name = mother_name
        self.mother_job = mother_job
        self.gender = gender
        self.section = section
        self.blood_group = blood_group
        self.religion = religion
    def __str__(self):
        return 'First Name : '+ self.first_name +'\nLast Name :  ' + self.last_name + '\nFather Name:  ' + self.father_name + '\nFather Job :  ' + self.father_job  + '\nDate of Birth :  ' + str(self.date_of_birth)  + '\nCourse :  ' + self.course  + '\nMobile Number:  ' + str(self.mobile_no)  + ' \nLandline Number :  ' + str(self.landline_no)  + '\nAddress :  ' + str(self.address)  + '\nAdmission:  ' + str(self.admission)  +'\nMother Name : '  +  self.mother_name  + '\nMother Job : ' +self.mother_job  + '\nGender : ' + str(self.gender)  +  '\nSection : ' + self.section  + '\nBlood Group : ' + self.blood_group  + '\nReligion : ' + self.religion