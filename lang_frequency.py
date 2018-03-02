import re
import sys
from collections import Counter

TOP_WORDS = 10


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return file_handler.read()
    except FileNotFoundError:
        print('Bad path to file')


def word_processing(text):
    prepared_text = re.sub(r'\W', ' ', text)
    words = prepared_text.split()
    return words


def creation_dictionary_words(words):
    dictionary_words = Counter(words)
    return dictionary_words


def get_most_frequent_words(dictionary_words, top_words=TOP_WORDS):
    return dictionary_words.most_common(top_words)


if __name__ == '__main__':

    text = load_data(sys.argv[1])
    if text is not None:
        words = word_processing(text)
        dictionary_words = creation_dictionary_words(words)
        most_frequent_words = get_most_frequent_words(dictionary_words)
        for num, word in enumerate(most_frequent_words):
            print(num + 1, " ", word)
