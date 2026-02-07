'''
split string into words and check only decimals.
'''


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for w in s.split():
            if w.isdecimal():
                num = int(w)
                if num <= prev:
                    return False
                prev = num
        return True

