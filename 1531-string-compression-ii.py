'''
2022/10/15 daily challenge

learnt from
https://leetcode.com/problems/string-compression-ii/discuss/767602/Python-Clear-top-down-recursive-approach-with-detailed-comments

note the greedy method doesn't work when multiple contiguous blocks of
same char can be connected after some chars deleted,
it returns more smaller cost of compressed string.
(e.g. s="xyzaabbbaa", k=3 given by author algomelon)

dynamic programming approach
with memorizing all cases of function calls.
(we can also use python's functools.lru_cache as dp cacher here.)
'''

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        '''
        the key is the arguments of the following inner function call,
        its value is the returned value of its call.
        '''
        dp = dict()
        
        def compressor(i, run_char, run_length, k_remain):
            '''
            :param i: the pointer of s.
            :param run_char: character of last run.
            :param run_length: last run length of the same character.
            :param k_remain: remaining count of characters to be deleted.
            '''
            
            if i == len(s):
                '''
                all chars of s are proceeded,
                the length of remaining to be compressed is zero.
                '''
                return 0
            
            # check dp cache.
            key = (i, run_char, run_length, k_remain)
            if key in dp:
                return dp[key]
            
            '''
            since the greedy method didn't work, we need to compare all possible options
            including both deleting and keeping s[i] in order to get the minimum length of compressed s.
            '''
            
            # (1) delete s[i] with k -= 1
            cost_when_delete_si = float('inf')
            if k_remain > 0:
                cost_when_delete_si = compressor(i+1, run_char, run_length, k_remain - 1)
            
            # (2) keep s[i]
            cost_when_keep_si = 0
            if s[i] == run_char:
                '''
                last run of the same char continues.
                
                we need to increment the cost when the length of current compressed run grows up.
                e.g. 'a' -> 'a2', 'a9' -> 'a10', 'a99' -> 'a100'
                when '0 <= k <= s.length <= 100' constraint applied.
                '''
                extra_cost = 1 if run_length in [1, 9, 99] else 0
                cost_when_keep_si = extra_cost + compressor(i+1, run_char, run_length+1, k_remain)
            else:
                '''
                a new run of char always costs a length of 1.
                '''
                cost_when_keep_si = 1 + compressor(i+1, s[i], 1, k_remain)
            
            # save the minimum cost
            dp[key] = min(cost_when_delete_si, cost_when_keep_si)
            
            return dp[key]
        
        return compressor(0, None, 0, k)
