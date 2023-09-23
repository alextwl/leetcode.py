'''
2023/09/23 daily challenge

depth first search approach
'''

import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPredecessor(a: str, b: str):
            '''
            check if a is a predecessor of b.
            '''
            diff = 0
            it_a = iter(a)
            char_a = next(it_a)
            
            for char_b in b:
                if char_b != char_a:
                    diff += 1
                    if diff > 1:
                        return False
                else:
                    try:
                        char_a = next(it_a)
                    except StopIteration:
                        char_a = None

            return True if diff == 1 else False
        
        # len2words[length of word] = [word, ...]
        len2words = collections.defaultdict(list)
        for w in words:
            len2words[len(w)].append(w)
        
        # g[predecessor] = {successor, ...}
        g = collections.defaultdict(set)
        for predecessor_len in sorted(len2words.keys()):
            predecessors = len2words[predecessor_len]
            successors = len2words[predecessor_len + 1]
            for a in predecessors:
                for b in successors:
                    if a == b:
                        continue
                    if isPredecessor(a, b):
                        g[a].add(b)
        
        ans = 0
        word_max_chain = collections.defaultdict(int)
        # run DFS in order of ascending word length
        stack = [(w, 1) for _, l in sorted(len2words.items(), reverse=True) for w in l]
        while(stack):
            w, k = stack.pop()
            if word_max_chain[w] >= k:
                continue
            
            word_max_chain[w] = k

            k += 1
            for child in g[w]:
                stack.append((child, k))
        
        return max(word_max_chain.values())


'''
dynamic programming approach

since the input is limited in 1 <= words[i].length <= 16,
it's possible to use exhaustive method to delete any char from each word
and accumulate the chain length by dynamic programming.

learnt from
https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
'''

import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        querying any missing predecessor word returns zero of chain's length,
        and we can initialize any successor word with 1 of chain's length.
        '''
        dp = collections.defaultdict(int)
        
        # iterate word in ascending word length order
        for w in sorted(words, key=len):
            # dp[w] = max(dp[any-single-char-deleted-from w] + 1)
            dp[w] = max(dp[w[:i] + w[i+1:]] + 1 for i in range(len(w)))
        
        return max(dp.values())

