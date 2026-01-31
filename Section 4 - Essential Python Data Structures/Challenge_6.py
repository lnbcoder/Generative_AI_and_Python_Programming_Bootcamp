# Change the solution of the previous challenge to ignore whitespace
# and letter case when checking if a string is a palindrome.

my_str = input("Enter a word: ").replace(' ','')
reversed_str = my_str[::-1]
print(f"Is the word {my_str} a palindrome: {my_str == reversed_str}")