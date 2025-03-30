'''
2025/03/30 daily challenge

stack + set approach
'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack = []  # (partition len, partition set)
        seen = set()  # overall set of seen chars

        for c in s:
            if c in seen:
                p_len, p_set = stack.pop()
                p_len += 1
                # combine previous partitions until it has c
                while stack and c not in p_set:
                    prev_len, prev_set = stack.pop()
                    p_len += prev_len
                    p_set.update(prev_set)
                stack.append([p_len, p_set])
            else:
                # create a new partition
                stack.append([1, {c}])
                seen.add(c)
        return [i for i, _ in stack]

