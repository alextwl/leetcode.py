'''
2026/09/11 daily challenge

counter (brute force) approach
'''


import collections


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        copies = collections.Counter(digits)
        return sum(collections.Counter(map(int, str(v))) <= copies for v in range(100, 999, 2))


'''
O(n**3) enumerations approach
'''


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        visited = [False] * 1000  # only evens in [100, 998] to be used
        cnt = 0

        for i, v0 in enumerate(digits):
            if v0 == 0:
                continue
            v0 = v0 * 100
            for j, v1 in enumerate(digits):
                if i == j:
                    continue
                v1 = v1 * 10
                for k, v2 in enumerate(digits):
                    if v2 & 1:
                        continue
                    if i == k or j == k:
                        continue
                    target = v0 + v1 + v2
                    if not visited[target]:
                        visited[target] = True
                        cnt += 1

        return cnt

