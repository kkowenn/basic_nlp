import nltk
from nltk.corpus import reuters
from collections import Counter

# Download required NLTK data (only needs to be done once)
nltk.download('reuters')
nltk.download('punkt')

# Load the Reuters corpus
words = reuters.words()

# Count word frequencies using Counter
word_counts = Counter(words)

# Calculate the total number of words
total_words = sum(word_counts.values())

# Calculate word probabilities and store them in a list
word_probabilities = []
for word, count in word_counts.items():
    probability = count / total_words
    word_probabilities.append((word, probability))

# Sort the list by probability in descending order
word_probabilities.sort(key=lambda x: x[1], reverse=True)

# top 20 words
top_20 = [word for word, prob in word_probabilities[:20]]

print(top_20)
