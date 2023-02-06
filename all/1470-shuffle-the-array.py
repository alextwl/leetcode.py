'''
2023/02/06 daily challenge
'''


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for x, y in zip(nums[:n], nums[n:]):
            ans.append(x)
            ans.append(y)
        return ans


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
        return ans


'''
btw the official in-place solution did a trick on
all nums' unused higher bits since n is restricted in 1 <= n <= 500.
with bitwise trick we can achieve space=O(1) solution.
'''

