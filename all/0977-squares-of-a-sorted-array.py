'''
2024/03/02 daily challenge

stack approach
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # filter non-negative integers from nums[]
        non_negs = []
        while(nums and nums[-1] >= 0):
            non_negs.append(nums.pop())
        
        # nums[] has only negative integers now
        ans = []
        while(nums or non_negs):
            if nums and non_negs:
                if -nums[-1] < non_negs[-1]:
                    ans.append(nums.pop() ** 2)
                else:
                    ans.append(non_negs.pop() ** 2)
            elif nums:
                ans.append(nums.pop() ** 2)
            else:
                ans.append(non_negs.pop() ** 2)

        return ans

