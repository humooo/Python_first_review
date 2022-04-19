import sys

from get_stream import get_stream
from PIL import Image


def encode(input_image, secret_image, input_file):
    with get_stream(input_file, 'r') as input_file:
        message = input_file.read()
    img = Image.open(input_image)
    encoded = img.copy()
    width, height = img.size
    i = 0

    message = str(len(message)) + ":" + str(message)
    message_bits = "".join([bin(ord(x))[2:].rjust(8, "0") for x in message])
    message_bits += "0" * ((3 - (len(message_bits) % 3)) % 3)

    for row in range(height):
        for col in range(width):
            if i + 3 <= len(message_bits):
                pixel = img.getpixel((col, row))
                r = pixel[0] & ~1 | int(message_bits[i])
                g = pixel[1] & ~1 | int(message_bits[i + 1])
                b = pixel[2] & ~1 | int(message_bits[i + 2])

                if img.mode == "RGBA":
                    encoded.putpixel((col, row), (r, g, b, pixel[3]))
                else:
                    encoded.putpixel((col, row), (r, g, b))

                i += 3
            else:
                img.close()
                break
    encoded.save(secret_image)


def decode(secret_image):
    img = Image.open(secret_image)
    width, height = img.size
    buff, count = 0, 0
    a = []
    massage = ''
    limit = None
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            if img.mode == "RGBA":
                pixel = pixel[:3]
            for color in pixel:
                buff += (color & 1) << (7 - count)
                count += 1
                if count == 8:
                    a.append(chr(buff))
                    buff, count = 0, 0
                    if a[-1] == ":" and limit is None:
                        try:
                            limit = int("".join(a[:-1]))
                        except Exception:
                            pass

            if len(a) - len(str(limit)) - 1 == limit:
                img.close()
                return "".join(a)[len(str(limit)) + 1 :]
    # with get_stream(output_file, 'w') as output_file:
    #    output_file.write(massage)
