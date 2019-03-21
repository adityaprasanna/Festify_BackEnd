import base64
import re

from django.conf import settings


def save_to_file(img_string, name):
    img_string = img_string.split('base64,')[1]
    img_string = bytearray(img_string, 'utf-8')
    filename = settings.UPLOADS_DIR + name + '.jpg'
    with open(filename, 'wb') as f:
        f.write(base64.decodebytes(img_string))
        f.close()
    return '/uploads/' + name + '.jpg'

def replace_str_with_us(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '_', s)
    return s
