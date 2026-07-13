'''
2024/02/02 daily challenge
2026/07/13 daily challenge
'''


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def find_start(low, high):
            # find the start digits
            lsd = int(str(low)[0])  # leftmost digit
            width = len((str(low)))

            for lsd in range(lsd, 10-width+1):
                curr = lsd
                for i in range(lsd+1, lsd+width):
                    curr = curr * 10 + i
                if curr > high:
                    return None
                if curr >= low:
                    return curr
            return None
        
        start = find_start(low, high)
        if start is None:
            # try to plus one more digit
            start = find_start(10 ** (len(str(low))), high)
            if start is None:
                # start digits not found even if plus one more digit
                return []
        
        lsd = int(str(start)[0])
        start_width = len(str(start))
        max_width = len(str(high))
        
        ans = []
        
        for width in range(start_width, max_width + 1):
            for lsd in range(lsd, 10-width+1):
                curr = lsd
                for i in range(lsd+1, lsd+width):
                    curr = curr * 10 + i
                if curr > high:
                    break
                ans.append(curr)
            # reset lsd for next loop of width
            lsd = 1

        return ans


'''
recursion + string manipulation approach

fix rightmost digit and try all possible values by concatenating digits
'''


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s_dig = "0123456789"
        s_low, s_high = str(low), str(high)
        len_low, len_high = len(s_low), len(s_high)
        ans = []
        for start in range(1, 10):
            stack = []
            for i in range(start, 10):
                stack.append(s_dig[i])
                if len(stack) > len_high:
                    break
                if len(stack) >= len_low:
                    val = int(''.join(stack))
                    if low <= val <= high:
                        ans.append(val)
        return sorted(ans)

