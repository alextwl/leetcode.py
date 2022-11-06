'''
2022/09/27 daily challenge

intuitive: calculate the distances from L & R dominoes
time=O(3n), space=O(2n)

note: more efficient algos are avail from official solutions.
'''

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        total = len(dominoes)
        
        # distance == -1 means it does not fall to the left/right pushes
        distance2L = [-1] * total
        distance2R = [-1] * total
        
        '''
        count distance from L starting from right bound.
        '''
        distance = -1
        for i, domino in reversed(list(enumerate(dominoes))):
            if domino == 'L':
                distance = 0
            elif domino == 'R':
                # disable distance growth
                distance = -1
            elif distance >= 0:
                # increment distance from L
                distance += 1
                distance2L[i] = distance

        '''
        count distance from R starting from left bound.
        '''
        distance = -1
        for i, domino in enumerate(dominoes):
            if domino == 'R':
                distance = 0
            elif domino == 'L':
                # disable distance growth
                distance = -1
            elif distance >= 0:
                # increment distance from R
                distance += 1
                distance2R[i] = distance
        
        '''
        compare both side of distance and calculate answer
        '''
        ans = list()
        for i, domino in enumerate(dominoes):
            if domino == '.':
                if distance2L[i] >= 0 and distance2R[i] < 0:
                    ans.append('L')
                elif distance2R[i] >= 0 and distance2L[i] < 0:
                    ans.append('R')
                elif distance2L[i] > distance2R[i]:
                    ans.append('R')
                elif distance2L[i] < distance2R[i]:
                    ans.append('L')
                else:
                    ans.append(domino)
            else:
                ans.append(domino)
        
        return ''.join(ans)
