'''
formatting string.
'''


class Solution:
    def maskPII(self, s: str) -> str:
        if s[-1].isalpha():
            # email address
            email = s.lower().split('@')
            return "%s*****%s@%s" % (email[0][0], email[0][-1], email[1])
        else:
            # phone number
            stack = []
            i = len(s) - 1
            digits = 0
            while i >= 0:
                if s[i].isdigit():
                    if digits in [4, 7, 10]:
                        stack.append('-')
                    if digits < 4:
                        stack.append(s[i])
                    else:
                        stack.append('*')
                    digits += 1
                i -= 1
            if digits > 10:
                stack.append('+')
            return ''.join(stack[::-1])

