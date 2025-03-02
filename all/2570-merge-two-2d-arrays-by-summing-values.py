'''
2025/03/02 daily challenge

two pointers approach
'''


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        i = j = 0

        ans = []
        while i < m and j < n:
            id1, v1 = nums1[i]
            id2, v2 = nums2[j]
            if id1 > id2:
                ans.append(nums2[j])
                j += 1
            elif id1 < id2:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append([id1, v1+v2])
                i += 1
                j += 1

        # append all remaining elements
        while i < m:
            ans.append(nums1[i])
            i += 1
        while j < n:
            ans.append(nums2[j])
            j += 1

        return ans

