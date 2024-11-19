import re

# Regular expressions
regex_alphabetic = r'^[a-zA-Z]+$'
regex_lowercase_b = r'^[a-z]*b$'
regex_ab_bounded = r'^b*(ab)+b*$'

# Test strings
test_strings = ["HelloWorld", "abcde", "worldb", "ab", "bab", "aa", "bb", "baba", "abab"]

def validate_strings(regex, strings):
    return [s for s in strings if re.match(regex, s)]

# Validate alphabetic strings
alphabetic_strings = validate_strings(regex_alphabetic, test_strings)
print("Alphabetic strings:", alphabetic_strings)

# Validate lowercase alphabetic strings ending with 'b'
lowercase_b_strings = validate_strings(regex_lowercase_b, test_strings)
print("Lowercase strings ending with 'b':", lowercase_b_strings)

# Validate strings from {a, b} with 'a' bounded by 'b'
ab_bounded_strings = validate_strings(regex_ab_bounded, test_strings)
print("Strings with each 'a' bounded by 'b':", ab_bounded_strings)
