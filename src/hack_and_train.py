import collections
import itertools
import pickle
import string

from alphabets import russian_alphabeth, symbols_, arabian_alphabeth, len_english_alphabeth
from encode_and_decode import caesar, next_symbol
from get_stream import get_stream


def count(text):
    """
    a function that counts for each character the number of
    times the specified character occurs in the text and
    returns a dictionary of them
    """
    count_1 = dict(collections.Counter(symbol.lower() for symbol in text if symbol in
                                       itertools.chain(string.ascii_letters, russian_alphabeth,
                                                       symbols_, arabian_alphabeth)))
    sum_1 = sum(count_1.values())
    if sum_1:
        for l in count_1.keys():
            count_1[l] /= sum_1
    return count_1


def train(text_file, model_file):
    """
    creates a dictionary of characters and their number in a large text
    """
    with get_stream(text_file, 'r') as text_file:
        text = text_file.read()
    with open(model_file, 'wb') as model_file:
        pickle.dump(count(text), model_file)
    return model_file


def diff(step, mod, count_):
    """
    considers the measure of similarity
    """
    sum_2 = 0
    for symbol in count_:
        sum_2 += abs(mod[next_symbol(symbol, step)] - count_[symbol])
    return sum_2


def suitable_step(text, model_file):
    """
    a function that uses frequency analysis to find the right key for us
    """
    with open(model_file, 'rb') as model_file:
        value_in_model_file = pickle.load(model_file)
    step_ = len_english_alphabeth - min(range(len_english_alphabeth), key=lambda step:
                                       diff(step, value_in_model_file, count(text)))
    return step_


def hack(input_file, output_file, model_file):
    """
    the function that finds the key for the Caesar cipher will
    count all the measures, and finding among them the most minimal
    """
    with get_stream(input_file, 'r') as input_file:
        text = input_file.read()
    step = suitable_step(text, model_file)
    text = caesar(text, step, is_encode=False)
    with get_stream(output_file, 'w') as output_file:
        output_file.write(text)
    return output_file
