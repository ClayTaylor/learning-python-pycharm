
#open("read.txt", "r") # Reading the File Only
#open("read.txt", "w") # Writing the File Only
#open("read.txt", "a") # Appending information to the end of the File Only
#open("read.txt", "r+") # Reading and Writing on the File

employee_file = open("read.txt", "r") #Creating a variable that will open the file 'read.txt' and declaring that I want to read it only - 'r'.

#print(employee_file.readable()) #Checking to see if a file is readable before I even try to do anything with it
#print(employee_file.readlines()[1]) #Printing out an individual line in the file.
for employee in employee_file.readlines(): #For loop named employee that loops over employee_file and reads all the lines.
    print(employee) #After looping over the lines, each line is printed out.

employee_file.close() #Closing the File. If I open a file to access the data, I want to make sure I am closing the file.
