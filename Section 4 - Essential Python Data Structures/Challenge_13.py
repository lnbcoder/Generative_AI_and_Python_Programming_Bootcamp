# Write a Python script to format a number using:
# US/UK format: A comma , as the thousands separator
# EU format: A period . as the thousands separator
# Example:
# Input: 1234567
# Output: 1,234,567 (US/UK) and 1.234.567 (EU)

number =  1234567
thousands_separator = f'{number:,}'
us_uk_format = thousands_separator
eu_format =  us_uk_format.replace(',','.')
print(f'{us_uk_format} (US/UK) and {eu_format}')

