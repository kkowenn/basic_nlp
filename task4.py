import re
import csv
from collections import Counter

# Sample input text
text = "I take CSX4210, CSX3009 and CSX3010 but my best friend takes CSX3007, CSX4210, and CSX4110 this semester."

# Define the regex pattern for course codes
# [A-Za-z]{2,3} Matches 2 or 3 alphabetical characters
# [0-9]{4}: Matches exactly 4 digits.
course_pattern = r'[a-zA-Z0-9._]{2,3}[0-9]{4}'

# Find all course codes in the text
course_codes = re.findall(course_pattern , text)

'''
# Print each course code on a new line
for code in course_codes:
    print(code)
'''
# Count the frequency of each course code
course_code_frequency = Counter(course_codes)

# Sort the course codes by code
sorted_course_codes = sorted(course_code_frequency.items())

# Save the course codes and their frequency to a CSV file
with open('course_codes.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Header
    csvwriter.writerow(['Course Code', 'Frequency'])
    # Body
    for code, frequency in sorted_course_codes:
        csvwriter.writerow([code, frequency])

# Display output
print("Sample Output in CSV:")
for code, frequency in sorted_course_codes:
    print(f"{code}, {frequency}")

