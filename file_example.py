"""
    r : read mode
    w : write mode
    a : append mode
"""
import os
#if ouput is not comming then write (r): raw string
#f = open(r"C:\Users\HETVI\OneDrive\Documents\GitHub\python_practicals\programs\9_june\example.txt","r")
#f = open("C:\\Users\\HETVI\\OneDrive\\Documents\\GitHub\\python_practicals\\Daily_work\\programs\\example.txt","r")

#print(f.read())(for read)

#----------------------------------------------------------------------------

#print(f.readline())
#readline : read the first line it will display one - one line

#l1 = f.readlines()

#print("------>",l1)
#print("no.of lines in file:",len(l1))

#print("3rd line of file",l1[1])

#-------------------------------------------------------------

#import os

#f = open("C:\\Users\\HETVI\\OneDrive\\Documents\\GitHub\\python_practicals\\Daily_work\\my_file_example.txt","w")

#f.write("\n my file practical")
#f.write("\n this file is created by me")
#f.write("\n hello all")

#f.close()

#-------------------------------------------------------------------------------------


#import os

#f = open("C:\\Users\\HETVI\\OneDrive\\Documents\\GitHub\\python_practicals\\Daily_work\\my_file_example.txt","a") #by writing (a) it will store old lines in file
#f.write("\n my python language")
#f.close()

#---------------------------------------------------------------------

#x : by writting x mode it will create blank file 
#create blank file

#f = open("C:\\Users\\HETVI\\OneDrive\\Documents\\GitHub\\python_practicals\\Daily_work\\myblankfile.txt","x")

#---------------------------------------------

#create folder
#os.mkdir ( TO CREATE FOLDER)

import os

if os.path.exists(r"C:\Users\HETVI\OneDrive\Documents\GitHub\python_practicals\Daily_work\\my_folder"):
    print("FOLDER ALREADY EXIST")
else:
    os.mkdir(r"C:\Users\HETVI\OneDrive\Documents\GitHub\python_practicals\Daily_work\my_folder")
    print("CREATED FOLDER")