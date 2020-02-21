
class Student:
   def __init__(self, name, major, gpa, is_on_probation): #Taking the values passed in and assigning them as attributes to the Object.
       self.name = name
       self.major = major
       self.gpa = gpa
       self.is_on_probation = is_on_probation

#In order for the Object (Student in this case) to have any attributes, we first have to tell Python to assign these attributes to the Object in the first place.
#When calling Student, this initialize function is executed and any values passed into the Object (in learning-classes-and-objects.py) are now stored as attributes of the Object.

# Example

# studentClay = Student("Clay", "Python", 4.0, False")
# This information is now coming over into this file, student.py, and since I called Student(), then the parameters entered are recognizing the values I entered, and attaching them as attributes
# to studentClay.

