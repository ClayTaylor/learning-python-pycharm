

# employee_file = open("office.txt", "a") #Opening the office.txt file and Appending it (adding to the end of it).
# employee_file.write("\nKelly - Customer Service") #Writing to the file with a new line and inserting a new Employee named 'Kelly - Customer Service'
# print(employee_file) #Printing out the entire employee_file
# employee_file.close() #Closing the office.txt

employee_file = open("office.txt", "w") #Operning the office.txt file and writing to it. Writing to a file will delete any previous information on the file and will overwrite it with the new information.
#employee_file = open("office1.txt", "w") # Creates a new file to be written on.
employee_file.write("Kelly - Customer Services") #Writing to the file with a new line and inserting a new employee named 'Kelly - Customer Service'.
print(employee_file) # Printing out the file
employee_file.close() # Closing the file
