'''
2022/11/08 daily challenge

strip 2 adjacent same-letter chars with different font cases recursively.
'''

class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        while (i < len(s)):
            '''
            find the difference between adjacent chars
            note that ord('a') - ord('A') == 32 for the same letter.
            '''
            if abs(ord(s[i-1]) - ord(s[i])) == 32:
                s = s[:i-1] + s[i+1:]
                i = max(i - 2, 1)
            else:
                i += 1
        
        return s
