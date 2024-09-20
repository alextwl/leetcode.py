'''
2024/09/20 daily challenge

equivalent to find the longest palindrome.
'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        
        for i in range(n):
            if s[:n-i] == rev[i:]:
                return rev[:i] + s
        
        return ''

