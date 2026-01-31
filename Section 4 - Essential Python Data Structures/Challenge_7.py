# Write a Python script that replaces all occurrences of the first character in a
# string with '$', except for the first occurrence itself.
# Example:
# Input: 'mama'
# Output: 'ma$a'

word = input('Enter word: ')
first_char = word[0]
new_word = first_char + word[1:].replace(first_char, '$')
print(new_word)