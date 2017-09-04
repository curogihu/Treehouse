# https://en.wikipedia.org/wiki/Polybius_square


import string

from ciphers import Cipher


class PolybiusSquare(Cipher):

    def __init__(self, offset=3):
        self.cipher_table = [
                            [['a'], ['b'], ['c'], ['d'], ['e']],
                            [['f'], ['g'], ['h'], ['i', 'j'], ['k']],
                            [['l'], ['m'], ['n'], ['o'], ['p']],
                            [['q'], ['r'], ['s'], ['t'], ['u']],
                            [['v'], ['w'], ['x'], ['y'], ['z']]
        ]

    def encrypt(self, text):
        output = []
        text = text.lower()

        for char in text:
            output_len = len(output)

            for row_index, row_value in enumerate(self.cipher_table):
                for column_index, column_value in enumerate(row_value):
                    if char in column_value:
                        output.append(str(row_index + 1) + str(column_index + 1))
                        break

                if output_len < len(output):
                    break

        return ''.join(output)

    def decrypt(self, text):
        output = []
        index_num_list = [(i + j) for (i, j) in zip(text[::2], text[1::2])]

        for index_num in index_num_list:
            row_index = int(index_num[0]) - 1
            column_index = int(index_num[1]) - 1
            output.append(self.cipher_table[row_index][column_index][0])

        return ''.join(output)



