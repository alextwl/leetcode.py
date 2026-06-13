'''
2026/06/13 daily challenge

simulation approach
'''


ASCII_A = ord('a')
ASCII_Z = ord('z')


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for w in words:
            wsum = sum(weights[v - ASCII_A] for v in map(ord, w))
            ans.append(chr(ASCII_Z - wsum % 26))
        return ''.join(ans)

