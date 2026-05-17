'''
2026/05/17 daily challenge

graph traversal + visited set approach
'''


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = [start]
        visited = {start}

        while q:
            i = q.pop()
            val = arr[i]
            if val == 0:
                return True
            
            for j in [i - val, i + val]:
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    q.append(j)

        return False

