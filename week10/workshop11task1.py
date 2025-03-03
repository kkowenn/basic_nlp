import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

with open('The_Adventures_of_Sherlock_Holmes.txt', 'r') as file:
    Sherlock_Holmes_doc = file.read()

def count_noun_chunks(doc):
    return len(list(doc.noun_chunks))

def extract_top_noun_chunks(doc, num=20):
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    return Counter(noun_chunks).most_common(num)

def extract_entities(doc, label, num=10):
    entities = [ent.text for ent in doc.ents if ent.label_ == label]
    return Counter(entities).most_common(num)

# print(Sherlock_Holmes_doc)
doc = nlp(Sherlock_Holmes_doc)

length = count_noun_chunks(doc)
top_20_noun_chunks = extract_top_noun_chunks(doc)
top_10_persons = extract_entities(doc, 'PERSON')
top_10_orgs = extract_entities(doc, 'ORG')
top_10_locations = extract_entities(doc, 'GPE')

print("----------------------------------------------------------------")
print("Length of noun chunks:")
print("----------------------------------------------------------------")
print(f"Number of noun chunks: {length}")
print("----------------------------------------------------------------")
print("Top 20 Noun Chunks:")
print("----------------------------------------------------------------")
for chunk, frequency in top_20_noun_chunks:
    print(f"{chunk}: {frequency}")
print("----------------------------------------------------------------")
print("Top 10 Persons:")
print("----------------------------------------------------------------")
for person, frequency in top_10_persons:
    print(f"{person}: {frequency}")
print("----------------------------------------------------------------")
print("Top 10 Organizations:")
print("----------------------------------------------------------------")
for org, frequency in top_10_orgs:
    print(f"{org}: {frequency}")
print("----------------------------------------------------------------")
print("Top 10 Locations:")
print("----------------------------------------------------------------")
for location, frequency in top_10_locations:
    print(f"{location}: {frequency}")
print("----------------------------------------------------------------")
