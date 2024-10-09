'''
2024/10/09 daily challenge

count open & unbalanced brackets
'''


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        min_add = 0
        unbalanced = 0

        for c in s:
            if c == '(':
                unbalanced += 1
            elif unbalanced:
                unbalanced -= 1
            else:
                min_add += 1

        return min_add + unbalanced

