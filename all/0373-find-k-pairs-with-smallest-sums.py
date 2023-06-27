'''
2023/06/27 daily challenge

heap approach

use min heap to gradually queue the sum of pairs
instead of sort the entire [x+y for x in nums1 for j in nums2].
'''

import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)

        ans = []
        seen = set()  # Set[Tuple(int, int)], a set of tuples which is already added to ans.

        '''
        h[*] = (sum, nums1 index, nums2 index)
        
        nums1[0]+nums2[0] is the smallest sum.
        '''
        h = [(nums1[0]+nums2[0], 0, 0)]

        while(h and k):
            _, i, j = heapq.heappop(h)  # the sum of popped elements is not important anymore.
            ans.append([nums1[i], nums2[j]])
            k -= 1

            # try to iterate the next element of nums1
            new_i = i+1
            if new_i < n1:
                if (new_i, j) not in seen:
                    heapq.heappush(h, (nums1[new_i]+nums2[j], new_i, j))
                    seen.add((new_i, j))

            # try to iterate the next element of nums2
            new_j = j+1
            if new_j < n2:
                if (i, new_j) not in seen:
                    heapq.heappush(h, (nums1[i]+nums2[new_j], i, new_j))
                    seen.add((i, new_j))

        return ans

