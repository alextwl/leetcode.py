'''
2023/03/05 daily challenge
2026/05/18 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        target = n - 1

        v2i = collections.defaultdict(set)
        for i, v in enumerate(arr):
            v2i[v].add(i)

        visited_i = set()  # prevent from revisiting indexes
        visited_v = set()  # prevent from queueing duplicate indexes of the same value
        # start from the first index
        q = collections.deque([(0, 0)])  # (index, step)

        while(q):
            i, step = q.popleft()

            if i in visited_i:
                continue
            visited_i.add(i)

            step += 1

            # (1) jump to next
            if (j := i+1) < n:
                if j == target:
                    return step
                q.append((j, step))
            # (2) jump to previous
            if (j := i-1) >= 0:
                if j == target:
                    return step
                q.append((j, step))
            # (3) jump to any indexes with the same value
            v = arr[i]
            if v in visited_v:
                continue
            
            for j in v2i[v] - {i}:
                if j == target:
                    return step
                q.append((j, step))

            visited_v.add(v)

        # undefined behavior
        return -1


'''
level order traversal approach
'''


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        seen_val = set()
        seen_idx = set()
        n = len(arr)
        target = n - 1

        v2i = dict()
        for i, v in enumerate(arr):
            if v not in v2i:
                v2i[v] = [i]
            else:
                v2i[v].append(i)

        curr_list = [0]
        next_list = []
        jumps = 0
        while curr_list:
            for i in curr_list:
                if i == target:
                    return jumps
                if i in seen_idx:
                    continue
                seen_idx.add(i)

                if i - 1 >= 0:
                    next_list.append(i - 1)
                if i + 1 < n:
                    next_list.append(i + 1)
                if arr[i] not in seen_val:
                    seen_val.add(arr[i])
                    next_list.extend(v2i[arr[i]])

            jumps += 1
            curr_list, next_list = next_list, []

        return -1  # undefined

