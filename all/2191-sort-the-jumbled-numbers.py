'''
2024/07/24 daily challenge

custom hash key sorting approach
'''


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {str(i): str(v) for i, v in enumerate(mapping)}

        def get_key(jumbled):
            restored = [d[x] for x in str(jumbled)]
            return int(''.join(restored))

        # note we need to maintain relative order if two mapped values were equal,
        # the indices of the values are included in the keys for sorting.
        ordered_nums = [(get_key(v), i, v) for i, v in enumerate(nums)]
        ordered_nums.sort()

        return [v for _, _, v in ordered_nums]

