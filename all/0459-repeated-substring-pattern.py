'''
2023/08/21 daily challenge
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def isRepeating(sublen):
            substr = s[:sublen]

            left = 0
            for right in range(sublen, len(s)+1, sublen):
                if s[left:right] != substr:
                    # substring pattern mismatch.
                    return False
                left = right

            return True
        
        for sublen in range(len(s) // 2, 0, -1):
            if len(s) % sublen:
                '''
                the length of substring cannot divide the full length of string evenly,
                thus the substring cannot be the repeated pattern.
                '''
                continue

            if isRepeating(sublen):
                '''
                repeated substring found.
                '''
                return True

        '''
        repeat substring not found.
        '''
        return False

