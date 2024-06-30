'''
2023/04/30 daily challenge
2024/06/30 daily challenge

union find approach

the idea is to count the edges which united two nodes (groups) for the first time,
and such edges can be considered necessary (non-removable).

if the edges between two nodes which were already united,
the edges can be removed. (and count it for the max number of removable edges.)

we need exact n-1 edges to make the graph with n nodes fully traversable,
so that (Type 3 + Type 1) and (Type 3 + Type 2) non-removable edges must be equal to n-1.
'''


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            '''
            :return: True if succeeded, False if already united.
            :rtype: bool
            '''
            x, y = find(parent, x), find(parent, y)
            if x == y:
                # x & y are already united.
                return False
            
            if x > y:
                parent[x] = y
            else:
                parent[y] = x
            return True

        removable = 0  # max number of removable edges

        # proceed Type 3 edges (Alice & Bob)
        both_edges = 0  # min edges can be traversed by both Alice & Bob
        uf_both = [i for i in range(n+1)]  # note: 1 <= n <= 10**5
        for t, u, v in edges:
            if t == 3:
                if union(uf_both, u, v):
                    both_edges += 1
                else:
                    # u & v are already reachable, the edge can be removed.
                    removable += 1

        alice_edges = bob_edges = both_edges
        # 2 copies for alice & bob respectively
        uf_alice = uf_both  # (alice & bob) + alice only edges
        uf_bob = uf_both.copy()  # (alice & bob) + bob only edges

        for t, u, v in edges:
            if t == 1:
                # proceed Type 1 edges (Alice only)
                if union(uf_alice, u, v):
                    alice_edges += 1
                else:
                    removable += 1
            elif t == 2:
                # proceed Type 2 edges (Bob only)
                if union(uf_bob, u, v):
                    bob_edges += 1
                else:
                    removable += 1

        if alice_edges == bob_edges == n - 1:
            # make sure all nodes are connected exactly with n-1 edges
            return removable

        # Alice & Bob cannot fully traverse the graph because there're nodes unreachable.
        return -1

