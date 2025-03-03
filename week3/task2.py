import nltk
from nltk.corpus import reuters
from nltk.util import bigrams
from collections import Counter, defaultdict
import random
import string

# Download necessary NLTK resources
nltk.download('reuters')
nltk.download('punkt')

# lowercase and remove non-alphabetic words
corpus = [word.lower() for word in reuters.words() if word.isalpha()]

# Calculate bigram and unigram frequencies
bigram_freqs = Counter(bigrams(corpus))
unigram_freqs = Counter(corpus)

# Build the bigram language model
bigram_model = defaultdict(dict)
for (w1, w2), freq in bigram_freqs.items():
    bigram_model[w1][w2] = freq / unigram_freqs[w1]

# Generate a 20-word
sequence = []
current_word = random.choice(list(bigram_model.keys()))  # random word
sequence.append(current_word)

while len(sequence) < 20:  # Keep generating until 20 words are reache
    if current_word not in bigram_model or not bigram_model[current_word]:
        break  # Stop if no valid next words
    next_word = random.choices(
        list(bigram_model[current_word].keys()),
        weights=[(freq ** 0.75) for freq in bigram_model[current_word].values()],
        k=1
    )[0]
    sequence.append(next_word)
    current_word = next_word  # Update the current word

print(' '.join(sequence))

