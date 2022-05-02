from Globals import third_pixel
from get_stream import get_stream
from PIL import Image


def to_bit_message(message):
    """
    converting each character of the text into its bits
    """
    bit_message = [bin(ord(x))[2:] for x in message]
    bit_message = [x.rjust(8, '0') for x in bit_message]
    return bit_message


def encode(input_image, secret_image, input_file):
    """
    encrypting (hiding) text with the last bit

    input_image: the input image in which we want to hide the text
    secret_image: the received image, in which the text is hidden
    input_file: the text itself
    """
    with get_stream(input_file, 'r') as input_file:
        message = input_file.read()
    img = Image.open(input_image)
    encoded = img.copy()
    width, height = img.size
    i = 0

    message = str(len(message)) + ":" + str(message)
    message_bits = "".join(to_bit_message(message))
    message_bits += "0" * ((third_pixel - (len(message_bits) % third_pixel)) % third_pixel)

    for row in range(height):
        for col in range(width):
            if i + third_pixel <= len(message_bits):
                pixel = img.getpixel((col, row))
                r = pixel[0] & ~1 | int(message_bits[i])
                g = pixel[1] & ~1 | int(message_bits[i + 1])
                b = pixel[2] & ~1 | int(message_bits[i + 2])

                if img.mode == "RGBA":
                    encoded.putpixel((col, row), (r, g, b, pixel[third_pixel]))
                else:
                    encoded.putpixel((col, row), (r, g, b))

                i += third_pixel
            else:
                img.close()
                break
    encoded.save(secret_image)
    return secret_image


def decode(secret_image):
    """
    decryption (disclosure) of the text using the last bit of the image
    """
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
                pixel = pixel[:third_pixel]
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