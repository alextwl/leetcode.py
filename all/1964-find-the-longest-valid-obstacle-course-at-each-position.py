'''
2023/05/07 daily challenge

dynamic programming + binary search approach

try to build longest obstacle cource with shared dp sequence.
'''


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        seq = []  # the dp space of obstacle sequence
        ans = []  # the list of lengths of longest valid obstacle course

        for ob in obstacles:
            # search the insertion position of the end of longest valid obstacle sequence
            left, right = 0, len(seq)-1
            while(left <= right):
                mid = left + ((right-left)>>1)
                if seq[mid] <= ob:
                    # if seq[mid]==ob, that means both seq[mid] and ob can be included in the sequence together.
                    left = mid + 1
                else:
                    right = mid - 1
            
            if left == len(seq):
                seq.append(ob)
            else:
                '''
                override seq[left] and the result of seq[:left+1] is the sequence of
                longest valid obstacle course for this position of ob.

                the sequence containing the original seq[left] won't be the longest,
                so it can be overrided safely.
                '''
                seq[left] = ob
            #print(seq)
            ans.append(left+1)

        return ans

