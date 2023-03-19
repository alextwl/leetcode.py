'''
2023/03/19 daily challenge

Trie approach
'''


class Trie:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        '''
        add the input word to the Trie.
        '''
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        '''
        search the word in the Trie.
        '''
        currents = [self.root]
        for c in word:
            nexts = []
            # BFS
            if c == '.':
                for node in currents:
                    nexts.extend(node.children.values())
            else:
                for node in currents:
                    if c in node.children:
                        nexts.append(node.children[c])
            currents = nexts
        
        return any(node.endOfWord for node in currents)

