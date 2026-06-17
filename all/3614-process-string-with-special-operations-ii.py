'''
2026/06/17 daily challenge

simulation approach

do not manipluate the string but simulate changes to the length of string & k pointer.

learnt from official editorial:
https://leetcode.com/problems/process-string-with-special-operations-ii/editorial/#approach-simulation
'''


class Solution:
    def processStr(self, s: str, k: int) -> str:
        slen = 0

        # calculate the final length of result string
        for c in s:
            if c == '%':
                # reversing string does not affect length
                continue
            elif c == '#':
                # double the length
                slen <<= 1
            elif c == '*':
                # pop a char if existed
                if slen:
                    slen -= 1
            else:
                slen += 1
        
        # shortcut: out-of-bound query
        if k >= slen:
            return '.'

        # reverse the operations
        for c in reversed(s):
            if c == '%':
                # reverse the pointer
                k = slen - k - 1
            elif c == '#':
                # undo the double
                if k + 1 > (slen + 1) // 2:
                    k -= slen // 2
                slen = (slen + 1) // 2
            elif c == '*':
                # undo pop char
                slen += 1
            else:
                # undo append char
                if k + 1 == slen:
                    return c
                slen -= 1

        return '.'

