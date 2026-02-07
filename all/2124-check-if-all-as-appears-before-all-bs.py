'''
linear search approach
'''


class Solution:
    def checkString(self, s: str) -> bool:
        b_found = False
        for c in s:
            if c == 'a':
                if b_found:
                    return False
            else:
                b_found = True
        return True

