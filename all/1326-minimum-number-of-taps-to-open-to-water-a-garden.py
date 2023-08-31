'''
2023/08/31 daily challenge

dynamic programming approach
'''

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        '''
        top-down dp space
        dp[i] = the minimum number of taps needed for interval [0, i]
        '''
        dp = [float('inf')] * (n+1)
        
        '''
        base case
        no taps needed for a zero interval [0, 0] which covers no garden.
        '''
        dp[0] = 0
        
        '''
        evaluate all taps from left to right
        '''
        for i, radius in enumerate(ranges):
            left = max(0, i - radius)
            right = min(i + radius, n)
            
            # update [left, right] interval
            min_taps = dp[right]
            for j in range(left, right + 1):
                '''
                2 cases:
                (1) we have the minimum taps opened.
                (2) we can have more lesser taps opened by opening j-th tap before i-th tap.
                '''
                min_taps = min(min_taps, dp[j] + 1)
            dp[right] = min_taps

        return dp[-1] if dp[-1] < float('inf') else -1


'''
greedy approach, reduce to problem 45 Jump Game II

learnt from official solution:
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/solution/
'''

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        '''
        calculate how far the rightmost position each tap can reach.
        '''
        max_reach = [0] * (n+1)
        
        for i, radius in enumerate(ranges):
            # determine the garden interval [left, right] of this single tap
            left = max(0, i - radius)
            right = min(i + radius, n)
            
            '''
            left-th tap can reach the rightmost position `right` if the current tap `i` opened.
            or left-th tap is already able to reach `i` and further taps.
            '''
            max_reach[left] = max(max_reach[left], right)
        
        # the minimum number of taps used
        taps = 0

        # base case: an empty interval
        # current rightmost position reached (== the rightmost covered garden)
        curr_end = 0        
        # next rightmost position can be reached. (== the rightmost garden which could be covered.)
        next_end = 0
        
        for i in range(n+1):
            if i > next_end:
                '''
                there's a gap between previous opened tap and
                current tap that cannot cover.
                '''
                return -1
            
            '''
            i is within the next_end, that means we may have water here
            and determine whether we need to open the previous tap or not.
            '''
            if i > curr_end:
                '''
                we need to open the tap ending at next_end to tap the water
                because the opened tap's interval cannot cover i-th garden.
                '''
                taps += 1
                '''
                so we opened a new tap, current rightmost position is extended.
                '''
                curr_end = next_end
            
            '''
            update the next rightmost garden that can be reached if we opened the i-th tap.
            '''
            next_end = max(next_end, max_reach[i])
        
        return taps

