import re
import sys
from collections import Counter


def load_data(filepath):
        with open(filepath, 'r') as file_handler:
            return file_handler.read()


def get_words(text):
    prepared_text = re.sub(r'\W', ' ', text.lower())
    words = prepared_text.split()
    return words


def get_counter_words(words):
    counter_words = Counter(words)
    return counter_words


def get_most_frequent_words(counter_words, top_words=10):
    return counter_words.most_common(top_words)


if __name__ == '__main__':
    try:
        text = load_data(sys.argv[1])
        words = get_words(text)
        counter_words = get_counter_words(words)
        most_frequent_words = get_most_frequent_words(counter_words)
        for num, count in enumerate(most_frequent_words, start=1):
            print(num, " ", count)
    except (FileNotFoundError, IndexError):
        print('Bad path to file')
