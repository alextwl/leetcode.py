'''
2026/05/07 daily challenge

divide and conquer approach

learnt from official editorial 1:
https://leetcode.com/problems/jump-game-ix/editorial/#approach-1-interval-divide-and-conquer
'''


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # the previous maximum and its index (val, idx)
        prev_max = []
        prev = (float('-inf'), -1)
        for i, v in enumerate(nums):
            if v > prev[0]:
                prev = (v, i)
            prev_max.append(prev)
        
        def process(r, right_min, right_max):
            p_max, pivot_idx = prev_max[r]
            if p_max <= right_min:
                # no elements can transfer to the right interval
                curr_max = p_max
            else:
                # all elements can reach p_max and then go to right_max
                curr_max = right_max
            
            next_right_min = min(p_max, right_min)
            for i in range(pivot_idx, r + 1):
                ans[i] = curr_max
                next_right_min = min(next_right_min, nums[i])

            if pivot_idx == 0:
                return
            
            process(pivot_idx - 1, next_right_min, curr_max)
        
        process(n - 1, float('inf'), 0)
        return ans

