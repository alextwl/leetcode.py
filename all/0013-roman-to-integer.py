class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        c = x = i = 0
        for digit in s:
            if digit == 'M':
                ans += 1000
                if c:
                    ans -= c
                    c = 0
            elif digit == 'D':
                ans += 500
                if c:
                    ans -= c
                    c = 0
            elif digit == 'C':
                c += 100
                if x:
                    ans += c - x
                    c = x = 0
            elif digit == 'L':
                ans += 50
                if x:
                    ans -= 10
                    x = 0
            elif digit == 'I':
                i += 1
            elif digit == 'X':
                x += 10
                if i:
                    ans += x - i
                    x = i = 0
            elif digit == 'V':
                ans += 5
                if i:
                    ans -= i
                    i = 0
        ans += c + x + i
        return ans
