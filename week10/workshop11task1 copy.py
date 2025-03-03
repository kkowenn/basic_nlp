import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

with open('The_Adventures_of_Sherlock_Holmes.txt', 'r') as file:
    Sherlock_Holmes_doc = file.read()

# print(Sherlock_Holmes_doc)

doc = nlp(Sherlock_Holmes_doc)

# Extract noun chunks and count their frequencies
noun_chunks = [chunk.text for chunk in doc.noun_chunks]
top_20_noun_chunks = Counter(noun_chunks).most_common(20)

for chunk, frequency in top_20_noun_chunks:
    print(f"{chunk}: {frequency}")

