'''Paint Calculator
Calculate the number of gallons needed to paint the ceiling of a room. 
Prompt the user for length and width and assume 1 gallon covers 350 
square fee. Display the number of gallons needed to paint the ceiling
as whole number. 
'''

import math

width = float(input("Please enter the width of the ceiling: "))
length = float(input("Please enter the length of the ceiling: "))
area = width * length

gallons = math.ceil(area / 350) #Purchasing whole gallons requires rounding up.

print(f"You will need to purchase {gallons} gallons of paint to cover {area} square feet.")
