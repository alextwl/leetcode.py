'''
leetcode 75 lv1 day 14
'''

import string


class Solution:
    def decodeString(self, s: str) -> str:
        qQuant = []  # List[int] quantifier stack
        currQuant = ""  # str numeric quantifier buffer
        qStr = []  # List[str] string stack
        currStr = ""  # str string buffer

        for c in s:
            if c == '[':
                qQuant.append(int(currQuant))
                currQuant = ""
                qStr.append(currStr)
                currStr = ""
            elif c == ']':
                currStr = qStr.pop() + qQuant.pop() * currStr   
            elif c in string.digits:
                currQuant = currQuant + c
            else:
                # c in ascii_lowercase
                currStr += c
        
        return currStr

