'''
2026/01/30 daily challenge

Trie + Floyd-Warshall algorithm + top-down dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/minimum-cost-to-convert-string-ii/editorial/#approach-trie--floyds-algorithm--dynamic-programming
'''


ASCII_A = ord('a')
INF = float('inf')


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # shortcut
        if source == target:
            return 0

        src_len = len(source)

        # array-based Trie structure
        trie = [[-1] * 26]
        word_id = [-1]  # id of a word with terminal trie of last char
        idx = -1

        def trie_new_node():
            nonlocal trie, word_id
            trie.append([-1] * 26)
            word_id.append(-1)
            return len(trie) - 1  # index of word_id

        def trie_add(word):
            nonlocal trie, word_id, idx
            node = 0
            for c in word:
                c = ord(c) - ASCII_A
                next_node = trie[node][c]
                if next_node == -1:
                    next_node = trie_new_node()
                    trie[node][c] = next_node
                node = next_node
            if word_id[node] == -1:
                idx += 1
                word_id[node] = idx
            return word_id[node]

        # build edge & distance mapping
        edges = []
        for i, (s0, s1, w) in enumerate(zip(original, changed, cost)):
            x = trie_add(s0)
            y = trie_add(s1)
            edges.append((x, y, w))

        total_word = idx + 1  # count of unique words
        distance = [[INF] * total_word for _ in range(total_word)]

        # base case: same word to same word has length of zero.
        for i in range(total_word):
            distance[i][i] = 0

        # build distances of direct edges
        for x, y, w in edges:
            if w < distance[x][y]:
                # there may be multiple edges between same pair of two edges,
                # select the shortest.
                distance[x][y] = w

        # Floyd-Warshall algorithm
        for k, k_to in enumerate(distance):
            for i, i_to in enumerate(distance):
                i2k = i_to[k]
                if i2k == INF:
                    # k is unreachable from i,
                    # no need to iterate for all destination to j via k.
                    continue
                for j in range(total_word):
                    i_k_j = i2k + k_to[j]  # i->k + k->j
                    if i_to[j] > i_k_j:
                        i_to[j] = i_k_j
        
        # dynamic programming
        # dp[j] = minimum cost to convert source into target with source[:j] changed,
        # leaving source[j:] untouched.
        dp = [INF] * (src_len + 1)
        dp[0] = 0
        src = [ord(c) - ASCII_A for c in source]
        dst = [ord(c) - ASCII_A for c in target]

        for j in range(src_len):
            if dp[j] >= INF:
                continue

            base = dp[j]
            if src[j] == dst[j] and base < dp[j + 1]:
                dp[j + 1] = base

            u = v = 0
            for i in range(j, src_len):
                u, v = trie[u][src[i]], trie[v][dst[i]]
                if u == -1 or v == -1:
                    # Trie node terminated, no need to search further
                    break
                uid = word_id[u]
                vid = word_id[v]
                if uid != -1 and vid != -1:
                    # possible conversion found, try to minimize cost
                    w = distance[uid][vid]
                    if w != INF:
                        new_dist = base + w
                        if new_dist < dp[i + 1]:
                            dp[i + 1] = new_dist
        ans = dp[-1]
        return -1 if ans >= INF else ans

