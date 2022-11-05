'''
dict tree approach

learnt from official solution
'''

class TrieNode:
    def __init__(self, value: str = ""):
        '''
        :param value: initialize the value of the node.
        :type value: str
        
        if it's root node, set value to empty string.
        '''
        self.value = value
        self.endOfWord = False  # if any word terminated here, set to True.
        self.childern = dict()  # a dict of childern nodes, the key is child's value.


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.childern:
                # child node found
                node = node.childern[c]
            else:
                # child node not found, create new node for c
                child = TrieNode(c)
                node.childern[c] = child
                node = child
        # set flag to indicate a word ends here.
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.childern:
                # a char of word not found
                return False
            node = node.childern[c]
        
        '''
        although the path is found, we also need to check the flag.
        it fails if the input was just a prefix of another word.
        '''
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.childern:
                # a char of word not found
                return False
            node = node.childern[c]
        '''
        similar to self.search() but it always returns True regardless of node.endOfWord.
        '''
        return True

