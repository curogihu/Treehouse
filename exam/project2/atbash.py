import string

from ciphers import Cipher


class Atbash(Cipher):

    def encrypt(self, text):
        output = []

        for char in text:
            unicode_number = ord(char)

            if char.islower():
                unicode_diff = unicode_number - ord('a')
            else:
                unicode_diff = unicode_number - ord('A')

            if unicode_diff < 13:
                output.append(chr(unicode_number + (12 - unicode_diff) * 2 + 1))
            else:
                output.append(chr(unicode_number + (unicode_diff - 13) * 2 - 1))

        return ''.join(output)

    def decrypt(self, text):
        output = []

        for char in text:
            unicode_number = ord(char)

            if char.islower():
                unicode_diff = unicode_number - ord('a')
            else:
                unicode_diff = unicode_number - ord('A')

            if unicode_diff < 13:
                output.append(chr(unicode_number + (12 - unicode_diff) * 2 + 1))
            else:
                output.append(chr(unicode_number + (unicode_diff - 13) * 2 - 1))

        return ''.join(output)



