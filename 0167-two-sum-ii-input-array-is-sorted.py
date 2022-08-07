# 2019 submission

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = dict()
        for idx, i in enumerate(numbers):
            if target - i in checked:
                return [checked[target-i]+1, idx+1]
            checked[i] = idx
