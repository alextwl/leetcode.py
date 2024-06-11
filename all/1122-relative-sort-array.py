'''
2024/06/11 daily challenge

hashmap approach
'''


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {v: i for i, v in enumerate(arr2)}

        rel = []
        asc = []

        for v in arr1:
            if v in d:
                rel.append(v)
            else:
                asc.append(v)

        rel.sort(key=lambda v: d[v])
        asc.sort()

        return rel + asc

