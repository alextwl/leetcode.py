'''
2023/11/13 daily challenge
2025/09/11 daily challenge

counting sort approach
'''


class Solution:
    def sortVowels(self, s: str) -> str:
        counter = {c: 0 for c in "AEIOUaeiou"}
        vowel_pos = []  # indices of vowels in s

        # count each vowel
        for i, c in enumerate(s):
            if c in counter:
                counter[c] += 1
                vowel_pos.append(i)

        q = [c for c in "uoieaUOIEA" if counter[c] > 0]
        if not q:
            # return the input directly if no vowels
            return s

        ls = list(s)
        # place vowels in nondecreasing ASCII order
        for i in vowel_pos:
            c = q[-1]
            ls[i] = c
            counter[c] -= 1
            if counter[c] == 0:
                q.pop()

        return ''.join(ls)

