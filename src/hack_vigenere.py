import collections
import itertools
import string

from Globals import fraction, len_english_alphabeth, matches_index
from Globals import polyalphabetic_matchs_index, russian_alphabeth, symbols_
from encode_and_decode import vigenere
from get_stream import get_stream
from hack_and_train import suitable_step


def coincident_index(text: str) -> float:
    """
    a function for finding the match index, knowing for each character its number in the text
    """
    l = 0
    for symbol in text:
        if symbol in string.ascii_letters:
            l += 1
    count = dict(collections.Counter(symbol.lower() for symbol in text if symbol in
                                     itertools.chain(string.ascii_letters,
                                                     russian_alphabeth, symbols_)))
    s = 0
    for symbol in string.ascii_lowercase:
        if symbol not in count:
            continue
        s += count[symbol] * (count[symbol] - 1) / (l * (l - 1))
    return s


def len_key(text: str) -> int:
    """
    algorithm for finding the length of the text key for the English alphabet
    """
    n = 0
    for symbol in text:
        if symbol in string.ascii_letters:
            n += 1
    len_ = (fraction * n) / ((n - 1) * coincident_index(text) + matches_index - polyalphabetic_matchs_index * n)
    return int(len_) + 1


def find_key(text: str, len_key_text: int, model_file) -> str:
    """
    the algorithm for finding the key of the text for the English alphabet, knowing already the length of the key
    """
    key = ''
    for i in range(len_key_text):
        key += chr(ord('a') + suitable_step(text[i::len_key_text], model_file) % len_english_alphabeth)
    return key


def hack_vigenere(input_file, output_file, model_file):
    """
    hack the Vigenere cipher using match indexes

    input_file: the input file, by default this is standard input
    output_file: the output file, by default, is the standard output
    model_file: the file in which the language model is built using large text
    """
    with get_stream(input_file, 'r') as input_file:
        text = input_file.read()
    key = find_key(text, len_key(text), model_file)
    text = vigenere(text, key, is_encode=False)
    with get_stream(output_file, 'w') as output_file:
        output_file.write(text)
    return output_file
