'''
2023/05/06 daily challenge

binary search approach (same to 0001 two sum.)

Since a subsequence can be formed by picking any elements
within the input array (or a subarray,) the number of subsequences which
satisfied the condition will be the same to the ones formed from a sorted array.

Just think those elements to form satisfied subsequences are able to be selected
from both the original array and sorted array regardless of the order.

and then do two pointer (to get min/max vals) & binary search to calculate the ans.
'''

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        # after nums sorted, the beginning & the end of any subarray are its min/max vals.
        left, right = 0, len(nums)-1

        ans = 0
        '''
        the condition of left==right should be captured
        because a single element also forms a subsequence.
        '''
        while(left <= right):
            if nums[left] + nums[right] > target:
                # the sum is too big, shrink the max.
                right -= 1
            else:
                '''
                the sum satisfies, count the ans.
                the subsequences we count have the same min value
                and any max values which <= nums[right] in order to satisfies the target sum.

                e.g. input array=[1,2,3], target=4, left=0, right=2
                valid subsequences:
                [1], [1,2], [1,3], [1,2,3]
                there are 4 subseqs == 2**(right-left)
                '''
                ans += pow(2, right-left, 1_000_000_007)
                # we can try to increase the min for the next round.
                left += 1

        return ans % 1_000_000_007

