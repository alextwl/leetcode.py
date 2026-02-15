'''
counter approach
'''


import collections


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate_ctr = collections.Counter(licensePlate.lower())
        for k in list(plate_ctr.keys()):
            if not k.isalpha(): del plate_ctr[k]

        ans = None
        for w in words:
            ctr = collections.Counter(w.lower())
            for k in plate_ctr.keys():
                if ctr[k] < plate_ctr[k]:
                    break
            else:
                if ans is None or len(ans) > len(w):
                    ans = w

        return ans

