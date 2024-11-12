'''
2024/11/12 daily challenge

sorting approach
'''


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        ans = [0] * len(queries)

        items.sort()
        q = sorted((p, j) for j, p in enumerate(queries))

        i = 0
        max_beauty = 0
        for p, j in q:
            while i < n and items[i][0] <= p:
                max_beauty = max(max_beauty, items[i][1])
                i += 1
            ans[j] = max_beauty

        return ans

