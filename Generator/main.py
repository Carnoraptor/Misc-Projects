import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import defaultdict, Counter
import random

# PDF reading
import typing

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction

# Summon text from pdf

def read_pdf():
    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open("TestPDF.pdf", "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])
    assert d is not None
    # print(l.get_text_for_page(0))
    return (l.get_text())

print(read_pdf())

# Tuple 2 string

def tuple_to_string(sentence):
    string_sentence = []
    for word in sentence:
        if isinstance(word, tuple):
            string_sentence.append(tuple_to_string(word))
        else:
            string_sentence.append(word)
    return ' '.join(string_sentence)


# Load text file

def load_data(file_path):
    with open (file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text.lower()

text_data = load_data("Src.txt")
tokens = word_tokenize(text_data)

# print("Tokens:", tokens)

# generate n-grams

trigrams = list(ngrams(tokens, 3))

# create trigram model

trigram_model = defaultdict(Counter)
for trigram in trigrams:
    trigram_model[(trigram[0], trigram[1])][trigram[2]] += 1

#for trigram, next_word_counter in trigram_model.items():
#    print("Trigram:", trigram)
#    print("Next words:", next_word_counter)

# generate the text

def generate_text(starting_words, model, num_words=20):
    sentence = list(starting_words)

    while True:
        # print("Current sentence:", sentence)
        if tuple(sentence[-2:]) in model:
            next_word_counter = model[tuple(sentence[-2:])]
            if next_word_counter:
                next_word = next_word_counter.most_common(1)[0][0]
            else:
                next_word = random.choice(list(model.keys()))
            sentence.append(next_word)
        else:
            next_word = random.choice(list(model.keys()))
            sentence.append(next_word)
        if len(sentence) >= num_words:
            break  # Exit the loop if the desired number of words has been reached
    
    return ''.join(tuple_to_string(sentence))

# init

starting_words = ("We", "the")
generated_text = generate_text(starting_words, trigram_model, 20)
print(generated_text)
