'''
@oiu850714 told me this is evil and full of chaos.

intuitive approach, as a kind of DFS?
the idea is to find the next cell and check if the ball stucks.

Runtime: 195 ms, faster than 97.95% of Python3 online submissions for Where Will the Ball Fall.
'''

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        width = len(grid[0])
        height = len(grid)
        
        ans = [-1] * width
        
        for start_col in range(0, width):
            from_top = True
            row = 0
            col = start_col
            
            while row < height:
                if grid[row][col] == 1:
                    if from_top:
                        '''
                        ball is dropped from the top and falls to the right cell.
                        '''
                        next_col = col + 1
                        next_row = row
                        from_top = False
                        
                        if next_col >= width or grid[next_row][next_col] == -1:
                            '''
                            get stuck in the right wall or between columns.
                            '''
                            break
                    else:
                        '''
                        ball is dropped from the left cell.
                        '''
                        next_col = col
                        next_row = row + 1
                        from_top = True
                        
                else:
                    if from_top:
                        '''
                        ball is dropped from the top and falls to the left cell.
                        '''
                        next_col = col - 1
                        next_row = row
                        from_top = False
                        
                        if next_col < 0 or grid[next_row][next_col] == 1:
                            '''
                            get stuck in the left wall or between columns.
                            '''
                            break
                    else:
                        '''
                        ball is dropped from the right cell.
                        '''
                        next_col = col
                        next_row = row + 1
                        from_top = True
                
                # ball continues falling
                row = next_row
                col = next_col
            else:
                '''
                ball falls out of the box.
                the last col is always the last column where ball falls.
                '''
                ans[start_col] = col
        
        return ans
