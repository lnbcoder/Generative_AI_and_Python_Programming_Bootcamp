# Write a Python script to check if a string is a palindrome.

my_str = input("Enter a word: ").lower()
reversed_str = my_str[::-1]
print(f"Is the word {my_str} a palindrome: {my_str == reversed_str}")