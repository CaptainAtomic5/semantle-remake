import nltk
from nltk.corpus import words
import spacy

# model loaded in
nlp = spacy.load("en_core_web_lg")

word_list = words.words()

def distance(vec1, vec2):
    norm = (vec1 - vec2)**2
    total = norm.sum()
    return total**(1/2)
word1 = nlp(input("Enter a word: "))
word2 = nlp(input("Enter another word: "))

print(f"Similarity of the words: {word1.similarity(word2): .3f}")

word1 = word1.vector
word2 = word2.vector

print(f"Distance between the words: {distance(word1, word2): .3f}")
