'''
2022/09/26 daily challenge

Union-find (Disjoint set) approach
'''

import string

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        '''
        default all char's root to itself.
        Union-find structure, use dict as a forest graph.
        '''
        ufs = {x: x for x in string.ascii_lowercase}
        
        def find(x):
            if x != ufs[x]:
                # find the root of the set and update x's root.
                ufs[x] = find(ufs[x])
            return ufs[x]
        
        # process all '==' equations
        for a, op, _, b in equations:
            if op == '=':
                # update root of a's root to the root of b
                ufs[find(a)] = find(b)
        
        # search any 'a!=b' which 'a==b' also existed.
        return not any(op == '!' and find(a) == find(b) for a, op, _, b in equations)
