#Latoya Richardson
#September 28th, 2023
#In this lab we will create arithmetic calculations to output the area of a rectangle. We will achieve this by using variables, the print command, arithmetic operators, and concatenations. 
# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)
height = int(input("Enter the height for the rectangle: ")) #height variable saves the height the user inputs and int() converts the input to an integer
width = int(input("Enter the width for the rectangle: ")) #width variable saves the width the user inputs and int() converts the input to an integer
area = height * width #area variable saves the product of height multiplied by width
print("The area of the rectangle you created is " + str(area)) #print command outputs the area of the retangle with the use of concatenation and str 
length = int(input("Enter the length for the rectangle: "))#length variable saves the length of the rectangle that user inputs int saves the rectangle as an integer
width2 = int(input("Enter the width for the rectangle: "))#width2 variable saves the width of the rectangle the user inputs int saves the rectangle as an integer
perimeter = 2*(length+width2) #perimeter variable calculates the perimeter of the rectangle by adding the length and with of the rectangle and then multiplying it by 2
print("The perimeter of the rectangle you created is " + str(perimeter)) #print command outputs the perimeter of the rectangle to the user 