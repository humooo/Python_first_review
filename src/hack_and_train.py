import collections
import itertools
import pickle
import string


from alphabets import russian_alphabeth, symbols, symbols_
from encode_and_decode import caesar, next_symbol
from get_stream import get_stream


def count(text):
    count_1 = dict(collections.Counter(symbol.lower() for symbol in text if symbol in
                                       itertools.chain(string.ascii_letters, russian_alphabeth, symbols_)))
    sum_1 = sum(count_1.values())
    if sum_1:
        for l in count_1.keys():
            count_1[l] /= sum_1
    return count_1


def train(text_file, model_file):
    with get_stream(text_file, 'r') as text_file:
        text = text_file.read()
    with open(model_file, 'wb') as model_file:
        pickle.dump(count(text), model_file)
    return model_file


def diff(step, mod, count_):
    sum_2 = 0
    for symbol in count_:
        sum_2 += abs(mod[next_symbol(symbol, step)] - count_[symbol])
    return sum_2


def hack(input_file, output_file, model_file):
    with open(model_file, 'rb') as model_file:
        value_in_model_file = pickle.load(model_file)
    with get_stream(input_file, 'r') as input_file:
        text = input_file.read()
    min_step = 26 - min(range(26), key=lambda step:
                        diff(step, value_in_model_file, count(text)))
    text = caesar(text, min_step, is_encode=False)
    with get_stream(output_file, 'w') as output_file:
        output_file.write(text)
    return output_file