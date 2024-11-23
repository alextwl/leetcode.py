'''
2024/11/23 daily challenge

brute force approach
'''


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        ans = [['.'] * m for _ in range(n)]
        
        for j, row in enumerate(reversed(box)):
            i = 0  # the next row to be filled
            stone = 0  # the number of stones to be placed
            for cell in row:
                if cell == '.':
                    i += 1
                elif cell == '#':
                    stone += 1
                else:
                    # stationary obstacle found
                    # place the stones first
                    for _ in range(stone):
                        ans[i][j] = '#'
                        i += 1
                    stone = 0  # reset
                    
                    # fill the obstacle
                    ans[i][j] = '*'
                    i += 1
            # place the stone if available
            for _ in range(stone):
                ans[i][j] = '#'
                i += 1

        return ans

