# Name - Divyanshu
# SID - 21103104


# QUESTION 1
string_1="Python is a case sensitive language" 
print("<a>Length of the string is : ",len(string_1)) #function to find LENGTH OF STRING
print("<b>The reversed string is : ",string_1[-1::-1])
# <c>
string_2=string_1[10:26] #Stored "a case sensitive" in a new string
# <d>
string_2.replace("a case sensitive","object oriented") #REPLACED "a case sensitive" WITH "object oriented"
print("<e>THE INDEX OF SUBSTRING a is : ",string_1.find('a'))
print("<f>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS : ",string_1.replace(" ",""))
print("\n")



#QUESTION 2
NAME=input("ENTER YOUR NAME ")
SID=int(input("ENTER YOUR SID "))
DEPARTMENT=input("ENTER YOUR DEPARTMENT ")
CGPA= float(input("ENTER YOUR CGPA "))
rounded_value = round(CGPA, 1) #because the cgpa to be printed is 9.9 and not 9.90000
print("Hey %s,"%NAME,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%DEPARTMENT,"and my CGPA is ",rounded_value)
print("\n")



#QUESTION 3
a=56
b=10
#a
print("a. ",a&b)
#b
print("b. ",a|b)
#c
print("c. ",a^b)
#d
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
#e
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print("\n")



#QUESTION 4
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))
 
if (number_1 > number_2) and (number_1 > number_3):
   largest = number_1
elif (number_2 > number_1) and (number_2 > number_3):
   largest = number_2
else:
   largest = number_3
 
print("THE LARGEST NUMBER IS ",largest)
print("\n")



#QUESTION 5
string = input("ENTER A STRING ")
if 'name' in string:
    print ("Yes")
else:
    print ("No")
print("\n")


#QUESTION 6
side_1=int(input("ENTER LENGTH OF FIRST SIDE OF TRIANGLE : "))
side_2=int(input("ENTER LENGTH OF SECOND SIDE OF TRIANGLE : "))
side_3=int(input("ENTER LENGTH OF THIRD SIDE OF TRIANGLE : "))
if(side_1>(side_2+side_3)):
    print("No")
elif(side_2>(side_1+side_2)):
    print("No")
elif(side_3>(side_1+side_2)):
    print("No")
elif(side_1 < 0 or side_2 < 0 or side_3 < 0)
    print("No")
#All sides should be positive and sum of any two sides should be greater than the third side : Condition to form a triangle
else:
    print("Yes")
print("\n")
