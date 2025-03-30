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


'''
dict + two pointer approach
'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {chr(ord('a') + i): 0 for i in range(26)}
        for i, c in enumerate(s):
            last_seen[c] = i
        
        ans = []
        # current partition's boundary
        p_left = p_right = 0
        for i, c in enumerate(s):
            # if there're more occurance later, extend the partition
            p_right = max(p_right, last_seen[c])

            if i == p_right:
                # the last occurance of c is included and ended here,
                # we can form a partition now.
                ans.append(i - p_left + 1)
                p_left = i + 1
        return ans

