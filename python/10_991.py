class College:
    your_name = "Ronit" 
    college_name = "ACE"
    language = "Python"
    fees = 110001
    # your_name = input("Enter your name : ")
    # name = input("Enter the name of the college : ")
    # language = input("Enter the language used most in your college : ")
    # fees = int(input("Enter the semester wise fees of your college : "))

    def greet(grt):
        print(f"Good morning {grt.your_name}")

    def getInfo(info):
        print(f"The Name if the college is {info.college_name}.The Enviormental language in the college is {info.language} and The semester wise fees of the college is {info.fees}")

    def __init__(greet):
        print("Thank You")

    @staticmethod
    def you():
        print("hi")

information = College()
#information.language = "java"
information.greet()
information.getInfo()
