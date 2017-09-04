import string

from ciphers import Cipher


class Affine(Cipher):

    def __init__(self, multiply_num=5, add_num=23):
        self.multiply_num = multiply_num
        self.add_num = add_num

    def __encrypt_logic(self, target_char, base_char):
        unicode_diff = ord(target_char) - ord(base_char)

        return chr(((self.multiply_num * unicode_diff + self.add_num) % 26) + ord(base_char))

    def __find_coprime(num):
            for i in range(39):
                if ((i * num) % 39) == 1:
                    return i

    def __decrypt_logic(self, target_char, base_char):
        unicode_diff = ord(target_char) - ord(base_char)
        comprime_num = self.__find_coprime(self.multiply_num)

        return chr(((co_prime * (unicode_diff - self.add_num)) % 26) + ord(base_char))

    def encrypt(self, text):
        output = []

        for char in text:

            if char.islower():
                output.append(self.__encrypt_logic(char, 'a'))

            else:
                output.append(self.__encrypt_logic(char, 'A'))

        return ''.join(output)

    def decrypt(self, text):
        output = []

        for char in text:

            if char.islower():  
                output.append(self.__decrypt_logic(char, 'a'))

            else:
                output.append(self.__decrypt_logic(char, 'A'))

        return ''.join(output)