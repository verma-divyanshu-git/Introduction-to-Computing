#QUESTION 4

print("Ans 4 ")
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Divyanshu", 21103104)
print("Object created")
#printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.roll_no}.")
#deleting object
del student1
print("\n")
