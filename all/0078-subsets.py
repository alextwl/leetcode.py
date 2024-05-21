'''
2024/05/21 daily challenge

recursion approach
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def gen_subset(i, subset_list):
            if i == n:
                ans.append(subset_list)
                return
            
            # not to include nums[i]
            gen_subset(i + 1, subset_list.copy())
            # to include nums[i]
            subset_list.append(nums[i])
            gen_subset(i + 1, subset_list)
            
            return
        
        gen_subset(0, list())
        return ans

