class Student: #Creating a class named Student
    def __init__(self, name, major, gpa): #Declaing an init function to assign values as attributes to Object Students
        self.name = name
        self.major = major
        self.gpa = gpa

    def honor_roll(self): # Class function named honor_roll with the parameter self
        if self.gpa >= 3.5: # If statement checking to see if the gpa of a Object Student is greater than or equal to 3.5
            return True #If so, it returns True
        else:
            return False #If not, it returns false.