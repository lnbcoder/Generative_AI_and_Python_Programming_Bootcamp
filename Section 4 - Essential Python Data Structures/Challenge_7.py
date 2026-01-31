# Write a Python script that extracts the first and
# last two characters from a user-entered string.
# Example:
# Input: 'Hello!'
# Output: 'Heo!'

word = input('Enter string: ')
new_word = word[:2] + word[-2:]
print(new_word)