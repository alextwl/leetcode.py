'''
2023/01/03 daily challenge
'''

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 1:
            # columns with length 1 are always sorted.
            return 0

        # counter for deleted columns
        columns_deleted = 0

        # check if columns were sorted.
        # transpose the matrix for the convenience.
        for column in zip(*strs):
            for i in range(1, len(column)):
                if column[i-1] > column[i]:
                    # the column is not sorted.
                    columns_deleted += 1
                    break

        return columns_deleted

