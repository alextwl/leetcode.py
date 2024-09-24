'''
2024/09/24 daily challenge

set approach
'''


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def arr2set(arr):
            s = {""}  # an empty string is necessary for no common prefix case
            for w in map(str, arr):
                for i in range(1, len(w)):
                    s.add(w[:i])
                s.add(w)
            return s
        
        s1, s2 = arr2set(arr1), arr2set(arr2)

        return max(map(len, s1 & s2))

