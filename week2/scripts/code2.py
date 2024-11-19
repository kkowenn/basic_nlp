import re

# Input text
text = "I have so much fun. Yahoo! kwan@scitech.au.edu"

# Regex pattern for hashtags
hashtag_pattern = r'#\w+'
hashtags = re.findall(hashtag_pattern, text)

# Define regex pattern for email
email_regex = r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+'

# Remove emails from the text
cleaned_text = re.sub(email_regex, '', text)
print("Cleaned text:", cleaned_text)

# Split the cleaned text into words
words = cleaned_text.split()
print("Words:", words)

# Find all emails in the original text
emails = re.findall(email_regex, text)
print("Emails:", emails)
