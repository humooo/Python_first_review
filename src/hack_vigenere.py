import collections
import itertools
import string

from alphabets import russian_alphabeth, symbols_, len_english_alphabeth
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
    len_ = (0.027 * n) / ((n - 1) * coincident_index(text) + 0.065 - 0.038 * n)
    return int(len_) + 1


def find_key(text: str, len_key_text: int, model_) -> str:
    """
    algorithm for finding the key of the text for the English alphabet
    """
    key = ''
    for i in range(len_key_text):
        key += chr(ord('a') + suitable_step(text[i::len_key_text], model_) % len_english_alphabeth)
    return key


def hack_vigenere(input_file, output_file, model_):
    """
    hack the Vigenere cipher using match indexes
    """
    with get_stream(input_file, 'r') as input_file:
        text = input_file.read()
    key = find_key(text, len_key(text), model_)
    text = vigenere(text, key, is_encode=False)
    with get_stream(output_file, 'w') as output_file:
        output_file.write(text)
    return output_file
