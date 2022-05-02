import parser

from get_stream import get_stream
from stegano_encode_decode import encode, decode


def main():
    args = parser.command_parser.parse_args()
    if args.method == 'encode':
        encode(f'IMG/{args.start_img}', f'IMG/{args.encoded_img}', args.input_file)
    elif args.method == 'decode':
        with get_stream(args.output_file, 'w') as output_file:
            output_file.write(decode(f'IMG/{args.encoded_img}'))


if __name__ == '__main__':
    main()
