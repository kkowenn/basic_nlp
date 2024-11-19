import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello Mr.Kritsada. We've got a mission for you. Here're the details."

sentences = sent_tokenize(text)
print("sent_tokenize")
print(sentences)
print(len(sentences))


print("word_tokenize")
words = word_tokenize(text)
print(words)
print(len(words))



