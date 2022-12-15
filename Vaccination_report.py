import datetime
d = datetime.datetime.now()
print(d)

import os
f = open(r"C:\\Users\\HETVI\\OneDrive\\Documents\\GitHub\\python_practicals\\Assignment_work\\vaccinceReport.txt","r")
print(f.read())



first_name = input("enter your firstname:")
last_name = input("enter your lastname:")
age = int(input("enter your age:"))
gender = input("enter your gender:")
vaccine = input("enter your vaccine name :")
vaccine_doze = int(input("enter your doze:"))



print("----------------------")
print("first name :",[first_name])
print("last name :",[last_name])
print("age :",[age])
print("gender :",[gender])
print("vaccine :",[vaccine])
print("vaccine doze :",[vaccine_doze])
#f.write