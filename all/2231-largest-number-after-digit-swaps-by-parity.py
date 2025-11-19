'''
sorting + str/int conversion approach

assign bigger number to higher digit
'''


class Solution:
    def largestInteger(self, num: int) -> int:
        arr = [int(c) for c in str(num)]
        odds = sorted(v for v in arr if v & 1)
        evens = sorted(v for v in arr if v & 1 == 0)
        ans = []
        for orig in arr:
            if orig & 1:
                ans.append(odds.pop())
            else:
                ans.append(evens.pop())
        return int(''.join(map(str, ans)))

