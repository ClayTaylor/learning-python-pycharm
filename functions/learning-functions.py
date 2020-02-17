
# def sayhi (name, age):
#    print("Hello " + name + ", you are " + age + ".")

# sayhi("Clay", "25")
# sayhi("John", "70")

# Step 1: Tell Python I am wanting to define a function
# Step 2: Give the function a name
# Step 3: Define any parameters that I would like to give/pass to the function.
# Step 4: Write the code inside the function.
# Step 5: Call the function with its name and pass the information to the paramenters previously defined in the function.



#Example

def today_date (month, day, year):
    print("Hello," + " today's date is " + month + " " + day +", " + year + ".")

# today_date("Feb", "17", "2020")
today_date(input("Month: "), input("Day: "), input("Year: "))