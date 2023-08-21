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


'''
mathematical approach (string concatenation)

if we could repeat a substring of s,
then s can be a substring of a rotated double-length s.

learnt from official approach 2:
https://leetcode.com/problems/repeated-substring-pattern/solution/
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        return True if s in t[1:-1] else False

