'''
2024/12/05 daily challenge

two pointers approach

learnt from official solution 3:
https://leetcode.com/problems/move-pieces-to-obtain-a-string/solution/
'''


class Solution:
    def canChange(self, a: str, b: str) -> bool:
        n = len(a)
        i = j = 0

        while i < n or j < n:
            # skip '_'
            while i < n and a[i] == '_':
                i += 1
            while j < n and b[j] == '_':
                j += 1

            if i == n or j == n:
                return i == n and j == n

            # do char by char matching
            c0 = a[i]
            c1 = b[j]

            # (1) c0 must equal to c1
            # (2) if c0 was L, j must not be ahead of i because L cannot move to the right
            # (3) if c0 was R, i must not be ahead of j because R cannot move to the left
            if c0 != c1 or (c0 == 'L' and i < j) or (c0 == 'R' and i > j):
                return False

            i += 1
            j += 1

        return True

