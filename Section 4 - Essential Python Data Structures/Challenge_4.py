# Write a Python script to convert feet (ft) to centimeters (cm).
# Conversion: 1 ft = 30.48 cm
# Prompt the user to enter a value in feet.
# Display the result in centimeters with two decimal places, formatted using an f-string.

feet = input('Enter ft to convert to centimeters: ')
centimeters = int(feet) * 30.48
print(f'{feet}ft to centimeters is {centimeters:.2f}')
