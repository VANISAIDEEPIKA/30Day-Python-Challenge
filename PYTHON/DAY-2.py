# Calculate area of a rectangle from user input

# Step 1: Get inputs from user (Strings!)
length_input = input("Enter the length of the rectangle: ")   #  STRING (user input is always a string)
width_input = input("Enter the width of the rectangle: ")     #  STRING

# Step 2: Check data types before converting
print("Type of length_input:", type(length_input))            #  DATA TYPE CHECK (STRING)
print("Type of width_input:", type(width_input))              #  DATA TYPE CHECK (STRING)

# Step 3: Convert strings to floats (Type Conversion)
length = float(length_input)                                   #   TYPE CONVERSION: STRING ➜ FLOAT
width = float(width_input)                                     #   TYPE CONVERSION: STRING ➜ FLOAT

# Step 4: Calculate area (Float arithmetic)
area = length * width                                          #   FLOATS + ARITHMETIC (Multiplication)

# Step 5: Boolean checks (Comparison operators)
is_square = length == width                                    #  BOOLEAN: Check if sides are equal
is_positive = area > 0                                         #  BOOLEAN: Check if area is positive

# Step 6: Show results (Printing different types)
print("Length:", length, "units")                             #  FLOAT + STRING (Output)
print("Width:", width, "units")                               #  FLOAT + STRING (Output)
print("Area:", area, "square units")                          #  FLOAT + STRING (Output)

# Step 7: Bonus boolean outputs
print("Is it a square?", is_square)                           #   BOOLEAN OUTPUT
print("Is the area positive?", is_positive)                   #   BOOLEAN OUTPUT
