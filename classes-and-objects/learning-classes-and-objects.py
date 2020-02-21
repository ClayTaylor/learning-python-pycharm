
#Classes are used to define your own data type.

from student import Student # From the Student File (student.py), import the Student Class.

student1 = Student("Dalty", "Business", 3.2, False) #Object, student1, created from the Class (Student), from the file student.py with specific attributes that make up this particular student object.
student2 = Student("Jordan", "Nursing", 2.8, False)
student3 = Student("Andrew", "General Education", 4.0, True)
print(student3.gpa)