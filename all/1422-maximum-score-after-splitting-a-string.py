'''
2023/12/22 daily challenge

suffix sum approach
'''


class Solution:
    def maxScore(self, s: str) -> int:
        # cut only middle parts without the beginning & ending chars
        ss = s[1:-1]

        # assume the left substring is empty and the right one is full.
        ones = ss.count('1')
        zeroes = 0
        max_score = ones
        for c in ss:
            if c == '0':
                zeroes += 1
            else:
                ones -= 1
            
            max_score = max(max_score, ones + zeroes)

        # the problem asks for two non-empty substrings,
        # so the first & last chars are always counted.
        if s[0] == '0':
            max_score += 1
        if s[-1] == '1':
            max_score += 1

        return max_score

