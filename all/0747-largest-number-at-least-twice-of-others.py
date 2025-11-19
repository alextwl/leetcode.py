'''
sorting approach
'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        arr = sorted(list(enumerate(nums)), key=lambda x: (x[1], x[0]), reverse=True)
        if arr[0][1] < arr[1][1] * 2:
            return -1
        return arr[0][0]


'''
find two largest numbers and do comparsion.
'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        large1, idx1 = -1, -1
        large2 = -1

        for i, v in enumerate(nums):
            if v >= large1:
                large2 = large1
                large1, idx1 = v, i
            elif v > large2:
                large2 = v

        return idx1 if large1 >= large2 * 2 else -1

