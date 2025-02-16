'''
2025/02/16 daily challenge

backtracking + bitmask approach
'''


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def dfs(i, seq, bitmask):
            if bitmask == 0:
                # all integer used, return fully-constructed sequence
                return seq
            # search the next empty slot
            while i < len(seq) and seq[i]:
                i += 1
            if i == len(seq):
                return []
            # iterate from the most significant bit to the least significant bit
            for k in range(bitmask.bit_length(), 0, -1):
                k_mask = (1 << (k - 1))
                if bitmask & k_mask:
                    # sanity check
                    if k != 1 and (i + k >= len(seq) or seq[i+k]):
                        continue
                    # place k into the sequence
                    next_seq = seq.copy()
                    next_seq[i] = k
                    if k > 1:
                        next_seq[i + k] = k
                    ret_seq = dfs(i + 1, next_seq, bitmask - k_mask)
                    if ret_seq:
                        return ret_seq
            return []
        return dfs(0, [0] * (n * 2 - 1), (1 << n) - 1)

