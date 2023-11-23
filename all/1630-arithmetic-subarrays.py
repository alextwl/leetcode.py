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


'''
hash (set) ver
'''

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        
        for left, right in zip(l, r):
            seq = nums[left:right+1]
            sset = set(seq)
            smin, smax = min(seq), max(seq)
            diff = (smax - smin) / (len(seq)-1)
            
            curr = smin + diff
            while(curr < smax):
                if curr not in sset:
                    ans.append(False)
                    break
                curr += diff
            else:
                ans.append(True)

        return ans

