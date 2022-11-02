'''
2022/11/02 daily challenge

breadth-first search approach, learnt from official solution.

according to the problem,
each step of mutation must be valid and recorded in the bank,
so we can try to replace each character of a gene
and check if it's in the bank.
'''

import collections


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = collections.deque([(start, 0)])  # ('GENE', mutated steps)
        visited = {start}  # start gene is assumed to be valid.
        
        while q:
            gene, steps = q.popleft()
            
            if gene == end:
                return steps
            
            '''
            search each gene string with replaced 1 char
            and check if it's in the bank or not.
            '''
            for g in "ACGT":
                for i in range(0, 8):
                    mutated_gene = gene[:i] + g + gene[i+1:]
                    if mutated_gene not in visited and mutated_gene in bank:
                        '''
                        only a gene recorded in the bank is a valid gene
                        and can be mutated (enqueued) again.
                        '''
                        q.append((mutated_gene, steps+1))
                        visited.add(mutated_gene)

        # impossible to traverse from start to end.
        return -1

