# Write a Python script that counts the number of occurrences of a substring in
# a given string, ignoring letter case.
from idlelib.debugobj import myrepr

my_str = 'I am in pretoria at the moment and I will be in JHB soon.'.lower()
num_of_occur = my_str.count('in')
print(f'The substring "in" appears {num_of_occur} times in the sentence')