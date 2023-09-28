'''
2023/09/28 daily challenge
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for v in nums:
            if v & 1:
                odd.append(v)
            else:
                even.append(v)
        return even + odd


'''
two pointer approach
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while(left < right):
            if nums[left] & 1:
                '''
                the left element is an odd number,
                always swap it with a right element
                until it becomes even. (== swapped with an even number)
                '''
                nums[left], nums[right] = nums[right], nums[left]
                '''
                nums[right] becomes odd so it's sorted, let's move it one step left.
                '''
                right -= 1
            else:
                # the left element is an even number so it's sorted. next.
                left += 1

        return nums

