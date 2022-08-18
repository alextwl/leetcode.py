'''
2022/08/18 daily challenge
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2 + len(arr) % 2
        seen = dict()
        
        # count all occurances by value
        for val in arr:
            seen[val] = seen.get(val, 0) + 1
        
        element_size = 0
        min_set_size = 0
        for count in reversed(sorted(seen.values())):
            if element_size >= half:
                break
            element_size += count
            min_set_size += 1
        
        return min_set_size
