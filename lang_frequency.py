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


def get_most_frequent_words(words, top_words=10):
    counted_frequents_words = Counter(words)
    most_frequent_words = counted_frequents_words.most_common(top_words)
    return most_frequent_words


if __name__ == '__main__':
    try:
        text = load_data(sys.argv[1])
        words = get_words(text)
        most_frequent_words = get_most_frequent_words(words)
        print('num', 'word', 'count' )
        for num, count_dict in enumerate(most_frequent_words, start=1):
            word = count_dict[0]
            count = count_dict[1]
            print(num, ' ', word, ' ', count)
    except(IndexError, IOError):
        print('Bad path to file')
