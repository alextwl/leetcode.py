'''
2025/06/14 daily challenge

brute force approach

iterate all possible digits and maximize/minimize the value.
'''


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        digits = set(s)
        # shortcut: if there's only one digit,
        # then the max difference is the same length number with only digit 9.
        if len(digits) == 1:
            return int("9" * len(s))

        max_val = 0
        min_val = float('inf')
        for digit in digits:
            remapped = int(s.replace(digit, "9"))
            max_val = max(max_val, remapped)
            remapped = int(s.replace(digit, "0"))
            min_val = min(min_val, remapped)

        return max_val - min_val


'''
greedy method approach

learnt from official editorial:
https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/editorial/
'''


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)  # max value
        t = s         # min value

        # max value = replace the first occurance of non-9 digit with 9.
        i = 0
        while i < len(s) and s[i] == '9':
            i += 1
        if i < len(s):
            s = s.replace(s[i], '9')

        # min value = replace the leftmost digit to 0.
        t = t.replace(t[0], '0')
        return int(s) - int(t)

