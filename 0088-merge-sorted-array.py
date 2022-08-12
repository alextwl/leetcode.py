class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = m+n
        ans = nums1  # for code readiness
        
        # point to last element of nums1 & nums2
        m -= 1
        n -= 1
        
        while(ptr):
            ptr -= 1
            if (m >= 0 and n < 0):
                ans[ptr] = nums1[m]
                m -= 1
                # stop?
            elif (m < 0 and n >= 0):
                ans[ptr] = nums2[n]
                n -= 1
            elif (nums1[m] >= nums2[n]):
                ans[ptr] = nums1[m]
                m -= 1
            else:
                ans[ptr] = nums2[n]
                n -= 1
        return
