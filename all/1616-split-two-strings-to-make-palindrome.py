'''
greedy method + two pointers approach

learnt from @lee215's solution:
https://leetcode.com/problems/split-two-strings-to-make-palindrome/solutions/888967/java-c-python-greedy-solution-o-1-space
'''


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # match palindrome parts from a_prefix & b_suffix
        i, j = 0, len(b) - 1
        while i < j and a[i] == b[j]:
            i, j = i + 1, j - 1
        # middle parts of a & b
        s1, s2 = a[i:j + 1], b[i: j + 1]

        # match palindrome parts from b_prefix & a_suffix
        i, j = 0, len(b) - 1
        while i < j and b[i] == a[j]:
            i, j = i + 1, j - 1
        # another middle parts of a & b
        s3, s4 = a[i:j + 1], b[i: j + 1]

        # if any part of middle a & b was a palindrome,
        # then we can form a permutation of palindrome by rule:
        # [a_prefix or b_prefix] + [s1, s2, s3, or s4] + [a_suffix or b_suffix]
        return any(s == s[::-1] for s in [s1, s2, s3, s4])

