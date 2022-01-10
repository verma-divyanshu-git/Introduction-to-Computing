#question 4
student1_marks=int(input("Student 1 marks: " ))
student2_marks=int(input("Student 2 marks: " ))
student3_marks=int(input("Student 3 marks: " ))
student4_marks=int(input("Student 4 marks: " ))
student5_marks=int(input("Student 5 marks: " ))
list=[student1_marks, student2_marks, student3_marks, student4_marks, student5_marks]
#to sort list we will use an inbuilt function : sort
list.sort()
print("Sorted list is: ",list)
