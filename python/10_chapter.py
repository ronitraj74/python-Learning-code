class Employee:
    language = "python"
    salary = 12000000
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

ronit = Employee()
ronit.language = "java" #This is an instance attribute 
ronit.getInfo()
#Employee.getInfo(ronit)