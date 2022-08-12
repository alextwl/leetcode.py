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
            if (n < 0):
                # all elements of nums2 are merged,
                # no need to proceed remaining nums1 elements
                # because they were already sorted.
                return
                # ans[ptr] = nums1[m]
                # m -= 1
            elif (m < 0):
                # all elements of nums1 are merged,
                # just copy remaining num2 elements to the ans array.
                while(n >= 0):
                    ans[ptr] = nums2[n]
                    n -= 1
                    ptr -= 1
            elif (nums1[m] >= nums2[n]):
                ans[ptr] = nums1[m]
                m -= 1
            else:
                ans[ptr] = nums2[n]
                n -= 1
        return
