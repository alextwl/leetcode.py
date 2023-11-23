'''
2023/11/23 daily challenge

check each [l,r] range and sort the subarrays
'''


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        
        for left, right in zip(l, r):
            seq = nums[left:right+1]
            seq.sort()  # rearrange the subarray
            it = iter(seq)
            prev = next(it)
            curr = next(it)
            diff = curr - prev
            prev = curr
            for curr in it:
                if curr - prev != diff:
                    ans.append(False)
                    break
                prev = curr
            else:
                ans.append(True)

        return ans

