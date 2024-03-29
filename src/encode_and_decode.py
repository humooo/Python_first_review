import itertools
import string

from Globals import arabian_alphabeth, len_arabian_alphabeth, len_english_alphabeth, len_russian_alphabeth
from Globals import len_symbols, ord_first_arabian_symbol, russian_alphabeth, symbols, symbols_
from get_stream import get_stream


def next_symbol(symbol, step):
    """
    A function that takes one character and returns another character by a certain step modulo n,
    depending on the alphabet
    symbol: for it, we will return another character that differs from this one by step modulo the length of the alphabet
    step: in the case of encryption, this is a positive number, in the case of decryption, it is negative
    """
    res = symbol
    if symbol in string.ascii_letters:
        if symbol.isupper():
            res = chr(ord('A') + (ord(symbol) - ord('A') + step) % len_english_alphabeth)
        else:
            res = chr(ord('a') + (ord(symbol) - ord('a') + step) % len_english_alphabeth)
    elif symbol in russian_alphabeth:
        if symbol.isupper():
            res = chr(ord('А') + (ord(symbol) - ord('А') + step) % len_russian_alphabeth)
        else:
            res = chr(ord('а') + (ord(symbol) - ord('а') + step) % len_russian_alphabeth)
    elif symbol in arabian_alphabeth:
        res = chr(ord_first_arabian_symbol + (ord(symbol) - ord_first_arabian_symbol + step) % len_arabian_alphabeth)
    elif symbol in symbols_:
        res = symbols[(symbols_[symbol] + step) % len_symbols]
    return res


def caesar(text, key, is_encode):
    """
    For encrypting and decrypting the Caesar cipher
    text: the name of the file we want to encrypt or decrypt
    key: the key (for this cipher is a number) for encryption/decryption
    is_encode: True - in the case of encryption, False - in the case of decryption
    """
    text_ = ''
    for symbol in text:
        text_ += next_symbol(symbol, key if is_encode else -key)
    return text_


def vigenere(text, key, is_encode):
    """
    For encrypting and decrypting the Vigenere cipher
    text: the name of the file we want to encrypt or decrypt
    key: the key (for this cipher is a string) for encryption/decryption
    is_encode: True - in the case of encryption, False - in the case of decryption
    """
    text_ = ''

    for symbol, key1 in zip(text, itertools.cycle(key)):
        if key1 in string.ascii_letters:
            ord1 = ord(key1.lower()) - ord('a')
        elif symbol in russian_alphabeth:
            ord1 = ord(key1.lower()) - ord('а')
        elif symbol in symbols:
            ord1 = symbols[symbol]
        else:
            ord1 = 0
        text_ += next_symbol(symbol, ord1 if is_encode else -ord1)
    return text_


def encode_and_decode(cipher, key, input_file, output_file, is_encode):
    """
    A function that takes the output text and, depending on
    the encryption method, encrypts or decrypts the text and
    returns it

    cipher: cipher type - vegenere, caesar or vernam
    input_file: the input file, by default this is standard input
    output_file: the output file, by default, is the standard output
    """
    with get_stream(input_file, 'r') as input_file:
        text = input_file.read()
    if cipher == 'caesar':
        text = caesar(text, int(key), is_encode)
    elif cipher == 'vigenere':
        text = vigenere(text, key, is_encode)
    elif cipher == 'vernam':
        with get_stream(key, 'r') as text_:
            text = vigenere(text, text_.read(), is_encode)
    with get_stream(output_file, 'w') as output_file:
        output_file.write(text)
    return output_file
