class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # intuitive way
        seen1 = {}
        seen2 = {}
        for num in nums1:
            seen1[num] = 1
        for num in nums2:
            seen2[num] = 1
        
        ans = []
        for num in seen1.keys():
            if num in seen2:
                ans.append(num)
        
        return ans

        # oneliner
        return list(set(nums1) & set(nums2))
