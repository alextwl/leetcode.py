'''
2023/01/20 daily challenge

bitmask + recursive approach
'''


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # allocate a set of bitmask
        # because the subsequences may be duplicated
        bitmask_set = set()

        def appendNum(bitmask, i, prev = None):
            if i >= len(nums):
                # end of array reached, verify if the subsequence is valid.
                if bitmask and bin(bitmask).count('1') >= 2:
                    bitmask_set.add(bitmask)
                return

            if prev is None or nums[i] >= prev:
                # non-decreasing number found, append nums[i]
                appendNum(bitmask << 1 | 1, i+1, nums[i])
            
            # do not append nums[i]
            appendNum(bitmask << 1, i+1, prev)

        # try to append nums from i=0 recursively
        appendNum(0, 0, None)

        # convert bitmask set to an array of non-decreasing subsequences
        ans = []
        subseq_str_set = set()
        for bitmask in bitmask_set:
            subseq = []
            for i in range(len(nums)-1, -1, -1):
                if bitmask & 1:
                    subseq.append(nums[i])
                bitmask = bitmask >> 1
            subseq_str = str(subseq)  # list is not hashable in python, duh!
            # avoid duplicating subsequences of having different element but the same values
            if subseq_str not in subseq_str_set:
                ans.append(subseq[::-1])
                subseq_str_set.add(subseq_str)

        return ans

