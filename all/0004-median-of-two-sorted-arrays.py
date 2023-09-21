'''
2023/09/21 daily challenge

merge sort approach

time=O(m+n)
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        mid, mod = divmod(m+n, 2)
        
        # indices to be searched
        q = [mid]
        if not mod:
            q.append(mid-1)

        ans = []
        
        i = j = 0
        idx = 0
        
        target = q[-1]
        while(q):
            for curr in range(i, m):
                if j < n and nums1[curr] > nums2[j]:
                    nums1, nums2 = nums2, nums1
                    m, n = n, m
                    i, j = j, curr
                    break
                
                if idx == target:
                    ans.append(nums1[curr])
                    q.pop()
                    if q:
                        target = q[-1]
                    else:
                        break
                idx += 1
            else:
                nums1, nums2 = nums2, nums1
                m, n = n, m
                i, j = j, n

        if len(ans) == 2:
            return (ans[0] + ans[1]) / 2.0

        return ans[0] * 1.0

