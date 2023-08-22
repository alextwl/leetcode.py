'''
2023/08/22 daily challenge
'''

import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        
        '''
        convert columnNumber to 26-base digits,
        and then convert 26-base to Excel column title.
        '''
        quo = columnNumber
        while(quo):
            '''
            while the system is likely a 26-base,
            note that the number would start from 1 (1~26) and not from 0 (0~25),
            so we need to substract 1 from the dividend in each round.

            for example:
            columnNumber = 26, ans = "Z" -> (25+1) * 26**0
            columnNumber = 27, ans = "AA" -> (0+1) * 26**1 + (0+1) * 26**0
            columnNumber = 28, ans = "AB" -> (0+1) * 26**1 + (1+1) * 26**0
            '''
            quo -= 1
            quo, rem = divmod(quo, 26)
            ans += string.ascii_uppercase[rem]

        return ans[::-1]

