import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

encoding = 'ISO-8859-1'
# for debugging: ValueError: [E088] Text of length 1109179 exceeds maximum of 1000000. The parser and NER models require roughly 1GB of temporary memory per 100,000 characters in the input. This means long texts may cause memory allocation errors. If you're not using the parser or NER, it's probably safe to increase the `nlp.max_length` limit. The limit is in number of characters, so you can check whether your inputs are too long by checking `len(text)`.
nlp.max_length = 1500000

with open('Harry_Potter_1_Sorcerers_Stone.txt', 'r', encoding=encoding) as file:
    harry1 = file.read()

with open('Harry_Potter_2-The_Chamber_of_Secrets.txt', 'r', encoding=encoding) as file:
    harry2 = file.read()

with open('Harry_Potter_3_Prisoner_of_Azkaban.txt', 'r', encoding=encoding) as file:
    harry3 = file.read()

with open('Harry_Potter_4_The_Goblet_of_Fire.txt', 'r', encoding=encoding) as file:
    harry4 = file.read()

harry1 = nlp(harry1)
harry2 = nlp(harry2)
harry3 = nlp(harry3)
harry4 = nlp(harry4)

def extract_top_characters(doc, num=10):
    entities = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    return Counter(entities).most_common(num)

def extract_top_places(doc, num=15):
    entities = [ent.text for ent in doc.ents if ent.label_ in 'LOC']
    return Counter(entities).most_common(num)

# Extract named entities for each book
top_characters_book1 = extract_top_characters(harry1)
top_characters_book2 = extract_top_characters(harry2)
top_characters_book3 = extract_top_characters(harry3)
top_characters_book4 = extract_top_characters(harry4)

top_places_book1 = extract_top_places(harry1)
top_places_book2 = extract_top_places(harry2)
top_places_book3 = extract_top_places(harry3)
top_places_book4 = extract_top_places(harry4)

# Print leading characters and important places
print("Leading Characters in Book 1:")
print("----------------------------------------------------------------")
print(top_characters_book1)
print("----------------------------------------------------------------")
print("\nImportant Places in Book 1:")
print("----------------------------------------------------------------")
print(top_places_book1)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
print("\nLeading Characters in Book 2:")
print("----------------------------------------------------------------")
print(top_characters_book2)
print("----------------------------------------------------------------")
print("\nImportant Places in Book 2:")
print("----------------------------------------------------------------")
print(top_places_book2)


print("----------------------------------------------------------------")
print("\nLeading Characters in Book 3:")
print("----------------------------------------------------------------")
print(top_characters_book3)
print("----------------------------------------------------------------")
print("\nImportant Places in Book 3:")
print("----------------------------------------------------------------")
print(top_places_book3)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
print("\nLeading Characters in Book 4:")
print("----------------------------------------------------------------")
print(top_characters_book4)
print("----------------------------------------------------------------")
print("\nImportant Places in Book 4:")
print("----------------------------------------------------------------")
print(top_places_book4)
print("----------------------------------------------------------------")
