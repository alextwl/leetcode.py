'''
2024/02/24 daily challenge

Union-find approach
'''

import collections


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = [i for i in range(n)]
        rank = [0] * n
        
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
        
        def union(a, b):
            a, b = find(a), find(b)
            
            if rank[a] >= rank[b]:
                rank[a] += 1
                parent[b] = a
            else:
                rank[b] += 1
                parent[a] = b
        
        # convert meetings to d[time] = (x, y)
        meetings.sort(key=lambda k: k[2])
        meetings_by_time = collections.defaultdict(list)
        for x, y, t in meetings:
            meetings_by_time[t].append((x, y))
        
        # person 0 shares secret to firstPerson
        union(0, firstPerson)
        
        for groups in meetings_by_time.values():
            # hold the meetings
            for x, y in groups:
                union(x, y)
            
            # reset Union-Find if both x & y didn't get the secret.
            for x, y in groups:
                if find(x) != find(0):
                    parent[x] = x
                    rank[x] = 0
                    # y didn't get the secret because x didn't, too.
                    parent[y] = y
                    rank[y] = 0

        ans = [0]
        for i in range(1, n):
            if find(i) == find(0):
                ans.append(i)

        return ans

