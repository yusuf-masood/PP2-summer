# 1
import math

#Degree
degree = 15

#Convert degrees to radians
radian = degree * (math.pi / 180)

print("Input degree:", degree)
print("Output radian:", radian)

# 2
height = 5
base1 = 5
base2 = 6

# Calculation of  the area of the trapezoidal
area = 0.5 * (base1 + base2) * height

print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area)


# 3
num_sides = 4
side_length = 25

#Calculation of  the area of the regular polygon
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

print("Input number of sides:", num_sides)
print("Input the length of a side:", side_length)
print("The area of the polygon is:", area)


# 4
base_length = 5
height = 6

# Calculate the area of the parallelogram
area = base_length * height

# Output the result
print("Length of base:", base_length)
print("Height of parallelogram:", height)
print("Expected Output:", float(area))
