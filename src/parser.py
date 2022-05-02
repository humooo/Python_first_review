import argparse
import sys


def build_encode_parser():
    """
    for parsing command line arguments in case of Caesar/Vigenere/Vernam
    """
    encode_parser = subs.add_parser('encode', description='Encode')
    encode_parser.set_defaults(method='encode')
    encode_parser.add_argument('--cipher', required=True, help='Cipher name: caesar or vigenere or vernam')
    encode_parser.add_argument('--key', required=True, help='Cipher key')
    encode_parser.add_argument('--input-file', required=False,
                               help='Name of input file', dest='input_file', default=sys.stdin)
    encode_parser.add_argument('--output-file', required=False,
                               help='Name of output file', dest='output_file', default=sys.stdout)
    return encode_parser


def build_decode_parser():
    """
    for parsing command line arguments in case of Caesar/Vigenere/Vernam
    """
    decode_parser = subs.add_parser('decode', description='Decode')
    decode_parser.set_defaults(method='decode')
    decode_parser.add_argument('--cipher', required=True, help='Cipher name: caesar or vigenere or vernam')
    decode_parser.add_argument('--key', required=True, help='Cipher key')
    decode_parser.add_argument('--input-file', required=False,
                               help='Name of input file', dest='input_file', default=sys.stdin)
    decode_parser.add_argument('--output-file', required=False,
                               help='Name of output file', dest='output_file', default=sys.stdout)
    return decode_parser


def build_train_parser():
    """
    for parsing command line arguments in the case of building a language model
    """
    train_parser = subs.add_parser('train', description='Train')
    train_parser.set_defaults(method='train')
    train_parser.add_argument('--text-file', required=False,
                              help='Name of text file', dest='text_file', default=sys.stdin)
    train_parser.add_argument('--model-file', required=True,
                              help='Name of model file', dest='model_file')
    return train_parser


def build_hack_parser():
    """
    for parsing command line arguments in case of hacking the Caesar cipher by frequency analysis
    """
    hack_parser = subs.add_parser('hack', description='Hack')
    hack_parser.set_defaults(method='hack')
    hack_parser.add_argument('--input-file', required=False,
                             help='Name of text file', dest='input_file', default=sys.stdin)
    hack_parser.add_argument('--output-file', required=False,
                             help='Name of model file', dest='output_file', default=sys.stdout)
    hack_parser.add_argument('--model-file', required=True,
                             help='Name of model file', dest='model_file')
    return hack_parser


def build_hack_vigenere_parser():
    """
    for parsing command-line arguments in case of hacking the Vigener cipher using match index methods
    """
    hack__vigenere_parser = subs.add_parser('hack_vigenere', description='Hack_vigenere')
    hack__vigenere_parser.set_defaults(method='hack_vigenere')
    hack__vigenere_parser.add_argument('--input-file', required=False,
                             help='Name of text file', dest='input_file', default=sys.stdin)
    hack__vigenere_parser.add_argument('--output-file', required=False,
                             help='Name of model file', dest='output_file', default=sys.stdout)
    hack__vigenere_parser.add_argument('--model-file', required=True,
                             help='Name of model file', dest='model_file')
    return hack__vigenere_parser


def build_stegano_encode_parser():
    """
    for parsing command line arguments in case of hiding text in image
    """
    stegano_encode_parser = subs.add_parser('stegano_encode', description='Steganography encode')
    stegano_encode_parser.set_defaults(method='encode')
    stegano_encode_parser.add_argument('--start-img', required=True,
                                             help='Name of start image', dest='start_img')
    stegano_encode_parser.add_argument('--encoded-img', required=True,
                                             help='Name of encoded image', dest='encoded_img')
    stegano_encode_parser.add_argument('--input-file', required=False,
                                             help='Name of input file', dest='input_file', default=sys.stdin)
    return stegano_encode_parser


def build_stegano_decode_parser():
    """
    for parsing command line arguments in case of text disclosure in photogrophy
    """
    stegano_decode_parser = subs.add_parser('stegano_decode', description='Steganography decode')
    stegano_decode_parser.set_defaults(method='decode')
    stegano_decode_parser.add_argument('--encoded-img', required=True,
                                             help='Name of encoded image', dest='encoded_img')
    stegano_decode_parser.add_argument('--output-file', required=False,
                                             help='Name of output file', dest='output_file', default=sys.stdout)
    return stegano_decode_parser


command_parser = argparse.ArgumentParser()
subs = command_parser.add_subparsers()
encode_parser = build_encode_parser()
decode_parser = build_decode_parser()
train_parser = build_train_parser()
hack_parser = build_hack_parser()
hack_vigenere_parser = build_hack_vigenere_parser()
stegano_encode_parser = build_stegano_encode_parser()
stegano_decode_parser = build_stegano_decode_parser()