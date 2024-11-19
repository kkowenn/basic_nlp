import re

# Sample input text
text = "I like CSX4210 CSX3001"

# Define the regex pattern for course codes
# [A-Za-z]{2,3} Matches 2 or 3 alphabetical characters
# [0-9]{4}: Matches exactly 4 digits.
course_pattern = r'[a-zA-Z0-9._]{2,3}[0-9]{4}'

# Find all course codes in the text
course_codes = re.findall(course_pattern, text)

# Print each course code on a new line
for code in course_codes:
    print(code)
