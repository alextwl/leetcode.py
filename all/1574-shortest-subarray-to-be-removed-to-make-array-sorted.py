'''
2024/11/15 daily challenge

two pointers approach

learnt from official solution:
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solution/
'''

import itertools


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # find the starting index of longest right subarray ending at last element.
        right = n - 1
        
        for v1, v0 in itertools.pairwise(reversed(arr)):
            if v0 <= v1:
                right -= 1
            else:
                break

        ans = right  # init with max length to be removed

        # find the ending index of longest left subarray
        left = 0

        while left < right and (left == 0 or arr[left-1] <= arr[left]):
            # shrink the right subarray if the current value is
            # larger than the starting point of right subarray
            while right < n and arr[left] > arr[right]:
                right += 1

            # calculate and minimize the length of subarray to be removed
            ans = min(ans, right - left - 1)
            left += 1

        return ans

