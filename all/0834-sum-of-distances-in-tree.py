'''
2022/12/22 daily challenge

subtree sum + depth first search (postorder+preorder) approach
learnt from official solution
'''

import collections


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        build an undirected connected tree first.
        all nodes connected have no duplicate neighbors so use set.
        '''
        nodes = collections.defaultdict(set)
        for ai, bi in edges:
            nodes[ai].add(bi)
            nodes[bi].add(ai)

        '''
        the node count of subtrees for each node as a root
        initialized from 1 node (== root itself.)
        '''
        stCount = [1] * n
        '''
        the answer space, it stores sums in 2 stages.
        (1) all subtree sums after postorder DFS
        (2) sum of distances (final answer) after preorder DFS
        '''
        dp = [0] * n

        def post_dfs(stRoot, parent):
            '''
            count nodes & sum of the subtree with specified root node.

            :param stRoot: node as a root of a subtree
            :param parent: the parent node
                           (can be None if stRoot is the ultimate root of the input tree)
            '''
            for child in nodes[stRoot]:
                '''
                since it's an undirected tree,
                child can be connected back to its parent,
                so don't traverse parent.
                '''
                if child != parent:
                    post_dfs(child, stRoot)
                    # child's subtree count completed, accumulate it.
                    stCount[stRoot] += stCount[child]
                    '''
                    stRoot's sum += child subtree's sum + child node count (each child node to stRoot costs additional distance of 1.)
                    '''
                    dp[stRoot] += dp[child] + stCount[child]
        
        def pre_dfs(iRoot, parent):
            '''
            we run preorder traversal here because
            the parent node's final answer is always calculated earlier
            and all childern's answer need to refer it.

            :param iRoot: node as a root of the entire input tree
            :param parent: the parent node of iRoot in the original top-down angle of view
                           (can be None if iRoot is the ultimate root of the input tree)
            '''
            for child in nodes[iRoot]:
                if child != parent:
                    '''
                    think we are going to move root flag from iRoot (child's parent)to child.

                    child's sum of distance = 
                        iRoot's subtree sum
                        - node count of child subtree (because we are moving root flag to child, the distance of each node in child's subtree to child node itself reduced one, so total reduction is equal to subtree's node count.)
                        + node count outside of child's subtree (the distance of these nodes to this child node is increased by 1 per node.)
                    '''
                    dp[child] = dp[iRoot] - stCount[child] + (n - stCount[child])
                    pre_dfs(child, iRoot)
    
        # build subtree sums first, from the ultimate root 0.
        post_dfs(0, None)
        # calculate the final answer (aka sum of distances for each node as a root)
        pre_dfs(0, None)

        return dp

