'''
cyclic replacement, time=O(n), space=O(1)
learnt from
https://leetcode.com/problems/rotate-array/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = None
        numslen = len(nums)
        k %= numslen  # maybe k > len(nums)
        count = 0  # replacement count
        start = 0

        while count < numslen:
            current = start
            prev = nums[current]
            
            while(True):
                dest = (current + k) % numslen
                temp = nums[dest]
                nums[dest] = prev
                prev = temp
                
                current = dest
                count += 1
                
                if start == current:
                    break
                
            start += 1
        return
