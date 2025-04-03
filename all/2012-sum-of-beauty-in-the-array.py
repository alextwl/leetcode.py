'''
greedy method + suffix min approach

similar to problem 2873 & 2874.
'''


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)

        # build a suffix min array
        current_min = 100_000
        suffix_min = []  # suffix_min[i] = min(nums[j] for j in range(i, n))
        for v in reversed(nums):
            current_min = min(current_min, v)
            suffix_min.append(current_min)
        suffix_min.reverse()

        beauty = 0
        it = enumerate(nums)
        _, v0 = next(it)
        _, v1 = next(it)
        max_j = v0
        for k, v2 in it:
            if max_j < v1 < suffix_min[k]:
                beauty += 2
            elif v0 < v1 < v2:
                beauty += 1
            max_j = max(max_j, v1)
            v0, v1 = v1, v2

        return beauty

