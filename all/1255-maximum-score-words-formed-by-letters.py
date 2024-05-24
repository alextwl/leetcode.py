'''
2024/05/24 daily challenge

depth first search backtracing approach

python >= 3.10: counter comparsion used
'''

import collections


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_quota = collections.Counter(letters)

        # build word counters and strip all words with exceeded number of letters used
        word_counters = []
        for w in words:
            cnt = collections.Counter(w)
            if letters_quota >= cnt:
                word_counters.append(cnt)

        n = len(word_counters)
        max_score = 0

        def dfs(i, current_counter):
            if i == n:
                current_score = sum(score[ord(c) - ord('a')] * num for c, num in current_counter.items())
                nonlocal max_score
                max_score = max(max_score, current_score)
                return

            # subset with word_counters[i] included
            current_counter += word_counters[i]
            # check if the number of used letters exceeded the quota or not.
            if letters_quota > current_counter:
                dfs(i + 1, current_counter)
            elif letters_quota == current_counter:
                # shortcut: maximum expected score appeared
                dfs(n, current_counter)
                return

            current_counter -= word_counters[i]
            # subset without word_counters[i]
            dfs(i + 1, current_counter)

        dfs(0, collections.Counter())

        return max_score

