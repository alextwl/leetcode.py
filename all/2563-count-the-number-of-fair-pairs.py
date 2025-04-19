'''
2024/11/13 daily challenge
2025/04/19 daily challenge

two pointers approach

note the sorting does not affect the result because no matter whether
i < j or j < i, (nums[i], nums[j]) and (nums[j], nums[i]) have the same
sum and form the same number of pair.
'''


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        
        def get_pairs(target):
            # calculate the number of pairs with its sum < target
            left, right = 0, n - 1
            pairs = 0
            
            while left < right:
                if nums[left] + nums[right] < target:
                    # accumulate the number of pairs (nums[left], each element in nums[left+1:right+1])
                    pairs += right - left
                    # shrink the window from left
                    left += 1
                else:
                    # sum too large, shrink the window from right
                    right -= 1
            return pairs

        # note the upper & lower values should be included.
        return get_pairs(upper + 1) - get_pairs(lower)


'''
binary search approach
'''


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()

        def search(left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        ans = 0
        for i, v in enumerate(nums):
            # search the left bound of element right to nums[i]
            left = search(i + 1, n - 1, lower - v)  # sum < lower
            # search the right bound of element right to nums[i]
            right = search(i + 1, n - 1, upper - v + 1)  # sum <= upper
            ans += right - left
        return ans

