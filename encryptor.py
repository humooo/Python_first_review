import parser

from encode_and_decode import encode_and_decode
from hack_and_train import hack, train
from hack_vigenere import hack_vigenere


def main():
    args = parser.command_parser.parse_args()
    if args.method == 'encode':
        encode_and_decode(args.cipher, args.key, args.input_file, args.output_file, is_encode=True)
    elif args.method == 'decode':
        encode_and_decode(args.cipher, args.key, args.input_file, args.output_file, is_encode=False)
    elif args.method == 'train':
        train(args.text_file, args.model_file)
    elif args.method == 'hack':
        hack(args.input_file, args.output_file, args.model_file)
    elif args.method == 'hack_vigenere':
        hack_vigenere(args.input_file, args.output_file, args.model_file)


if __name__ == '__main__':
    main()
