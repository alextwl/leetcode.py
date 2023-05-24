'''
2023/05/24 daily challenge

heap approach
'''

import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        prefixSum = 0
        ans = 0
        h = []  # min heap for nums1

        '''
        sort the pairs and order by nums2 descending,
        when we iterate it, the element will be always the minimum element of the iterated subsequence.

        it doesn't mean nums1 is not important,
        we also need to iterate over all the elements of nums1 & nums2 pairs later
        because the answer may consist of a bigger sum(nums1) and a smaller min(nums2).
        '''
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        for n1, n2 in pairs:
            prefixSum += n1
            heapq.heappush(h, n1)

            if len(h) == k:
                '''
                the prefixSum must contain the current n1
                so that the current n2 can be also chosen as a minimum of nums2 subsequence.
                '''
                ans = max(ans, prefixSum * n2)
                
                # pop the smallest nums1 and allocate a slot for the next pair.
                prefixSum -= heapq.heappop(h)

        return ans

