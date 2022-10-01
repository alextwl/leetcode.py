'''
2022/10/01 daily challenge

learnt from
https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming

dynamic programming approach
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            # invalid input with leading zero
            return 0
        
        # dp list for recording accumulated ways of decoding in each digit.
        dp = [0 for _ in range(len(s)+1)]
        
        '''
        assign initial values
        since we checked s[0] != '0' before,
        the first digit is guraranteed itself can form a way to be decoded.
        '''
        dp[0] = 1  # extra value for the first round of for-loop with 2-step jump.
        dp[1] = 1
        
        for i in range(2, len(s)+1):
            '''
            1-step jump
            if the digit is not zero, the digit itseif can form a way to be decoded.
            '''
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            '''
            2-step jump
            if 2 adjacent digits (i-2 & i-1) can form a decoded alphabet,
            accumulate the number of ways from dp[i-2]
            '''
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
