#python work on top to bottom approach
#if you assign a variable some value and then change it later, the last value will be considered



print("chetanya")
age = 19
college = "jecrc" 
name = "chetanya"
is_student = False
print(name,"is",age,"years old and student:",is_student)
#here is a simple way to take input from user
name = input("enter your name:")
age = input("enter your age:")
college = input ("enter your college name:")
print (name,"is",age,"years old and studies at",college)
#if you want to take user input as integer
age = int(input("enter your age:"))
#if you want to take user input as float
height = float(input("enter your height in meters:"))
#now i am going to work on if , elif and else statements
#here we have used if else statements to check if the user is able to drink alcohol or not
if age >= 18:
    print (name,"you are able to drink alcohol")
else:
    print (name,"you are not able to drink alcohol")
#now i am gonna test for if , else ,and elif statements
if height >= 75:
    print (name,"how are you so tall")
elif height >= 50: 
    print (name,"you are tall man")
elif height >= 25:
    print (name,"you look damn good")
else:
    print (name,"ypu are to shart get out dwarf")
#now i am gonna check wether my birth year is even or odd
birth_year = int(input("enter your birth year:"))
if birth_year % 2 == 0:
    print("you were born in an even year")
else:
    print("you were born in an odd year")
#now i am gonna check wether my birth year is a leap year or not
if (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0):
    print("you were born in a leap year")
else:   
    print("you were not born in a leap year")
#now we gonna work on while and for loops
#while loop is used to repeat a block of code as long as the condition is true 
count = 0
while count <= 10:
    print ("count is :", count)
    count += 2
#here in the while loop we are printing the count value and incrementing it by 2 until it reaches 10
#here i am gonna use for loop to print the numbers from 0 to 10
for i in range(1,10):
    print("here is the number :", i)
#now i am gonna use for loop to print the numbers from 0 to 10 with step of 2
for i in range(0, 10, 2):
    print("here is the number with the step of two:", i)
#here inside the range function we have used 3 arguments, the first one is the starting point, the second one is the ending point and the third one is the step
#now i am gonna write no backwardd using for loop
for i in range (10, 0, -1):
    print ("here are the no backward:",i)
#now i am gonna use while loop to print no backward 
count =10
while count > 0:
    print("here are the no backward using while loop:", count)
    count -= 1
#here now i am gonna use for loop to print * from taking input  from the user
stars = int (input("no of starts you want to print:"))
for i in range (stars):
    print("*")
#here we gonna use while loop to print * from taking input from the user
stars = int(input("no of stars you want to print:"))
count = 0
while count < stars:
    print("*")
    count +=1
#next we are gonna jump to break  statement in for loop
for i in range(1, 10):
    if i == 5:
        break
    print("here are the no before break statement:", i)
#break statement is used to exit the loop when the condition is met
#now we are gonna use continue statement in for loop
for i in range(1 ,10):
    if i == 8:
        continue
    print("print no without 8;",i)
#continue statement is used to skip the current iteration of the loop when the condition is met
#we are gonna use break and continue statement in while loop
count = 0
while count < 10:
    if count == 5:
        break
    print("here are the no before break statement:", count)
    count += 1
#here we are using continue statement in while loop
count = 0
while count < 10:
    count += 1
    if count == 8:
        continue
    print("print no without 8:",count)
#in while loop we write exit statement in the end of the loop in break statement and normal while loop
#in while loop for writing continue statement we write it in the middle of the loop
#now  i am  gonna work on arithmetic operations
x = 10
x += 5
x //=3
print(x)
#i will use all basic operation in this code
num1 = float(input("enter the first no:"))
num2 = float(input("enter the second no:"))
print("addition",num1 + num2)
print("subtraction",num1-num2)
print("multiplication",num1 * num2)
print("division", num1/num2)
print("modulus(remainder)",num1%num2)
print("exponential(power)",num1**num2)
#now we are working on file handling
#here r means read, w means write, a means append(add to end), x means create a new file, r+ means read and write
#i am gonna writing to a file
file = open("myfile.txt","w")
file.write("hello chetanya\n")
file.write("i will handle this file\n")
file.close()
#now i am gonna read the file
file = open("myfile.txt", "r")
content = file.read()
print("file content:")
print(content)
file.close()
#now i am gonna append to the file
file = open("myfile.txt","a")
file.write("this line is added later to this file")
file.close()
#now i am gonna read the file again to see the changes
#here this read function reads the entire content of the file after appending
file = open("myfile.txt", "r")
content = file.read()
print("file content after appending:")
print(content)
file.close()
#now i am gonna create a folder called data and then move into it and then create a file with my name and list all the files
#this is the os module which is used to interact with the operating system

import os

# Show the current working directory
print("Current directory:", os.getcwd())

# Step 1: Check and create the folder if missing
folder_path = os.path.join(os.getcwd(), "data")

if not os.path.exists(folder_path):
    print("Folder 'data' not found. Creating it...")
    os.mkdir(folder_path)
else:
    print("Folder 'data' already exists.")

# Step 2: Create the file safely
file_path = os.path.join(folder_path, "chetanya.txt")
print("Creating file at:", file_path)

with open(file_path, "w") as file:
    file.write("this is my file inside a folder")

print("✅ File written successfully!")
#now we move up to the sys module
#in sys module we can use sys.exit() to exit the program
#in sys module we interact with the command line arguments
# in sys module we can acess the command line arguments using sys.argv
#most useful things in sys are sys.argv means getcommand line arguments, sys.exit() means exit the program, sys.path means get the path of the python interpreter , sys.version means get the version of the python interpreter
#use sys to print python version
import sys
print("\nyour python version is:", sys.version)
#use of sys to use command line argument i.e sys.argv
print("\nall command line argument:", sys.argv)
if len(sys.argv)>1:
    #here this if len() statement will not work as i have not passed argument inside the script as we have to pass them when running the script from the terminal 
    #here len is the build in function in python that return the no of items in a list , string or other collection
    #here is how i run it by writing command in cmd prompt i.eC:\Users\cheta\OneDrive\Desktop\chetanya python>"C:\Users\cheta\AppData\Local\Programs\Python\Python313\python.exe" basic.py chetanya 19 
    print("\nfirst argument",sys.argv [1])
else:
    print("\nno extra argument passed. ")
#use of sys to exit the program
print("\nthis will run")
#sys.exit()
print("\nthis will not run")
#sys.exit() ends the program immediately any code after it wont't run
#accept multiple arguments
import sys
print("\nall command line argument:", sys.argv)
#i am gonna use loop to print all the command line arguments using for loop
# Loop through arguments starting from index 1 (skip script name at index 0)
for i in range(1,len(sys.argv)):
    print("arguments are {i}:",sys.argv[i])    

    
    
    
    
    


