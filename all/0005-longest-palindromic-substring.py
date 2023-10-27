'''
learnt from official approach 4: expand around center
time=O(n**2), space=O(1)
'''

class Solution:
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        '''
        expand substring with palindrome checking,
        return the maximum length of possible substring from input center.
        
        the input (left & right) may equal if the expected center was a letter. (e.g. abcba)
        or the expected center was between the left & right letters. (left != right.) (e.g. abba)
        '''
        while(left >= 0 and \
              right < len(s) and \
              s[left] == s[right]):
            left -= 1
            right += 1
        
        return right - left - 1
        
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # index of start:end+1 of longest palindrome substring
        start = end = 0
        
        for i in range(len(s)):
            # try to expand palindrome substring with selected center.
            len1 = self.expandAroundCenter(s, i, i)  # center is a letter
            len2 = self.expandAroundCenter(s, i, i+1)  # center is between 2 letters
            maxlen = max(len1, len2)
            if (maxlen > end - start):
                # longer substring found, update longest substring boundary
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        
        return s[start:end+1]


'''
2023/10/27 daily challenge

dynamic programming approach

evaluate every length of substrings with previously found palindromes
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # dp[i][j] == True if s[i:j+1] is a palindrome, O(n**2) space
        dp = [[False] * n for _ in range(n)]
        
        # the start & end indices of the longest palindrome
        longest = (0, 0)
        
        # all single char is a palindrome
        for i in range(n): dp[i][i] = True
        
        # evaluate length-2 palindromes
        it = enumerate(s)
        i, prev = next(it)
        for j, curr in it:
            if prev == curr:
                dp[i][j] = True
                longest = (i, j)
            i, prev = j, curr
        
        # evaluate length > 2 palindromes by extending from existed
        for delta in range(2, n):
            for i in range(n - delta):
                j = i + delta
                # both start/end are the same && substring is also palindrome
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    longest = (i, j)
        
        return s[longest[0]:longest[1]+1]

