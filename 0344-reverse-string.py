class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s) - 1
        middle = len(s) // 2
        
        while(low < middle):
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        
        return

        # oneliner
        for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]
        return
