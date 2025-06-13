'''
2023/08/09 daily challenge
2025/06/13 daily challenge

binary search + greedy approach

learnt from official solution
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/solution/
'''

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        '''
        sort the array first.
        the minimized pairs of difference are consisted of adjacent numbers.
        '''
        nums.sort()
        
        def countPairs(max_diff):
            '''
            count the number of pairs with diff <= max_diff.
            '''
            count = 0
            i = 0
            while(i < n-1):
                '''
                greedy method: always try to validate (nums[i], nums[i+1]) pairs.
                
                why greedy method works?
                assume we have two different answers of pairs,
                and the answers diverges from (i-1, i) and (i, i+1),
                that means both ans have the same pairs in the nums[0..i+1] range,
                but in the remaining range:
                
                (1) for the answer including (i-1, i), the remaining range is nums[i+1..n-1].
                (2) for the answer including (i, i+1), the remaining range is nums[i+2..n-1].
                
                although we suppose (2) might have valid pairs more than (1),
                but since (1) has remaining range nums[i+1..n-1] which is longer than (2)'s,
                (1)'s remaining range must contain more or equal pairs to (2)'s,
                thus greedy method works here.
                '''
                if nums[i+1] - nums[i] <= max_diff:
                    count += 1
                    i += 1  # the pair is consisted, let next loop starts from i+2.
                i += 1
            return count
        
        # do binary search a possible max_diff satisfying the input p.
        left, right = 0, nums[-1] - nums[0]

        '''
        we can always accept the right value of diff
        even if its valid pairs might be lesser than p
        when there's no more mid can provide sufficient pairs of p.
        '''
        while(left < right):
            mid = left + (right - left) // 2
            
            if countPairs(mid) >= p:
                # the mid can be accepted.
                right = mid
            else:
                # the mid is not satisfied.
                left = mid + 1

        return left


'''
dynamic programming approach (time limit exceeded)

learnt from the equation of recurrence relation in hint 3.
'''


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        # dp[i] = f(i, x) the minimum max diff of x pairs starting from nums[i]
        dp = [0] * n
        # prev_dp[i] = f(i, x-1) the minimum max diff of (x - 1) pairs starting from nums[i]
        # one extra value is workaround for the 1st iteration
        prev_dp = [0] * (n + 1)

        # build answer from 1 pair to p pairs.
        for pair_size in range(1, p + 1):
            # manipulate indices of possible values for new pairs
            p_range = list(range(n - 2 * pair_size, 2 * (p - pair_size) - 1, -1))
            dp[p_range[0] + 1] = float('inf')  # workaround for the 1st iteration
            for i in p_range:
                '''
                dp in two cases:

                f(i, x) = min(skip nums[i] as a value of the first new pair,
                              equation with the 1st new pair including nums[i])
                        = min(f(i+1, x),
                              max(nums[i+1] - nums[i], f(i+2, x-1))
                              )
                '''
                dp[i] = min(dp[i+1], max(nums[i+1] - nums[i], prev_dp[i+2]))
            dp, prev_dp = prev_dp, dp

        # f(0, p) is the answer
        return prev_dp[0]

