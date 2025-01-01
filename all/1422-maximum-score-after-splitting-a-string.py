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


'''
2025/01/01 daily challenge

one pass ver

learnt from official solution 3:
https://leetcode.com/problems/maximum-score-after-splitting-a-string/editorial/#approach-3-one-pass

score = left zeros + right ones
      = left zeros + (total ones - left ones)

running score = score - total ones
so the final answer is (running_score + total ones) = best score
'''


class Solution:
    def maxScore(self, s: str) -> int:
        zeros = ones = 0  # left zeros & left ones
        running_score = -500
        # iterate over the array except the last char for the right substring.
        for c in s[:-1]:
            if c == '0':
                zeros += 1
            else:
                ones += 1
            running_score = max(running_score, zeros - ones)
        # complete the total ones
        if s[-1] == '1':
            ones += 1
        # apply the derivative formula
        return running_score + ones

