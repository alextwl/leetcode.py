'''
2026/05/30 daily challenge

segment tree approach (memory limit exceeded)

learnt from official editorial 1:
https://leetcode.com/problems/block-placement-queries/editorial/#approach-1-segment-tree
'''


import bisect


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        maxval = 50000
        seg = [0] * (maxval << 2)
        slist = [0, maxval]  # list, keep sorted manually

        def update(idx, val, p, l, r):
            if l == r:
                seg[p] = val
                return
            
            mid = (l + r) // 2
            if idx <= mid:
                update(idx, val, p << 1, l, mid)
            else:
                update(idx, val, p << 1 | 1, mid + 1, r)

            seg[p] = max(seg[p << 1], seg[p << 1 | 1])
            return
        
        def query(blk_l, blk_r, p, l, r):
            if blk_l <= l and r <= blk_r:
                return seg[p]
            
            mid = (l + r) // 2
            ret = 0
            if blk_l <= mid:
                ret = max(ret, query(blk_l, blk_r, p << 1, l, mid))
            if mid < blk_r:
                ret = max(ret, query(blk_l, blk_r, p << 1 | 1, mid + 1, r))
            return ret
        
        update(maxval, maxval, 1, 0, maxval)

        ans = []
        for q in queries:
            if q[0] == 1:
                # type 1: place an obstacle
                x = q[1]
                i = min(len(slist) - 1, bisect.bisect_right(slist, x))
                right = slist[i]
                left = slist[i - 1] if i > 0 else slist[0]
                update(x, x - left, 1, 0, maxval)
                update(right, right - x, 1, 0, maxval)
                bisect.insort(slist, x)
            else:
                # type 2: try to place a block
                x, sz = q[1], q[2]  # value x, required size of block
                i = min(len(slist) - 1, bisect.bisect_right(slist, x))
                prev = slist[0] if i == 0 else slist[i - 1]
                max_space = max(x - prev, query(0, prev, 1, 0, maxval))
                ans.append(max_space >= sz)

        return ans


'''
Fenwick tree (binary indexed tree) approach (time limit exceeded)

learnt from official editorial 2:
https://leetcode.com/problems/block-placement-queries/editorial/#approach-2-fenwick-tree
'''


import bisect


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        maxval = 50000

        # assume all obstacles already exist
        slist = [q[1] for q in queries if q[0] == 1]
        slist.append(0)
        slist.append(maxval)
        slist.sort()

        tree = [0] * (maxval + 1)

        def update(x, v):
            while x < len(tree):
                if v > tree[x]:
                    tree[x] = v
                x += x & -x

        def query(x):
            ret = 0
            while x > 0:
                if tree[x] > ret:
                    ret = tree[x]
                x -= x & -x
            return ret


        prev = 0
        for x in slist:
            if x == 0:
                continue
            update(x, x - prev)
            prev = x

        # proceed reversely
        ans = []
        for q in reversed(queries):
            if q[0] == 1:
                # remove an obstacle
                x = q[1]
                i = bisect.bisect_left(slist, x)
                prev_val = slist[i - 1]
                next_val = slist[i + 1]
                update(next_val, next_val - prev_val)
                slist.remove(x)
            else:
                # block
                x, sz = q[1], q[2]
                i = bisect.bisect_left(slist, x)
                if i < len(slist) and slist[i] == x:
                    prev_val = x
                else:
                    prev_val = slist[i - 1]
                max_space = max(query(prev_val), x - prev_val)
                ans.append(max_space >= sz)

        return ans[::-1]

