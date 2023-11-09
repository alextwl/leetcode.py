'''
2023/11/09 daily challenge

count consecutive character approach

consider the number of substrings of a string:

a -> 1 a
aa -> 2 a + 1 aa
aaa -> 3 a + 2 aa + 1 aaa
aaaa -> 4 a + 3 aa + 2 aaa + 1 aaaa
... etc.

for n * 'a', the number of substrings is 1+2+...+n.

when a new group of consecutive character starts,
we can restart the streak.
'''


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        streak = 0

        prev = s[0]
        for c in s:
            if c == prev:
                streak += 1
            else:
                streak = 1

            ans = (ans + streak) % 1_000_000_007
            prev = c

        return ans

