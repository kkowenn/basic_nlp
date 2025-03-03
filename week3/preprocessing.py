import nltk
from nltk.corpus import reuters
from collections import Counter

# Download required NLTK data (only needs to be done once)
nltk.download('reuters')
nltk.download('punkt')

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

word_list = ["play", "played", "playing", "is", "am", "are", "be","mice","mouse"]

lemmatizer = WordNetLemmatizer()

lemma_verbs = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in word_list]
print(lemma_verbs)

lemma_nouns = [lemmatizer.lemmatize(word, pos=wordnet.NOUN) for word in word_list]
print(lemma_nouns)

