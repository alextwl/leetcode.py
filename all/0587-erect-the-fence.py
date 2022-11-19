'''
2022/11/19 daily challenge

wrap all trees with minimum length of boundary.

Jarvis algorithm approach

learnt from official solution.

start from the leftmost tree and connect to the most counterclockwise relative to the last tree.

time=O(trees*outerTrees), space=O(trees)
'''

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r) -> int:
            '''
            p is a tree coordinate added to the boundary.
            q & r are candidates.
            
            it returns the cross product of vector p->q and vector q->r.
            if the value was negative, then q is more counterclockwise to p than r.
            '''
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        
        def inBetween(p, i, j):
            '''
            return if i & j are collinear relative to p and i is in between p & j.
            '''
            return ((i[0] >= p[0] and i[0] <= j[0]) or (i[0] <= p[0] and i[0] >= j[0])) and \
                   ((i[1] >= p[1] and i[1] <= j[1]) or (i[1] <= p[1] and i[1] >= j[1]))
        
        '''
        corner case: if the number of trees was <= 3,
        all trees are enclosed and also wrapped with rope.
        '''
        totalTrees = len(trees)
        if totalTrees <= 3:
            return trees

        # outer tree indexes wrapped with rope.
        fence = set()
        # the index of the leftmost tree (compared with x coordinate of all trees) in trees[].
        leftmost_tree = min(enumerate(trees), key=lambda t: t[1][0])[0]
        
        p = leftmost_tree
        pCoord = trees[p]
        leftmost_added = False
        #print("leftmost p=%d" % p)

        while(1):
            q = p + 1
            if q >= totalTrees:
                q = 0
            qCoord = trees[q]
            # select the most counterclockwise tree to p.
            for i, iCoord in enumerate(trees):
                if orientation(pCoord, iCoord, qCoord) < 0:
                    q = i
                    qCoord = iCoord
                    #print("set q=%d" % q)
            # add all collinear trees between p & q to the fence.
            for i, iCoord in enumerate(trees):
                if i != p and i != q and \
                        orientation(pCoord, iCoord, qCoord) == 0 and \
                        inBetween(pCoord, iCoord, qCoord):
                    fence.add(i)
                    if i == leftmost_tree:
                        '''
                        set the break flag if connected to the first tree
                        or the infinite while loop may occur.
                        '''
                        leftmost_added = True
                    #print("add collinear i=%d" % i)
                    
            # finally add q to the fence.
            fence.add(q)
            #print("add collinear q=%d" % q)
            
            # stop when the rope connected to the first tree again.
            if q == leftmost_tree or leftmost_added:
                break
            p = q
            pCoord = qCoord
        
        return [trees[i] for i in fence]

