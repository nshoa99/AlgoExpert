# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
# Time complexity O(n) | Space complexity O(n)

import string
alphabet = string.ascii_lowercase
dict_alphabet = {}
my_len = len(alphabet)

for i, c in enumerate(alphabet):
    dict_alphabet[c] = i


def caesarCipherEncryptor(string, key):
    result = []
    for c in string:
        shift_number = (dict_alphabet[c] + key) % my_len
        result.append(alphabet[shift_number])

    return "".join(result)
