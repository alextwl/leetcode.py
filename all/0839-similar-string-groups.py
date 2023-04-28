'''
2023/04/28 daily challenge

union find approach

calculate the number of groups according to the counts of union occured.
'''

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(x, y):
            count = 0  # the number of different positions
            for c1, c2 in zip(x, y):
                if c1 != c2:
                    count += 1
                    if count > 2:
                        return False
            '''
            Since the constraints guarantee all words
            in strs have the same length and are anagrams of each other,
            so no need to verify if the swapped chars were valid or not.
            '''
            return True  # (x == y) or count==2
        
        n = len(strs)

        # Union find structure
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            '''
            :return: True if combined, False if already united
            :rtype: bool
            '''
            x, y = find(x), find(y)
            if x == y:
                return False
            if x > y:
                parent[x] = y
            else:
                parent[y] = x
            return True

        group_counts = n  # initial value: each str is a group.
        for i in range(0, n-1):
            for j in range(i+1, n):
                if isSimilar(strs[i], strs[j]) and union(i, j):
                    # subtract group counts if there're 2 groups combined.
                    group_counts -= 1

        return group_counts

