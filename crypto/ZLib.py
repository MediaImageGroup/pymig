"""
Copyright (c) Billal Fauzan 2021 <billal.xcode]@gmail.com>
"""

import random
import zlib
from utils import check_byte, check_string

class CompressObjectError(Exception):
    pass

def generate_keys(length, alp=True, nums=True):
    ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "1234567890"
    OUTPUTS = ""
    alp_lists = ""
    if alp:
        alp_lists += ALPHABET
    elif nums:
        alp_lists += NUMBERS
    else:
        alp_lists += ALPHABET
        alp_lists += NUMBERS

    for _ in range(length):
        OUTPUTS += random.choice(alp_lists)
    return OUTPUTS

def compress(data_original):
    default = random.randint(4, 6)
    keys = generate_keys(default)
    keys = "|" + keys
    keys = keys.encode()
    if check_byte(data_original):
        current_data = zlib.compress(data_original)
        return current_data + keys
    else:
        return False