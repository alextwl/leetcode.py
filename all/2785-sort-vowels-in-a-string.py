'''
2023/11/13 daily challenge

counting sort approach
'''


class Solution:
    def sortVowels(self, s: str) -> str:
        ls = list(s)
        counter = {c: 0 for c in "AEIOUaeiou"}
        vowel_pos = []

        # count each vowel
        for i, c in enumerate(ls):
            if c in counter:
                counter[c] += 1
                vowel_pos.append(i)

        q = [c for c in "uoieaUOIEA" if counter[c] > 0]
        if not q:
            # return the input directly if no vowels
            return s

        # place vowels in nondecreasing ASCII order
        for i in vowel_pos:
            if counter[q[-1]] == 0:
                q.pop()
            ls[i] = q[-1]
            counter[q[-1]] -= 1

        return ''.join(ls)

