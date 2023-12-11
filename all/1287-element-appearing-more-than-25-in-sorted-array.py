'''
2023/12/11 daily challenge

counter approach
'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4

        prev, count = None, 0

        for num in arr:
            if num == prev:
                count += 1
            else:
                prev = num
                count = 1

            if count > threshold:
                return num

        # undefined behavior
        return None

