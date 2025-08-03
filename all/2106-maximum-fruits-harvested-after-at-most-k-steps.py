'''
2025/08/03 daily challenge

prefix sum + binary search approach

learnt from official editorial:
https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/editorial/#approach-1-binary-search
'''


import bisect


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)
        i2pos = [0] * n

        for i, (j, v) in enumerate(fruits):
            prefix[i + 1] = prefix[i] + v
            i2pos[i] = j

        max_fruits = 0
        for x in range(k // 2 + 1):
            # optimal way: move in one direction and then then turn around only once
            # (1) move left x steps and then right (k - x*2) steps
            y = k - x * 2
            left, right = startPos - x, startPos + y
            # search the boundary of fruits to be collected
            start = bisect.bisect_left(i2pos, left)
            end = bisect.bisect_right(i2pos, right)
            max_fruits = max(max_fruits, prefix[end] - prefix[start])

            # (2) move right x steps and then left (k - x*2) steps
            left, right = startPos - y, startPos + x
            # search the boundary of fruits to be collected
            start = bisect.bisect_left(i2pos, left)
            end = bisect.bisect_right(i2pos, right)
            max_fruits = max(max_fruits, prefix[end] - prefix[start])

        return max_fruits


'''
sliding window + binary search approach
'''


import bisect


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        # binary search the boundary of the leftest possible window
        left = bisect.bisect_left(fruits, [startPos - k, float('-inf')])
        right = bisect.bisect_right(fruits, [startPos, float('inf')])

        window_sum = sum(fruits[i][1] for i in range(left, right))
        max_fruits = window_sum

        # try to expand right boundary of the window
        for i in range(right, n):
            curr_pos, curr_fruits = fruits[i]
            window_sum += curr_fruits

            if curr_pos - startPos > k:
                # next position too far, cannot expand boundary
                break

            # shrink from left (steps including the part of turning around)
            while min(abs(curr_pos - startPos), abs(startPos - fruits[left][0])) + \
                    curr_pos - fruits[left][0] > k:
                window_sum -= fruits[left][1]
                left += 1
            max_fruits = max(max_fruits, window_sum)
        return max_fruits

