'''
2023/01/01 daily challenge

dict approach

note multiple alphabets to the same word are not valid.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        plen = len(pattern)
        p2s = dict()  # alphabet -> word
        s2p = dict()  # word -> alphabet

        i = 0
        for word in s.split(' '):
            if i >= plen or p2s.setdefault(pattern[i], word) != word or s2p.setdefault(word, pattern[i]) != pattern[i]:
                # the word does not follow the pattern
                return False
            i += 1

        # the number of words in s should be equal to the length of pattern.
        return i == plen

