import random

class Solution:
    def __init__(self, nums: List[int]):
        self.orig_list = list(nums)
        self.array = list(nums)

    def reset(self) -> List[int]:
        self.array = list(self.orig_list)
        return self.array

    def shuffle(self) -> List[int]:
        # Fisher-Yates algorithm
        # randomly swap any two elements n times
        numsLen = len(self.array)
        for i in range(0, numsLen):
            randidx = random.randrange(i, numsLen)
            self.array[i], self.array[randidx] = self.array[randidx], self.array[i]
        return self.array
