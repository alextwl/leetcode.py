'''
2025/09/21 daily challenge

sorted list approach
'''


import bisect
import collections


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.copies = [collections.defaultdict(dict) for _ in range(n)]  # d[shop][movie] = price
        self.movies = collections.defaultdict(list)  # (price, shop)
        self.rented = []  # (price, shop, movie)

        for shop, movie, price in entries:
            self.copies[shop][movie] = price
            self.movies[movie].append((price, shop))
        
        for shops in self.movies.values():
            shops.sort()

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.copies[shop][movie]
        i = bisect.bisect_left(self.movies[movie], (price, shop))
        self.movies[movie].pop(i)
        t = (price, shop, movie)
        j = bisect.bisect_left(self.rented, t)
        self.rented.insert(j, t)

    def drop(self, shop: int, movie: int) -> None:
        price = self.copies[shop][movie]
        i = bisect.bisect_left(self.rented, (price, shop, movie))
        self.rented.pop(i)
        t = (price, shop)
        j = bisect.bisect_left(self.movies[movie], t)
        self.movies[movie].insert(j, t)

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]

