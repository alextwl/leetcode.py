'''
2025/12/24 daily challenge

sorting + greedy method approach
'''


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)  # in non-increasing order
        boxes = 0
        # fill the larger box first
        for cap in capacity:
            apples -= cap
            boxes += 1
            if apples <= 0:
                break
        return boxes

