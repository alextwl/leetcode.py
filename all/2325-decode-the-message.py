'''
table lookup (dictionary) approach
'''


LOWER_A = ord('a')


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = {' ': ' '}
        i = 0
        for c in key:
            if c not in cipher:
                cipher[c] = chr(LOWER_A + i)
                i += 1
        return ''.join(map(cipher.__getitem__, message))

