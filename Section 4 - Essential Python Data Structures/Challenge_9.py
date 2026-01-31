# Write a Python program to remove the character at the nth index from a non-empty string.
# The nth index is provided by the user.
sentence = 'Learning Python Programming'
index = int(input('Enter the index of the char you want to remove: '))
first_part = sentence[0:index]
last_part = sentence[index+1:]
new_sentence = first_part + last_part
print(new_sentence)