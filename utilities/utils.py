import base64
import re

from django.conf import settings


def save_to_file(img_string, name):
    if img_string is not None and 'base64,' in img_string:
        img_string = img_string.split('base64,')[1]
        img_string = bytearray(img_string, 'utf-8')
        filename = settings.UPLOADS_DIR + name + '.jpg'
        with open(filename, 'wb') as f:
            f.write(base64.decodebytes(img_string))
            f.close()
        return '/uploads/' + name + '.jpg'
    return img_string


def replace_str_with_us(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '_', s)
    return s


def generate_ticket_id(tid):
    a = str(abs(hash(tid)) % (10 ** 4))
    b = str(abs(hash(tid[::-1])) % (10 ** 4))
    return a + "-" + b
