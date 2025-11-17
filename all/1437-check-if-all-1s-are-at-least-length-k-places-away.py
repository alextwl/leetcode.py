'''
2025/11/17 daily challenge
'''


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        it = iter(nums)
        # find the first 1
        for c in it:
            if c:
                break

        # validate gap length
        zeros = 0
        for c in it:
            if c:
                if zeros < k:
                    return False
                zeros = 0
            else:
                zeros += 1

        return True

