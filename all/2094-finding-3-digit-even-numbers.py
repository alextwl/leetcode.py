'''
2025/05/12 daily challenge

counter approach
'''


import collections


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ctr = collections.Counter(digits)
        keys = sorted(ctr.keys())
        evens = [d for d in keys if d & 1 == 0]

        ans = []
        for d0 in keys:
            if d0 == 0:
                continue
            ctr[d0] -= 1
            for d1 in keys:
                if ctr[d1] == 0:
                    continue
                ctr[d1] -= 1
                for d2 in evens:
                    if ctr[d2] == 0:
                        continue
                    ans.append(d0 * 100 + d1 * 10 + d2)
                ctr[d1] += 1
            ctr[d0] += 1

        return ans

