'''
2025/06/15 daily challenge

greedy method approach

similar to problem 2566 (leading zeros allowed ver)
'''


class Solution:
    def maxDiff(self, num: int) -> int:
        min_s = max_s = str(num)

        n = len(max_s)
        i = 0
        while i < n and max_s[i] == '9':
            i += 1
        if i < n:
            max_s = max_s.replace(max_s[i], '9')

        if min_s[0] != '1':
            # replace the leftmost digit with '1' to prevent from generating leading zero
            min_s = min_s.replace(min_s[0], '1')
        else:
            i = 1
            # we also need to avoid replacing any digit which is same to the leftmost digit here.
            while i < n and (min_s[i] == '0' or min_s[i] == min_s[0]):
                i += 1
            if i < n:
                min_s = min_s.replace(min_s[i], '0')

        return int(max_s) - int(min_s)

