'''
Challenge #1

A company has a revenue of 45,897,513.
Calculate its profit, assuming profit is 12.7% of the revenue.
Display the result rounded to two decimal places.
'''

revenue = 45897513
percentage = 12.7 / 100
profit = f'{revenue * percentage:.2f}'
print(f'Tha profit is {profit}')