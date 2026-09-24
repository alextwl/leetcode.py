'''
2026/09/24 daily challenge

type conversion approach
'''


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, digs in enumerate(map(str, nums)):
            if sum(map(int, digs)) == i:
                return i
        return -1


'''
division approach
'''


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            digit_sum = 0
            while v:
                v, dig = divmod(v, 10)
                digit_sum += dig
            if dig == i:
                return i
        return -1

