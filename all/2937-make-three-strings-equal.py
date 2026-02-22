'''
find the length of common prefix.
'''


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # rearrange to make s1 the longest
        if len(s2) < len(s3):
            s2, s3 = s3, s2
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        prefix_len = 0
        for i, c in enumerate(s1):
            if i >= len(s2) or i >= len(s3) or s2[i] != c or s3[i] != c:
                prefix_len = i
                break
        else:
            return 0
        if prefix_len == 0:
            return -1

        return len(s1) + len(s2) + len(s3) - prefix_len * 3

