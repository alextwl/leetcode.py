'''
2024/01/28 daily challenge

prefix sum approach
'''


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        '''
        each row's (horizontal) prefix sum
        '''
        for row in matrix:
            for y in range(n-1):
                row[y+1] += row[y]
        
        ans = 0
        '''
        iterate from (x1, *) to (x2, *) with all y-coordinates.
        '''
        for x2 in range(m):
            for x1 in range(x2, -1, -1):
                '''
                bottom-up submatrix prefix sums
                '''
                if x1 == x2:
                    prefix = matrix[x2]
                else:
                    prefix = [prev[y]+matrix[x1][y] for y in range(n)]
                
                '''
                base case: for any submatrics including the leftmost cell
                if its sum equals target (== the diff is 0)
                then it's a valid submatrix.
                '''
                # counts[diff or a sum of submatrix] = the number of seen occurance
                counts = {0: 1}
                
                '''
                cases when we count up:
                (1) diff == 0: the sum of the submatrix equals target.
                    (note: such matrix always includes the leftmost cell
                     due to the nature of a complete prefix sum.)

                (2) diff != 0 but found in counts[]:
                
                given target = 4,
                row = [1, 2, 2, -4, 3, 1],
                prefix = [1, 3, 5, 1, 4, 5].

                for prefix[0]=1, diff=-3, diff not in counts[].
                counts[1] = 1.

                for prefix[1]=3, diff=-1, diff not in counts[].
                counts[3] = 1.

                for prefix[2]=5, diff=1, counts[1] == 1, a valid submatrix found.
                we find row[1:3] (== [2, 2]) as a valid submatrix
                by subtracting prefix[0] (counted in counts[1]) from prefix[2].
                ans += 1
                counts[5] = 1.

                for prefix[3]=1, diff=-3, diff not in counts[].
                counts[1] += 1 (so counts[1] == 2 now.)

                for prefix[4]=4, diff=0, diff matches base case.
                we find row[0:5] (== [1, 2, 2, -4, 3]) is a valid submatrix.

                for prefix[5]=5, diff=1, counts[1] == 2, two valid submatrics found.
                we find both row[4:6] (== [3, 1]) and row[1:6] (== [2, 2, -4, 3, 1])
                are valid because we can subtract prefix[0] or prefix[3] from prefix[5]
                to find these two valid submatrics.
                ans += 2
                counts[5] += 1 (so counts[5] == 2 now.)

                that's the reason why we memorize counts[1]==2 as the occurance of seen prefix sums.
                '''
                for sub in prefix:
                    if (diff := sub - target) in counts:
                        ans += counts[diff]
                    
                    counts[sub] = counts.get(sub, 0) + 1
                
                prev = prefix
        
        return ans
