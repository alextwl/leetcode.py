'''
2024/02/14 daily challenge

divide & merge approach
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        left, right = [], []

        for v in nums:
            if v < 0:
                left.append(v)
            else:
                right.append(v)

        ans = []
        for a, b in zip(left, right):
            # rearranged array begins with a positive integer
            ans.append(b)
            ans.append(a)

        return ans


'''
two pointers approach
'''


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        # note the rearranged array begins with a positive integer
        j, k = 0, 1  # the indices of next positive/negative integer

        for i, v in enumerate(nums):
            if v > 0:
                ans[j] = v
                j += 2
            else:
                ans[k] = v
                k += 2

        return ans

