'''
2024/12/19 daily challenge

counter approach
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt0 = [0] * 10
        cnt1 = cnt0.copy()

        chunks = 0
        for v0, v1 in zip(arr, sorted(arr)):
            cnt0[v0] += 1
            cnt1[v1] += 1
            if cnt0 == cnt1:
                chunks += 1

        return chunks


'''
monotonic stack approach

the stack stores max elements of each chunk,
so its length is the number of chunks.
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []  # max elements of each chunk

        for v in arr:
            if not stack or v > stack[-1]:
                stack.append(v)
            else:
                # merge v and last chunk
                max_val = stack[-1]
                # merge chunks whose max elements were larger than v
                while stack and v < stack[-1]:
                    stack.pop()
                stack.append(max_val)

        return len(stack)

