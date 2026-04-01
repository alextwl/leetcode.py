'''
sliding window approach
'''


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # the index of last ascending consecutive subarray starts at.
        ascend_start = -1

        # preprocess window
        prev = nums[0]
        it = enumerate(nums)
        for _ in range(k - 1):
            i, v = next(it)
            if prev != v - 1:
                ascend_start = i
            prev = v
        
        ans = []
        for i, v in it:
            if prev != v - 1:
                ascend_start = i
            prev = v
            if ascend_start > i - k + 1:
                # another ascending subarray starts after
                # the beginning of current window
                ans.append(-1)
            else:
                # the maximum element is the last element
                # due to the nature of ascending subarray.
                ans.append(v)

        return ans

