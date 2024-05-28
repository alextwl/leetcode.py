'''
2024/05/28 daily challenge

sliding window approach
'''


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        max_len = 0
        left = 0
        cost = 0

        for right, (c1, c2) in enumerate(zip(s, t)):
            # always accumulate the cost. the same char in both s & t generates no cost.
            cost += abs(ord(c1) - ord(c2))

            # shrink from the left
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

