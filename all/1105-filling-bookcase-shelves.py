'''
2024/07/31 daily challenge

dynamic programming approach (bottom-up)
'''


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)  # dp[i] = the minimum height of shelves with books[:i]
        # base case
        it = enumerate(books)
        _, current_book = next(it)
        dp[1] = current_book[1]

        for i, (book_thick, book_height) in it:
            # assume creating a new shelf with current book
            width_remaining = shelfWidth - book_thick
            shelf_height = book_height
            dp[i+1] = shelf_height + dp[i]

            j = i - 1
            # try to include a previous book j onto the current shelf
            while j >= 0 and (width_remaining := width_remaining - books[j][0]) >= 0:
                shelf_height = max(shelf_height, books[j][1])
                dp[i+1] = min(dp[i+1], shelf_height + dp[j])
                j -= 1

        return dp[-1]


'''
dynamic programming approach (recursive top-down)
'''

import functools


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @functools.lru_cache(maxsize=shelfWidth)
        def dp(i):
            # returns the minimum height of books[i:]
            if i == n:
                return 0

            remaining_width = shelfWidth - books[i][0]
            # init with creating a new shelf for current book
            shelf_height = books[i][1]
            min_height = shelf_height + dp(i+1)

            j = i + 1
            while j < n and (remaining_width := remaining_width - books[j][0]) >= 0:
                shelf_height = max(shelf_height, books[j][1])
                min_height = min(min_height, shelf_height + dp(j+1))
                j += 1

            return min_height

        return dp(0)

