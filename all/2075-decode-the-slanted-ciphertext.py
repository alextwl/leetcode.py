'''
2026/04/04 daily challenge

decoding simulation approach
'''


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        width = (n + rows - 1) // rows
        stack = []
        # enumerate encodedText by matrix indices
        i = j = 0
        while j < width:
            idx = (i * width) + i + j
            if idx >= n:
                break
            stack.append(encodedText[idx])
            i += 1
            if i == rows:
                i = 0
                j += 1
        # originalText has no trailing spaces
        return ''.join(stack).rstrip()

