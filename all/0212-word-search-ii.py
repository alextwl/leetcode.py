'''
2022/11/05 daily challenge

learnt from
https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).

the hard part is that optimization is necessary or it TLE.
'''

import collections


class TrieNode:
    '''
    it's a simplified version of Trie (see problem 208 for full ver)
    since the DFS procedure was out-of-box,
    the class Trie & some TrieNode functions are not implemented. 
    '''
    def __init__(self):
        self.childern = collections.defaultdict(TrieNode)
        self.endOfWord = False
    
    def insert(self, word):
        '''
        ported from class Trie.
        '''
        node = self
        for c in word:
            node = node.childern[c]
        node.endOfWord = True


class Solution:
    def __init__(self):
        self.remaining_count = 0  # the count of remaining words to be searched.
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsFound = []  # answer space
        
        '''
        First insert all targeted words to Trie root.
        '''
        root = TrieNode()
        for word in words:
            root.insert(word)
        self.remaining_count = len(words)
        
        # start searching all cells.
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                self.dfs(board, root, i, j, "", wordsFound)
        
        return wordsFound
    
    def dfs(self, board: List[List[str]], node: TrieNode, i: int, j: int, prefix: str, ans: list):
        '''
        :param board: input board of characters
        :param node: a TrieNode instance to be searched.
        :param i: coordinate of board
        :param j: coordinate of board[i]
        :param prefix: a common prefix of words found, and to be concatenated to next character.
        :param ans: answer space.
        '''
        if node.endOfWord:
            # current prefix found is a valid word, append it to answer.
            ans.append(prefix)
            node.endOfWord = False  # to prevent duplicate answer found from different path
            self.remaining_count -= 1
        
        if not self.remaining_count:
            # all words are found, no need to search deeper. (or it TLE.)
            return
        
        # boundary check
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        # search the char of the input coordinate
        char = board[i][j]
        child = node.childern.get(char)
        if child is None:
            # chat not found, stop searching on the current prefix.
            return
        
        # override the cell temporarily in order to prevent from using the cell more than once.
        board[i][j] = '*'
        
        # search the next cells of 4 directions
        prefix = prefix + char
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            self.dfs(board, child, i+x, j+y, prefix, ans)
        
        # recover the cell or the another prefix search will fail.
        board[i][j] = char
        
        # remove the child which has no further decendents to speed up. (or it TLE.)
        if not child.childern:
            del node.childern[char]

        return

