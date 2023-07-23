'''
2023/07/23 daily challenge

dynamic programming approach

e.g. k=5,

          allPossibleFBT(5)                              allPossibleFBT(5)
                 |                                              |
       +---------+--------+                           +---------+--------+
       |                  |                           |                  |
allPossibleFBT(1)  allPossibleFBT(3)           allPossibleFBT(3)  allPossibleFBT(1)
                          |                           |
                +---------+--------+                 ...
                |                  |
         allPossibleFBT(1)  allPossibleFBT(1)

'''

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        '''
        n must be an odd, or no possible FBT can be generated.
        (the root node always costs one node quota.)
        '''
        if n & 1 == 0:
            return []
        
        '''
        dp space: a cache of allPossibleFBT() -> List[TreeNode]
        dp[k] = allPossibleFBT(k)
        '''
        dp = [[] for _ in range(n+1)]
        '''
        dp[0] is useless,
        dp[1] contains only a root node.
        '''
        dp[1] = [TreeNode()]
        
        '''
        allPossibleFBT(1) is generated, let's start from k=3 to k=n.
        '''
        for k in range(3, n+1, 2):
            '''
            generate allPossibleFBT(k)
            
            the number of descendents is always k-1 which substracts root node from k.
            '''
            for i in range(1, k-1, 2):
                # i = the left node's argument
                j = (k-1) - i  # the right node's argument
                
                for left in dp[i]:
                    for right in dp[j]:
                        '''
                        generate root nodes for all possible FBTs by reusing cached FBTs
                        '''
                        node = TreeNode(0, left, right)
                        dp[k].append(node)

        return dp[-1]  # == allPossibleFBT(n)

