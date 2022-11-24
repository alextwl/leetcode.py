'''
2022/11/24 daily challenge

depth first search approach

it's easily TLE for many corner & large cases
so don't do too many so-called-optimization jobs!
don't track the path, don't maintain too many extra spaces such as visited cells blah blah...

just keep it simple,
return the result earlier,
eliminate those long-running annoying corner cases in the beginning, ...
and get accepted.
'''

import collections


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.wlen = len(word)
        self.board = board
        self.word = word

        # check if there were enough chars needed for the word.
        bc = collections.defaultdict(int)
        for x in range(self.m):
            for y in range(self.n):
                bc[board[x][y]] += 1
        wc = collections.Counter(word)
        for key, val in wc.items():
            if bc[key] < val:
                return False
        
        # manipulate all coordinates of possible begin character of word in the board.
        beginCoords = [(x, y) for x, row in enumerate(board) for y, val in enumerate(row) if val == word[0]]
        
        for begin in beginCoords:
            # time to search from the beginning (root)
            if self.dfs(begin[0], begin[1], 0):
                return True

        # word not found
        return False
        
    def dfs(self, x, y, wptr):
        '''
        :param x: x coordinate of the board
        :param y: y coordinate of the board
        :param wptr: the character index to be searched in the word
        '''
        # boundary check
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return False

        if self.board[x][y] != self.word[wptr]:
            return False

        # visit the char
        self.board[x][y] = '#'

        # search next char
        wptr += 1
        if wptr >= self.wlen:
            # all characters of the word are found.
            return True

        # push next coordinates to be searched
        for i, j in [(0,1), (1,0), (0,-1), (-1, 0)]:
            if self.dfs(x+i, y+j, wptr):
                return True

        # word not found in this branch, recover the cell
        self.board[x][y] = self.word[wptr-1]
        return False

