'''
2026/05/02 daily challenge

brute force approach
'''


class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for s in map(str, range(1, n + 1)):
            # ignore 018, check if there's at least one digit
            # could be rotated to another different digit,
            # and exclude those cannot be rotated.
            if any(c in "2569" for c in s) and not any(c in "347" for c in s):
                ans += 1
        return ans

