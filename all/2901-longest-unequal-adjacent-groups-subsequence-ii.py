'''
2025/05/16 daily challenge

dynamic programming approach
'''


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        len_grps = [list() for _ in range(11)]
        for i, w in enumerate(words):
            len_grps[len(w)].append(i)

        def is_valid_adjacent(w1, w2):
            hamming_dist = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    hamming_dist += 1
                    if hamming_dist > 1:
                        return False
            return hamming_dist == 1

        # max_prefix_len[i] = the maximum subsequence length ending at i
        max_prefix_len = [1] * len(words)
        # max_seq_prev[i] = the index prior to current position i in the longest subsequence ending at i
        max_seq_prev = [None] * len(words)
        max_seq_len = 0  # the maximum subsequence length
        max_seq_end = 0  # the index of longest subsequence ending at
        # search by word lengthes
        for lg in len_grps:
            if not lg: continue

            # O(n**2) search
            for j in range(len(lg) - 1):
                i = lg[j]  # convert to words[] index
                prev_group = groups[i]  # the group of words[i]
                curr_len = max_prefix_len[i] + 1
                for k in range(j + 1, len(lg)):
                    kk = lg[k]  # convert to words[] index

                    if prev_group != groups[kk] and \
                            is_valid_adjacent(words[i], words[kk]) and \
                            max_prefix_len[kk] < curr_len:
                        max_prefix_len[kk] = curr_len
                        max_seq_prev[kk] = i
                        if max_seq_len < curr_len:
                            max_seq_len = curr_len
                            max_seq_end = kk
        # build answer reversely
        ans = []
        prev = max_seq_end
        while prev is not None:
            ans.append(words[prev])
            prev = max_seq_prev[prev]
        ans.reverse()
        return ans

