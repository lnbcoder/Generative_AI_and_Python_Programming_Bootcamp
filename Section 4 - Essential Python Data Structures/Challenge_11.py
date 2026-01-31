# Write a Python script that prompts the user for a circle's radius and calculates its area.
# Formula: Area = π * r² (π = 3.1415)
# Display the area with four decimal places using an f-string.

radius = float(input("Enter a circle's radius: "))
area = 3.1415 * radius ** 2
print(f'The area of the circle is: {area:.4f}')