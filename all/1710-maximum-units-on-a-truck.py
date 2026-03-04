'''
sorting + greedy method approach
'''


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])

        loaded = 0
        while truckSize and boxTypes:
            boxes, units = boxTypes.pop()
            if truckSize >= boxes:
                truckSize -= boxes
                loaded += boxes * units
            else:
                loaded += truckSize * units
                break
        return loaded

