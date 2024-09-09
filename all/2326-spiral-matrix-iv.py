'''
2024/09/09 daily challenge

simulation approach
'''


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # concurrent boundaries
        up, down, left, right = 0, m-1, 0, n-1
        
        mat = [[-1] * n for _ in range(m)]
        
        x, y = 0, 0
        direction = 0  # 0..3: go right, go down, go left, go up
        
        while(head and up <= x <= down and left <= y <= right):
            mat[x][y] = head.val
            head = head.next
            
            if direction == 0:
                if y == right:
                    direction = 1
                    x += 1
                    up += 1
                else:
                    y += 1
            elif direction == 1:
                if x == down:
                    direction = 2
                    y -= 1
                    right -= 1
                else:
                    x += 1
            elif direction == 2:
                if y == left:
                    direction = 3
                    x -= 1
                    down -= 1
                else:
                    y -= 1
            else:
                if x == up:
                    direction = 0
                    y += 1
                    left += 1
                else:
                    x -= 1

        return mat


'''
simplified but slower ver
'''


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        mat = [[-1] * n for _ in range(m)]
        x, y = 0, 0
        direction = 0  # 0..3: go right, go down, go left, go up
        vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while(head and 0 <= x < m and 0 <= y < n):
            mat[x][y] = head.val
            head = head.next

            dx, dy = vectors[direction]
            dx += x
            dy += y

            if not (0 <= dx < m and 0 <= dy < n) or mat[dx][dy] != -1:
                direction = (direction + 1) % 4
                dx, dy = vectors[direction]
                x += dx
                y += dy
            else:
                x, y = dx, dy

        return mat

