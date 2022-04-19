import string
import itertools


from alphabets import russian_alphabeth, arabian_alphabeth, symbols, symbols_
from get_stream import get_stream


def next_symbol(symbol, step):
    if symbol in string.ascii_letters:
        if symbol.isupper():
            return chr(ord('A') + (ord(symbol) - ord('A') + step) % 26)
        else:
            return chr(ord('a') + (ord(symbol) - ord('a') + step) % 26)
    elif symbol in russian_alphabeth:
        if symbol.isupper():
            return chr(ord('А') + (ord(symbol) - ord('А') + step) % 33)
        else:
            return chr(ord('а') + (ord(symbol) - ord('а') + step) % 33)
    elif symbol in arabian_alphabeth:
        return chr(1575 + (ord(symbol) - 1575 + step) % 28)
    elif symbol in symbols_:
        return symbols[(symbols_[symbol] + step) % 5]
    else:
        return symbol


def caesar(text, key, is_encode):
    text_ = ''
    for symbol in text:
        text_ += next_symbol(symbol, key if is_encode else -key)
    return text_


def vigenere(text, key, is_encode):
    text_ = ''

    for symbol, key1 in zip(text, itertools.cycle(key)):
        if key1 in string.ascii_letters:
            ord1 = ord(key1.lower()) - ord('a')
        elif symbol in russian_alphabeth:
            ord1 = ord(key1.lower()) - ord('а')
        elif symbol in symbols:
            ord1 = symbols1[symbol]
        else:
            ord1 = 0
        text_ += next_symbol(symbol, ord1 if is_encode else -ord1)
    return text_


def encode_and_decode(cipher, key, input_, output_, is_encode):
    with get_stream(input_, 'r') as input_file:
        text = input_file.read()
    if cipher == 'caesar':
        text = caesar(text, int(key), is_encode)
    elif cipher == 'vigenere':
        text = vigenere(text, key, is_encode)
    elif cipher == 'vernam':
        with get_stream(key, 'r') as text_:
            text = vigenere(text, text_.read(), is_encode)
    with get_stream(output_, 'w') as output_file:
        output_file.write(text)
