'''
2022/10/10 daily challenge

time=O(n)
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            # Hint 1: no way to perform the replacement when only 1 char input.
            return ""
        
        # search the first half of palindrome.
        for i in range(0, len(palindrome) // 2):
            if palindrome[i] != 'a':
                '''
                Hint 2: always replace the first non-'a' with 'a'.
                '''
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        '''
        non-a replacement not occured
        this means the palindrome string is all 'a',
        or all 'a' with a middle non-'a'.
        
        Hint 4: replace the last 'a' with 'b'
        in order to get the lexicographically smallest string.
        '''
        return palindrome[:-1] + 'b'
