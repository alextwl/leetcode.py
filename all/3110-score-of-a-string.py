'''
2024/06/01 daily challenge
'''


class Solution:
    def scoreOfString(self, s: str) -> int:
        it = map(ord, s)
        prev = next(it)
        ans = 0
        for asciibyte in it:
            ans += abs(prev - asciibyte)
            prev = asciibyte
        
        return ans

