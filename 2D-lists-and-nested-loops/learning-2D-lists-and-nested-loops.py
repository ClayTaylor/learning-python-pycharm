
#2D Lists

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# print(number_grid[2][1]) // Parsing out individual elements within 2D Lists

for row in number_grid: # For loop named row looping through List number_grid
    for column in row: # Nested For Loop inside the above for loop lopping through the columns in the row
        print(column) #Printing out each value in each column in each row
