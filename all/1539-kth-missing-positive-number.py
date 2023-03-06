'''
2023/03/06 daily challenge

binary search approach

search the difference == k between any index+1 and its expected value,
and the value of the missing number can be found.
'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1

        while(left <= right):
            mid = left + ((right-left)>>1)

            if arr[mid] - (mid+1) < k:
                # the missing number is in the right part
                left = mid + 1
            else:
                # the missing number is in the left part
                right = mid - 1

        return left + k

