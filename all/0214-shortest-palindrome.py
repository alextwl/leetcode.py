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


'''
Knuth-Morris-Pratt algorithm
'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        t = s + ',' + rev
        
        # Knuth-Morris-Pratt prefix
        kmp = [0] * len(t)
        plen = 0
        
        for i in range(1, len(t)):
            while plen > 0 and t[i] != t[plen]:
                plen = kmp[plen - 1]
            if t[i] == t[plen]:
                plen += 1
            kmp[i] = plen
        
        # longest palindrome's length
        longest = kmp[-1]
        
        return rev[:n - longest] + s

