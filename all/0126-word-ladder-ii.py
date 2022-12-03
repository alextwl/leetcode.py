'''
2022/08/14 daily challenge

BFS from beginWord & DFS from endWord approach

learnt from
https://leetcode.com/problems/word-ladder-ii/discuss/2367587/Python-BFS-%2B-DFS-With-Explanation-Why-Optimization-Is-Needed-to-Not-TLE

all words are nodes and each word is visited once only by BFS,
and then do DFS from endWord in order to build answer pathes.

the judge is tough in 2022 and
it returns TLE if the optimization was insufficient (e.g. simply run BFS from beginWord.)
'''

import collections
import functools


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            # impossible to transform because the endWord is not in wordList.
            return []
        
        '''
        build a dict to query adjacency (descendent) words list from current word (key)
        '''
        childern_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                childern_dict[pattern].append(word)
        
        '''
        visit words by BFS from beginWord
        '''
        q = collections.deque([beginWord])
        visited = {beginWord: []}  # visited[next_word] = [from_words, ...]
        found = False  # flag of finding endWord
        while(q and not found):
            current_visited = dict()  # nodes visited at this level of depth
            
            # iterate nodes in the same level
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for nextWord in childern_dict[pattern]:
                        if nextWord == endWord:
                            '''
                            set flag to ensure the while loop will not continue searching the next level.
                            we don't stop it immediately because the problem requires
                            all the shortest transformation sequences == answers of the same level
                            '''
                            found = True
                        if nextWord not in visited:
                            if nextWord not in current_visited:
                                # the first visit
                                current_visited[nextWord] = [word]
                                '''
                                the next word is not yet visited and we need to traverse the next next word,
                                so add it to the queue for the next level.
                                '''
                                q.append(nextWord)
                            else:
                                current_visited[nextWord].append(word)
                '''
                if the next word was visited in the previous level of depth,
                no need to revisit it again.
                '''
            # update visited nodes of current level to the global visited dict.
            visited.update(current_visited)
        
        '''
        time to build answers by DFS from endWord. (backtrace the visited nodes)
        '''
        def dfs(word: str, visited: dict):
            '''
            it returns the pathes of transformation sequence.
            '''
            if word == beginWord:
                return [[beginWord]]
            if word not in visited:
                # the transformation will not reach endWord from the input word.
                return []
            
            pathes = []
            for prevWord in visited[word]:
                pathes.extend(dfs(prevWord, visited))
            # add current word to all pathes
            for path in pathes:
                path.append(word)

            return pathes
        
        return dfs(endWord, visited)

